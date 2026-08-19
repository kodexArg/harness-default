#!/usr/bin/env python3
"""Tests for nudge hooks and guardian dispatch safety net."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DISPATCH_HOOK = ROOT / "hooks" / "khook-dispatch-guardians.py"
API_READ_HOOK = ROOT / "hooks" / "khook-require-api-read.py"
CHECK_API_HOOK = ROOT / "hooks" / "khook-check-api.py"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise AssertionError(msg)


def ok(msg: str) -> None:
    print(f"ok  {msg}")


def run_dispatch(rel: str, session: str, tool: str = "Edit") -> subprocess.CompletedProcess:
    payload = json.dumps({
        "tool_name": tool,
        "session_id": session,
        "tool_input": {"file_path": str(ROOT / rel)},
    })
    env = os.environ.copy()
    env["CLAUDE_PROJECT_DIR"] = str(ROOT)
    return subprocess.run(
        [sys.executable, str(DISPATCH_HOOK)],
        input=payload,
        capture_output=True,
        text=True,
        env=env,
        timeout=5,
    )


def test_guardian_dispatch_nudges() -> None:
    session = "test-session-1"
    # Clean up test seen file if exists
    seen_file = ROOT / ".claude" / f".nudge-seen-{session}"
    if seen_file.exists():
        seen_file.unlink()

    try:
        # 1. Edit PRD -> should nudge kbot-prd
        res = run_dispatch("docs/constitution/PRD.md", session)
        if res.returncode != 0:
            fail(f"dispatch hook failed: {res.stderr}")
        if "kbot-prd" not in res.stdout:
            fail(f"expected kbot-prd in output, got: {res.stdout}")
        ok("PRD edit nudges kbot-prd")

        # 2. Re-edit PRD in same session -> should dedup (no output)
        res2 = run_dispatch("docs/constitution/PRD.md", session)
        if res2.stdout.strip():
            fail(f"expected dedup empty output, got: {res2.stdout}")
        ok("same-session PRD edit deduped")

        # 3. Edit ADR in new session -> should nudge kbot-adr
        session2 = "test-session-2"
        seen_file2 = ROOT / ".claude" / f".nudge-seen-{session2}"
        if seen_file2.exists():
            seen_file2.unlink()
        try:
            res3 = run_dispatch("adrs/adr-01-constitution.md", session2)
            if "kbot-adr" not in res3.stdout:
                fail(f"expected kbot-adr in output, got: {res3.stdout}")
            ok("ADR edit nudges kbot-adr in new session")
        finally:
            if seen_file2.exists():
                seen_file2.unlink()
    finally:
        if seen_file.exists():
            seen_file.unlink()



def test_api_read_nudge() -> None:
    # 1. Prompt mentioning API endpoint
    payload = json.dumps({"prompt": "Please add a new endpoint to the API"})
    res = subprocess.run(
        [sys.executable, str(API_READ_HOOK)],
        input=payload,
        capture_output=True,
        text=True,
        timeout=5,
    )
    if "API gate" not in res.stdout:
        fail(f"expected API gate warning in stdout, got: {res.stdout}")
    ok("API prompt triggers read reminder")

    # 2. Prompt not touching API
    payload2 = json.dumps({"prompt": "Refactor the helper functions in utils.py"})
    res2 = subprocess.run(
        [sys.executable, str(API_READ_HOOK)],
        input=payload2,
        capture_output=True,
        text=True,
        timeout=5,
    )
    if res2.stdout.strip():
        fail(f"expected empty stdout for non-API prompt, got: {res2.stdout}")
    ok("non-API prompt produces no output")


def test_check_api_hook_blocking() -> None:
    with tempfile.NamedTemporaryFile(suffix="_urls.py", mode="w", delete=False) as f:
        f.write('urlpatterns = [path("unregistered/secret/route/", view)]')
        temp_name = f.name
    try:
        res = subprocess.run(
            [sys.executable, str(CHECK_API_HOOK), temp_name],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if res.returncode != 2:
            fail(f"expected check-api to exit 2 on unlisted route, got {res.returncode}")
        if "is not declared in docs/API.md" not in res.stderr:
            fail(f"expected route declaration error in stderr, got: {res.stderr}")
        ok("check-api hook blocks undeclared routes with exit 2")
    finally:
        Path(temp_name).unlink(missing_ok=True)


def main() -> int:
    tests = [
        test_guardian_dispatch_nudges,
        test_api_read_nudge,
        test_check_api_hook_blocking,
    ]
    failed = 0
    for fn in tests:
        try:
            fn()
        except AssertionError:
            failed += 1
        except Exception as exc:
            print(f"FAIL: {fn.__name__}: {exc}", file=sys.stderr)
            failed += 1

    if failed:
        print(f"\n{failed} test(s) failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
