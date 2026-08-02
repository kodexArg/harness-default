---
title: Convention
description: Global conventions that apply to every document in this harness
status: active
updated: 2026-08-02
---

## Frontmatter documentation

Every markdown file in the knowledge tiers — `constitution/`, `docs/`,
`adrs/`, `assertions/`, and the root `README.md` — opens with a YAML
frontmatter block. It is the machine-readable summary of the document: agents
read it to decide whether the file is worth opening, and tooling can index it
without parsing prose.

Tooling files are exempt: `skills/`, `hooks/`, and `agents/` obey the formats
their tools fix (a skill's `SKILL.md` carries `name` + `description`), not
this convention.

Required keys:

| Key | Value |
|---|---|
| `title` | Short human-readable title. |
| `description` | One line stating what the document contains and when to read it. |
| `status` | `draft` — being written · `active` — current and binding · `deprecated` — kept for history, no longer applies. |
| `updated` | Date of last meaningful edit, `YYYY-MM-DD`. |

Rules:

- Frontmatter is the first thing in the file: `---` on line 1.
- Keys are lowercase and flat (no nesting); values are plain YAML scalars.
- `description` fits in one line (< 160 chars) — it is the hook an agent uses
  to decide relevance without opening the body.
- Document families may extend the base set with their own keys and may
  refine the `status` vocabulary in their discipline file; they never remove
  keys. ADRs and assertions are the first such families — ADRs replace the
  status values with their own lifecycle and add `date` / `supersedes` /
  `superseded-by`; assertions add `verified`. See
  [adr-00-discipline](../adrs/adr-00-discipline.md) and
  [assertion-00-discipline](../assertions/assertion-00-discipline.md).
