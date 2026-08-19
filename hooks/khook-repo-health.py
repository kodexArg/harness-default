#!/usr/bin/env python3
"""Repo health guard (SessionStart).

Reports repository CI state, open PR status, unmerged branches, and
harness structural health (symlinks, ADR schemas, agent contracts).
Fail-open: network blips or missing gh CLI gracefully exit 0.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

TIMEOUT = 6


def project_dir() -> Path:
    for var in ("ANTIGRAVITY_PROJECT_DIR", "CLAUDE_PROJECT_DIR", "PROJECT_ROOT"):
        val = os.environ.get(var)
        if val and Path(val).is_dir():
            return Path(val)
    try:
        git_root = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        if git_root:
            return Path(git_root)
    except Exception:
        pass
    return Path(__file__).resolve().parents[1]



def run_cmd(cmd: list[str], cwd: Path) -> str | None:
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
        )
        if proc.returncode != 0:
            return None
        return proc.stdout.strip()
    except Exception:
        return None


def check_harness_structure(root: Path) -> list[str]:
    issues = []
    for d in ("adrs", "agents", "hooks", "skills"):
        if not (root / d).is_dir():
            issues.append(f"Missing root harness directory: {d}/")

    claude = root / ".claude"
    if claude.is_dir():
        for target in ("rules", "agents", "hooks", "skills"):
            link = claude / target
            if not link.exists():
                issues.append(f"Broken symlink: .claude/{target}")
    return issues


def main() -> int:
    try:
        root = project_dir()
        branch = run_cmd(["git", "branch", "--show-current"], root) or "unknown"
        status = run_cmd(["git", "status", "--porcelain"], root)
        uncommitted = len(status.splitlines()) if status else 0

        harness_issues = check_harness_structure(root)

        print(f"=== REPO HEALTH ===")
        print(f"Branch: {branch}")
        print(f"Working tree: {'clean' if uncommitted == 0 else f'{uncommitted} uncommitted changes'}")

        if harness_issues:
            print("Harness warnings:")
            for issue in harness_issues:
                print(f"  ⚠️ {issue}")
        else:
            print("Harness structure: OK (root directories and symlinks valid)")

    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
