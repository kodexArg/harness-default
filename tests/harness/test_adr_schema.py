#!/usr/bin/env python3
"""Validates the ADR frontmatter contract defined in adr-00-adr-doctrine."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ADRS = ROOT / "adrs"

REQUIRED_KEYS = (
    "title",
    "type",
    "status",
    "created",
    "tags",
    "paths",
    "related_adrs",
    "related_agents",
    "description",
    "applies_when",
)

DESCRIPTION_MIN_WORDS = 20
DESCRIPTION_MAX_WORDS = 50


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n?(.*)\Z", text, re.DOTALL)
    if not match:
        return "", text
    return match.group(1), match.group(2)


def top_level_keys(fm: str) -> list[str]:
    return [m.group(1) for m in re.finditer(r"^([A-Za-z_][\w-]*):", fm, re.MULTILINE)]


def scalar(fm: str, key: str) -> str | None:
    match = re.search(rf"^{key}:[ \t]*(.*)$", fm, re.MULTILINE)
    return match.group(1).strip() if match else None


def test_adr_frontmatters():
    failures = []
    adr_files = sorted(ADRS.glob("adr-*.md"))
    assert len(adr_files) > 0, "No ADR files found in adrs/"

    for path in adr_files:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if not fm:
            failures.append(f"{rel}: missing YAML frontmatter")
            continue

        keys = top_level_keys(fm)
        for req in REQUIRED_KEYS:
            if req not in keys:
                failures.append(f"{rel}: missing required key `{req}`")

        title = scalar(fm, "title")
        if title != path.stem:
            failures.append(f"{rel}: title `{title}` does not match filename stem `{path.stem}`")

        adr_type = scalar(fm, "type")
        if adr_type != "adr":
            failures.append(f"{rel}: type must be `adr`, got `{adr_type}`")

        status = scalar(fm, "status")
        if status not in ("active", "defered", "superseded"):
            failures.append(f"{rel}: invalid status `{status}`")

        desc = scalar(fm, "description") or ""
        words = len(desc.split())
        if not (DESCRIPTION_MIN_WORDS <= words <= DESCRIPTION_MAX_WORDS):
            failures.append(f"{rel}: description is {words} words, must be between {DESCRIPTION_MIN_WORDS} and {DESCRIPTION_MAX_WORDS}")

    assert not failures, "\n".join(failures)


if __name__ == "__main__":
    test_adr_frontmatters()
    print("ok  all ADR frontmatters valid")
