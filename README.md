---
title: harness-default
description: Template harness for fullstack projects — constitution, docs, ADRs, and agent tooling scaffolding
updated: 2026-08-02
---

# harness-default

Template harness for fullstack projects. Clone it, fill the constitution, and
let the docs and the ADR discipline grow with the project.

## Structure

| Path | Purpose |
|---|---|
| `docs/constitution/` | Meaningful and stable — not expected to change: harness, PRD, requirements, conventions, localisation, infrastructure. |
| `docs/` | The loose documents iterate with the code: glossary, architecture, frontend, backend, interfaces, services, API. |
| `docs/adrs/` | Architecture Decision Records — discipline in [adr-00](docs/adrs/adr-00-discipline.md). |
| `docs/assertions/` | Verifiable promises the project must keep, periodically re-checked — discipline in [assertion-00](docs/assertions/assertion-00-discipline.md). |
| `docs/skills/`, `docs/hooks/`, `docs/agents/` | LLM-agnostic agent tooling (TBD). |
| `frontend/` + `backend/` | Code roots, the specific pair — classic fullstack webapp. |
| `interfaces/` + `services/` | Code roots, the generalistic pair — many services, many interfaces. |
| `state/` | Database state — Postgres docker volumes, SQLite files. Contents gitignored. |

Everything the project knows lives under `docs/`; the root holds only what
the project is. Both code-root pairs ship side by side: **the first action
in a new project is to pick one pair of folders and delete the other** — all
four stack documents stay in `docs/`. The duality is explained in
[docs/constitution/HARNESS.md](docs/constitution/HARNESS.md).

Every markdown document carries YAML frontmatter — the convention lives in
[docs/constitution/CONVENTION.md](docs/constitution/CONVENTION.md).

`docs/` is served as a wikilink-aware vault by
[markdown-vault-mcp](https://github.com/pvliesdonk/markdown-vault-mcp)
(recommended — config ships in `.mcp.json`). How to work inside the harness
is described in [docs/constitution/HARNESS.md](docs/constitution/HARNESS.md).

## License

[MIT](LICENSE)
