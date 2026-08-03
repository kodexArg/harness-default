---
title: harness-default
description: Scaffolding for fullstack projects — constitution, ADRs as rules, assertions as the entry path for solutions, and in-tree triage-and-fix delivery
updated: 2026-08-02
---

# harness-default

This repository is **scaffolding**, like any other project template: a place
to put a constitution, living docs, code roots, and agent tooling. Clone it,
pick a code-root pair, fill the brackets, grow the docs with the code.

Two layers of opinion sit on that scaffold — familiar if you have used
decision records and a product brief:

- **[PRD](docs/constitution/PRD.md)** — the objective at the top of the
  authority order.
- **[ADRs](docs/adrs/)** — decisions as binding rules. Presence in
  `docs/adrs/` is what makes a rule in force; where code and ADR disagree,
  the ADR is right. Discipline in [adr-00](docs/adrs/adr-00-discipline.md).

Everything else in the tree is ordinary harness structure. The one piece
that is **not** ordinary scaffolding is below.

## The novel piece: assertions

**Assertions are the only novel mechanism in this harness.** They are laws
the project must pass — reserved for the owner, kept few, because each one
demands real compute: an agent must interpret the law, demand the tests that
prove it, and drive the fix or feature until those tests hold forever.

An assertion is a Gherkin use case ([USE-CASES.md](docs/USE-CASES.md))
collapsed into one checkable paragraph. Example scenario:

```gherkin
Given a value X stored in the database
When the frontend displays X
Then the value shown equals the value stored
```

becomes the law:

> The value of X in the database is always the value displayed in the
> frontend.

Or a latency law: *the backend responds in 500ms or less* — then
`## RELATED` must link at least one test that demonstrates that bound. A
promise with no proving test is not an assertion; it is a wish.

### Entry path for solutions

Assertions are how solutions enter the project and stay:

1. The owner writes a law under `docs/assertions/`.
2. The [assertion-review](docs/skills/assertion-review/SKILL.md) skill
   interprets what the law means (LLM judgment), checks that `RELATED` links
   resolve, and **demands tests** following [TDD.md](docs/TDD.md).
3. Those tests prepare the fix or feature that satisfies the law — and they
   remain the permanent check that the law still holds.
4. Code follows the tests. The assertion, the tests, and the code coexist.

A project with **no** assertions is healthy. Presence is what binds: every
assertion that exists must be met. Discipline and template:
[assertion-00](docs/assertions/assertion-00-discipline.md).

## How to use this harness

Step-by-step: [CLONE.md](docs/CLONE.md).

- **Clone it.** Start inside a copy: pick a code-root pair (see
  [Structure](#structure)), fill the constitution, write your first ADR.
  Add an assertion only when you mean to spend the compute to prove it.
- **Reference it.** Point your LLM at `kodexArg/harness-default` and have it
  build your harness from this model.

### Issue delivery (triage-and-fix)

GitHub issue → PR ships **in this template**: skill
[triage-and-fix](docs/skills/triage-and-fix/SKILL.md), cast
`docs/agents/kwf-*.md`, binding [adr-02](docs/adrs/adr-02-issue-delivery.md).
Phases: forest → tavern → camp → stalking → plaza → post-bard
(`guardian-dispatch` + `assertion-review`). Runtime adapters (Kimi, Claude,
Cursor/Grok):
[runtimes.md](docs/skills/triage-and-fix/references/runtimes.md).
Assertions remain the entry path for important features — TDD first.

### ADRs are the rules

Decisions live as ADRs. Each ADR owns a theme for as long as the theme
lives — its policy changes in place, keeping history in `REJECTED`. Shape,
frontmatter, lifecycle: [adr-00](docs/adrs/adr-00-discipline.md).

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
| [TDD.md](docs/TDD.md) | How assertion-driven work writes tests first, then the code that passes them. |
| [CLONE.md](docs/CLONE.md) | First-run checklist — code roots, hooks, vault, optional triage-party. |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System-level design — components, boundaries, and how they talk. |
| [API.md](docs/API.md) | The API surface — endpoints, contracts, auth, versioning. |
| [FRONTEND.md](docs/FRONTEND.md) / [BACKEND.md](docs/BACKEND.md) | Stack, structure, and conventions of the specific code-root pair. |
| [INTERFACES.md](docs/INTERFACES.md) / [SERVICES.md](docs/SERVICES.md) | The same, for the generalistic pair — web, CLI, bots / APIs, workers, MCP servers. |

All four stack documents ship regardless of which code-root pair the project
keeps — the pick is about folders, the knowledge stays.

### Agent tooling

- **Skills** (`docs/skills/`) are instruction packages. Wire each into your
  agent's skill discovery. Residents:
  [assertion-review](docs/skills/assertion-review/SKILL.md) (laws → tests →
  code via [TDD.md](docs/TDD.md)) and
  [triage-and-fix](docs/skills/triage-and-fix/SKILL.md) (issue → PR).
- **Agents** (`docs/agents/`) and **hooks** (`docs/hooks/`): guardians
  ([guardian-adr](docs/agents/guardian-adr.md),
  [guardian-prd](docs/agents/guardian-prd.md)) per
  [adr-01](docs/adrs/adr-01-guardians.md); the `kwf-*` delivery cast per
  [adr-02](docs/adrs/adr-02-issue-delivery.md);
  [guardian-dispatch](docs/hooks/guardian-dispatch) /
  [pre-commit](docs/hooks/pre-commit) as the safety net.

## Structure

| Path | Purpose |
|---|---|
| `docs/constitution/` | Meaningful and stable — harness, PRD, requirements, conventions, localisation, infrastructure. |
| `docs/` | Loose documents that iterate with the code: glossary, use cases, user stories, TDD, architecture, stack docs, API. |
| `docs/adrs/` | Architecture Decision Records — [adr-00](docs/adrs/adr-00-discipline.md). |
| `docs/assertions/` | Owner-reserved laws; entry path for solutions via tests — [assertion-00](docs/assertions/assertion-00-discipline.md). |
| `docs/skills/`, `docs/hooks/`, `docs/agents/` | Agent tooling — assertion-review, triage-and-fix, guardians, `kwf-*` cast, dispatch safety net. |
| [CLONE.md](docs/CLONE.md) | First-run checklist (code roots, hooks, vault, delivery). |
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
