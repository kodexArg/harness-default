#!/usr/bin/env python3
"""Validates that .claude/hooks and all runtime projections mirror the root SSOTs."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

A = ROOT / ".claude" / "hooks"
B = ROOT / "hooks"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise AssertionError(msg)


def ok(msg: str) -> None:
    print(f"ok  {msg}")


def _files(tree: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for path in tree.rglob("*"):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts:
            continue
        if path.suffix == ".pyc":
            continue
        out[str(path.relative_to(tree))] = path
    return out


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_hooks_mirror_in_sync() -> None:
    if not A.is_dir():
        fail(f"missing hooks tree {A.relative_to(ROOT)}")
    if not B.is_dir():
        fail(f"missing hooks tree {B.relative_to(ROOT)}")

    if A.is_symlink() and A.resolve() == B.resolve():
        ok("hooks mirror is a single tree (.claude/hooks -> hooks)")
        return

    a_files = _files(A)
    b_files = _files(B)

    a_only = sorted(set(a_files) - set(b_files))
    b_only = sorted(set(b_files) - set(a_files))
    if a_only:
        fail(f"files present in {A.relative_to(ROOT)} but missing from {B.relative_to(ROOT)}: {a_only}")
    if b_only:
        fail(f"files present in {B.relative_to(ROOT)} but missing from {A.relative_to(ROOT)}: {b_only}")

    diverged = []
    for rel in sorted(a_files):
        if _sha256(a_files[rel]) != _sha256(b_files[rel]):
            diverged.append(rel)
    if diverged:
        fail(f"mirrored hook files diverged in content: {diverged}")

    ok(f"hooks mirror in sync ({len(a_files)} file pairs verified)")


def test_projections_are_symlinks() -> None:
    projections = [
        ROOT / ".claude" / "rules",
        ROOT / ".claude" / "agents",
        ROOT / ".claude" / "hooks",
        ROOT / ".claude" / "skills",
        ROOT / ".agents" / "agents",
        ROOT / ".grok" / "skills",
        ROOT / "CLAUDE.md",
        ROOT / "GEMINI.md",
    ]
    for p in projections:
        if not p.exists():
            fail(f"Projection missing: {p.relative_to(ROOT)}")
        if not p.is_symlink():
            fail(f"Projection must be a symlink: {p.relative_to(ROOT)}")
    ok("all runtime projections are verified symlinks")


def main() -> int:
    tests = [test_hooks_mirror_in_sync, test_projections_are_symlinks]
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
