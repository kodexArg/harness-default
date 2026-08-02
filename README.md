---
title: harness-default
description: Template harness for fullstack projects — constitution, docs, ADRs, and agent tooling scaffolding
status: active
updated: 2026-08-02
---

# harness-default

Template harness for fullstack projects. Clone it, fill the constitution, and
let the docs and the ADR discipline grow with the project.

## Structure

| Path | Purpose |
|---|---|
| `constitution/` | The non-negotiables: PRD, global conventions, localisation policy. |
| `docs/` | Living technical documentation: glossary, infrastructure, architecture, frontend, backend, API. |
| `adrs/` | Architecture Decision Records — discipline in [adr-00](adrs/adr-00-discipline.md). |
| `skills/` | LLM-agnostic skills useful to the project (TBD). |
| `hooks/` | LLM-agnostic hooks (TBD). |
| `agents/` | LLM-agnostic agent definitions (TBD). |

Every markdown file carries YAML frontmatter — the convention lives in
[constitution/CONVENTION.md](constitution/CONVENTION.md).

## License

[MIT](LICENSE)
