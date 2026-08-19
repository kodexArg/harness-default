---
title: Convention
description: Global conventions that apply to every document in this harness
version: v0.1.0
updated: 2026-08-18
---

## Frontmatter documentation

Every markdown document in this harness — across `docs/`, `adrs/`, `agents/`, `skills/`, and the root — opens with a YAML frontmatter block. It is the machine-readable summary and provenance of the document: agents read it to decide whether the file is worth opening, and tooling indexes and asserts version consistency across the entire harness.

Required keys:

| Key | Value |
|---|---|
| `title` | Short human-readable title (or `name` for skills/agents). |
| `description` | One line stating what the document contains and when to read it. |
| `version` | Mandatory harness version matching root `CHANGELOG.md` (e.g. `v0.1.0`). |
| `updated` | Date of last meaningful edit, `YYYY-MM-DD` (or `created` for ADRs). |

Rules:

- Frontmatter is the first thing in the file: `---` on line 1.
- Keys are lowercase and flat (no nesting, except where specific contracts like ADRs/agents permit lists); values are plain YAML scalars.
- `version` is mandatory in every markdown file in the harness and must strictly match the current version declared in root `CHANGELOG.md`.
- `description` fits in one line (< 160 chars) — it is the hook an agent uses to decide relevance without opening the body.
- A document that is present is valid — validity lives in the tree, not in an annotation. Information that stops being true is removed: deleted, retired whole to `docs/obsolete/`, or superseded per [[adr-00-adr-doctrine]].
- Document families may extend the base set with their own keys — assertions add `verified` — or their discipline file may own the frontmatter outright: ADRs carry their structured fields per [[adr-00-adr-doctrine]], agents carry their contract per [[adr-03-agent-contract]], and assertions follow [[assertion-00-discipline]].
