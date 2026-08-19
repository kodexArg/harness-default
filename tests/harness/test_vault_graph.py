#!/usr/bin/env python3
"""Validates the markdown vault link graph, agent soul references, and symlinks."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Syntax examples in obsidian documentation to ignore
IGNORED_SYNTAX_EXAMPLES = {
    "Note", "embed", "wikilinks", "Note Name", "", "image.png", "document.pdf",
    "improve workflow", "Algorithm Notes", "Architecture Diagram.png", "Meeting Notes 2024-01-10",
    "audio.mp3", "audio.ogg", "BaseFile.base", "Other Note", "..."
}



def test_vault_wikilinks_and_anchors():
    failures = []
    
    # Collect all valid target stems
    all_targets = set()
    for md in sorted(ROOT.glob("**/*.md")):
        if ".git" in md.parts or ".venv" in md.parts or "node_modules" in md.parts:
            continue
        all_targets.add(md.stem)
    
    # Add root special targets
    all_targets.update(["README", "LICENSE", "HARNESS", "PRD", "API", "BACKEND", "FRONTEND", "INTERFACES", "SERVICES", "GLOSSARY", "TDD", "USE-CASES", "USER-STORIES", "INFRASTRUCTURE", "CONVENTION", "REQUIREMENTS", "LOCALISATION"])
    
    for scan_dir in ("docs", "adrs", "agents", "skills"):
        dir_path = ROOT / scan_dir
        if not dir_path.is_dir():
            continue
        for md in sorted(dir_path.glob("**/*.md")):
            rel = md.relative_to(ROOT)
            text = md.read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(r"\[\[(.*?)\]\]", text):
                raw = m.group(1).strip()
                if not raw or raw in IGNORED_SYNTAX_EXAMPLES:
                    continue
                target = raw.split("|")[0].split("#")[0].strip()
                if not target or target in IGNORED_SYNTAX_EXAMPLES:
                    continue
                if target not in all_targets:
                    # Check if file exists under docs, adrs, etc.
                    found = list((ROOT / "docs").rglob(f"{target}.md")) + list((ROOT / "adrs").glob(f"{target}.md")) + list((ROOT / "agents").glob(f"{target}.md"))
                    if not found and not (ROOT / f"{target}.md").exists():
                        failures.append(f"{rel}: Dead wikilink [[{raw}]]")

    assert not failures, "\n".join(failures)


def test_agent_soul_references():
    failures = []
    agents_dir = ROOT / "agents"
    if agents_dir.is_dir():
        for agent_file in sorted(agents_dir.glob("*.md")):
            content = agent_file.read_text(encoding="utf-8")
            rel = agent_file.relative_to(ROOT)
            for m in re.finditer(r'Personality:\s*load\s+[`"]?([^`"\r\n]+)[`"]?', content):
                soul_rel = m.group(1).strip().strip('`"')
                resolved = ROOT / soul_rel
                if not resolved.is_file():
                    failures.append(f"{rel}: missing soul file '{soul_rel}'")
    assert not failures, "\n".join(failures)



def test_claude_symlinks():
    failures = []
    claude_dir = ROOT / ".claude"
    if claude_dir.is_dir():
        for link_name in ("rules", "agents", "hooks", "skills"):
            link_path = claude_dir / link_name
            if not link_path.exists():
                failures.append(f"Broken symlink: .claude/{link_name}")
            elif not link_path.is_symlink():
                failures.append(f"Not a symlink: .claude/{link_name}")
    assert not failures, "\n".join(failures)


if __name__ == "__main__":
    test_vault_wikilinks_and_anchors()
    test_agent_soul_references()
    test_claude_symlinks()
    print("ok  vault graph, agent souls, and symlinks valid")
