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
| `constitution/` | Meaningful and stable — not expected to change: harness, PRD, requirements, conventions, localisation, infrastructure. |
| `docs/` | Living technical documentation — iteration expected: glossary, architecture, frontend, backend, API. |
| `adrs/` | Architecture Decision Records — discipline in [adr-00](adrs/adr-00-discipline.md). |
| `assertions/` | Verifiable promises the project must keep, periodically re-checked — discipline in [assertion-00](assertions/assertion-00-discipline.md). |
| `frontend/` + `backend/` | Code roots, the specific pair — classic fullstack webapp. |
| `interfaces/` + `services/` | Code roots, the generalistic pair — many services, many interfaces. |
| `state/` | Database state — Postgres docker volumes, SQLite files. Contents gitignored. |

Both code-root pairs ship side by side: **the first action in a new project
is to pick one pair of folders and delete the other** — all four stack
documents stay in `docs/`. The duality is explained in
[constitution/HARNESS.md](constitution/HARNESS.md).
| `skills/` | LLM-agnostic skills useful to the project (TBD). |
| `hooks/` | LLM-agnostic hooks (TBD). |
| `agents/` | LLM-agnostic agent definitions (TBD). |

Every markdown file carries YAML frontmatter — the convention lives in
[constitution/CONVENTION.md](constitution/CONVENTION.md).

The knowledge tiers are served as a wikilink-aware vault by
[markdown-vault-mcp](https://github.com/pvliesdonk/markdown-vault-mcp)
(recommended — config ships in `.mcp.json`). How to work inside the harness
is described in [constitution/HARNESS.md](constitution/HARNESS.md).

## License

[MIT](LICENSE)
