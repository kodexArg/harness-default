---
title: harness-default
description: Template harness for fullstack projects — constitution, docs, ADRs, and agent tooling scaffolding
updated: 2026-08-02
---

# harness-default

Template harness for fullstack projects. Clone it, fill the constitution, and
let the docs and the ADR discipline grow with the project.

## How to use this harness

Two ways in, both good:

- **Clone it.** Start your project inside a copy of this repository: pick a
  code-root pair (see [Structure](#structure)), fill the constitution, write
  your first ADR.
- **Reference it.** Point your LLM at `kodexArg/harness-default` and have it
  build your harness using this one as the model — the structure, the
  disciplines, and the documents all translate.

Either way, what follows is what makes the harness work.

### ADRs are the rules

The obvious thing first, because everything hangs on it: **decisions live as
ADRs, and presence makes them binding.** An ADR in `docs/adrs/` is in force;
its numbered rules govern everything added to the project, and where code and
ADR disagree, the ADR is right. Each ADR owns a theme for as long as the
theme lives — its policy changes in place, keeping its own history. The whole
discipline — shape, frontmatter, lifecycle — is one file:
[adr-00](docs/adrs/adr-00-discipline.md), which is also its own template.

### Assertions

Assertions get an early chapter of their own because they are the harness's
teeth: the constitution made checkable.

They are completely optional — a project with none is healthy. Presence is
what binds: every assertion that exists must be met.

An assertion is a Gherkin use case ([USE-CASES.md](docs/USE-CASES.md)) made
an assertion — the scenario collapsed into one paragraph that must always
hold:

```gherkin
Given a value X stored in the database
When the frontend displays X
Then the value shown equals the value stored
```

becomes

> The value of X in the database is always the value displayed in the
> frontend.

Each assertion lives in its own file under `docs/assertions/`, states its
rules concretely enough to be checked, and ends with a `RELATED` list linking
the tests and files that realize it. A skill re-verifies every assertion
periodically: the links must resolve, and the promise must still hold.
Discipline and template in
[assertion-00](docs/assertions/assertion-00-discipline.md).

### The files

The constitution (`docs/constitution/`) — meaningful and stable, read first:

| File | What it holds |
|---|---|
| [PRD.md](docs/constitution/PRD.md) | What the product is, who it serves, what it must do — the top of the authority order. |
| [REQUIREMENTS.md](docs/constitution/REQUIREMENTS.md) | Functional and non-functional requirements the implementation must satisfy. |
| [HARNESS.md](docs/constitution/HARNESS.md) | What the harness is, how its pieces fit together, and how to work inside it. |
| [CONVENTION.md](docs/constitution/CONVENTION.md) | Global conventions that apply to every document — frontmatter included. |
| [LOCALISATION.md](docs/constitution/LOCALISATION.md) | Language policy for documentation and product copy. |
| [INFRASTRUCTURE.md](docs/constitution/INFRASTRUCTURE.md) | The bare metal beneath the project — hosting, cloud choice, resources. |

The loose documents (directly in `docs/`) — they iterate with the code:

| File | What it holds |
|---|---|
| [GLOSSARY.md](docs/GLOSSARY.md) | Canonical names for every domain concept — how we call each thing. |
| [USE-CASES.md](docs/USE-CASES.md) | The system's behavior as Gherkin scenarios — an open/close list, cited as `UC-NN`. |
| [USER-STORIES.md](docs/USER-STORIES.md) | Who wants what and why — `US-NN`, accepted when their linked cases pass. |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System-level design — components, boundaries, and how they talk. |
| [API.md](docs/API.md) | The API surface — endpoints, contracts, auth, versioning. |
| [FRONTEND.md](docs/FRONTEND.md) / [BACKEND.md](docs/BACKEND.md) | Stack, structure, and conventions of the specific code-root pair. |
| [INTERFACES.md](docs/INTERFACES.md) / [SERVICES.md](docs/SERVICES.md) | The same, for the generalistic pair — web, CLI, bots / APIs, workers, MCP servers. |

All four stack documents ship regardless of which code-root pair the project
keeps — the pick is about folders, the knowledge stays.

### Agent tooling

- **Skills** (`docs/skills/`) are LLM-agnostic: self-contained instruction
  packages an agent loads on demand. Agnostic still means wired — link each
  skill into your agent's own skill discovery (a symlink or a reference from
  the agent's skill folder) for it to load.
- **Agents** (`docs/agents/`) and **hooks** (`docs/hooks/`) are often
  agent-dependent — every runtime wires them its own way. What lives here are
  agnostic references to build your own from. The first residents are the two
  guardians — [guardian-adr](docs/agents/guardian-adr.md) and
  [guardian-prd](docs/agents/guardian-prd.md) — which watch the
  health of the ADR set and the PRD;
  [adr-01](docs/adrs/adr-01-guardians.md) makes their verdicts binding.
  The first hook is the guardians' safety net:
  [guardian-dispatch](docs/hooks/guardian-dispatch) names the guardians a
  batch owes, and [pre-commit](docs/hooks/pre-commit) says it at commit time.

## Structure

| Path | Purpose |
|---|---|
| `docs/constitution/` | Meaningful and stable — not expected to change: harness, PRD, requirements, conventions, localisation, infrastructure. |
| `docs/` | The loose documents iterate with the code: glossary, use cases, user stories, architecture, frontend, backend, interfaces, services, API. |
| `docs/adrs/` | Architecture Decision Records — discipline in [adr-00](docs/adrs/adr-00-discipline.md). |
| `docs/assertions/` | Verifiable promises the project must keep, periodically re-checked — discipline in [assertion-00](docs/assertions/assertion-00-discipline.md). |
| `docs/skills/`, `docs/hooks/`, `docs/agents/` | LLM-agnostic agent tooling — the guardians live in `docs/agents/`, their dispatch safety net in `docs/hooks/`; skills TBD. |
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
