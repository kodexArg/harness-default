---
title: Harness
description: What this harness is, how its pieces fit together, and how to work inside it
updated: 2026-08-18
---

This harness is a generic, stack-agnostic template for agentic software engineering. Written knowledge lives under `docs/` — the constitution, the living documents, and the assertion family. Harness artifacts live at the repository root (`adrs/`, `agents/`, `hooks/`, `skills/`) per [[adr-02-harness-layout]]. The written knowledge is served as a wikilink-aware vault by `markdown-vault-mcp` — see [The vault](#the-vault) below.

## Tiers and families

Written knowledge comes in two kinds of containers inside `docs/`.
`docs/constitution/` and the documents sitting directly in `docs/` are
**tiers**: every document sorts into one of them by a single question — **is
this both meaningful and stable?** `adrs/` and `docs/assertions/` are
**families**: numbered, append-only files that do not sort — they
accumulate, each ruled by its own `-00` discipline file.

### docs/constitution/

The constitution holds what the project does not expect to change. These
documents are foundational and binding: they are read first, they settle
arguments, and they are amended rarely and deliberately. Changing the
constitution is an event, not routine upkeep.

A document earns its place here only by being both things at once — meaningful
*and* stable. Meaningful but volatile belongs one level up, directly in
`docs/`; stable but unimportant belongs there too.

### docs/ — the loose documents

Everything else sits directly in `docs/`, which covers two kinds of material:

- **Documents that iterate with the code.** `API.md` is the clearest case: the
  surface it describes moves constantly, and the document is expected to move
  with it.
- **Documentation that is stable but not load-bearing.** Useful reference, kept
  current, but a change to it would not alter how the project is run.

### How the current files sort

| File | Tier | Why |
|---|---|---|
| `INFRASTRUCTURE.md` | constitution | The bare metal beneath the project — cloud choice, resources. Set up once; barely varies. |
| `ARCHITECTURE.md` | docs | Expected to vary as the system evolves. |
| `API.md` | docs | Iterates constantly with the code. |
| `FRONTEND.md` / `BACKEND.md` | docs | Describe the living code; iteration is the norm. |
| `INTERFACES.md` / `SERVICES.md` | docs | Same reason — the generalistic counterparts of the pair above. |
| `GLOSSARY.md` | docs | Canonical naming is meaningful, but the glossary grows for the entire life of the project — it fails the stability test. |
| `USE-CASES.md` / `USER-STORIES.md` | docs | Open/close lists — the behavior in Gherkin and the wants behind it; both churn for the life of the product. |
| `TDD.md` | docs | Working method for assertion-driven delivery — iterates with how the project ships laws into tests and code. |
| `CLONE.md` | docs | First-run operator checklist — code roots, hooks, vault, delivery. |

When a new document appears, apply the same two tests: *would changing this
alter how the project is run?* and *do we expect it to change again soon?*
Only a yes to the first and a no to the second puts it in the constitution.

## adrs/

Architecture Decision Records: the memory of the why, not just the what. An
ADR states numbered rules; presence in `adrs/` is what makes a rule binding.
Any semantic change executes the supersession protocol ([[adr-00-adr-doctrine]]):
the superseded body moves to `docs/obsolete/defered-adr-NN-slug.md`, the original
keeps only its frontmatter with `status: defered`, and any replacement is written
as a new ADR. Discipline and template in [[adr-00-adr-doctrine]]. Standing order
of the harness ADRs:

| ADR | Theme |
|---|---|
| [[adr-00-adr-doctrine]] | ADR architecture, structured frontmatter, trigger routing, supersession |
| [[adr-01-constitution]] | Source markdown — PRD, constitution, families, authority |
| [[adr-02-harness-layout]] | Skills, hooks, agents, ADRs — root layout and kind-prefixed naming |
| [[adr-03-agent-contract]] | Frontmatter contracts for agents, model inherit, quick exit, tool sequences |
| [[adr-04-guardians-and-delivery]] | Guardian gating architecture, repo-health, and issue-to-PR delivery |

## docs/assertions/

Assertions are the harness's **novel piece**: owner-reserved **laws** that a
skill must pass. Everything else in this tree is ordinary scaffolding plus
opinionated PRD and ADRs-as-rules; assertions are the entry path for
solutions that manifest first as proving tests ([[TDD]]) and then as code.

The family is completely optional — a project with none is healthy. They
stay few because each one costs real compute (interpret, demand tests,
implement, re-verify). Presence is what binds: every assertion that exists
must be met.

A single paragraph defines the law — every rule it imposes, concrete enough
to check:

> The user can get their last three messages, three clicks away from the home
> page, in a query, in less than 2 seconds.

Each assertion lives in its own file in `docs/assertions/`, states its rules
first, and ends with a `## RELATED` open/close list. The `### Tests` chapter
must link runnable tests that **demonstrate** the law (e.g. latency ≤ 500ms
→ a test that fails above that bound). The `k-assertion-review` skill
interprets the paragraph, demands those tests via [[TDD]], drives the fix or
feature, and stamps `verified` only when the tests pass.

Assertions are always aligned with `docs/constitution/PRD.md` and this constitution. They are
the constitution made verifiable — when an assertion and the constitution
disagree, the assertion is the one that is wrong. Their boundary with
`REQUIREMENTS.md` is one of form: requirements *enumerate* what must hold;
an assertion takes one promise and makes it a law with a proving path. The
discipline and template live in
[assertion-00](../assertions/assertion-00-discipline.md).

## Code roots — pick your pair

The harness ships **two vocabularies for the same two slots**, side by side.
**The first action in a new project is to pick one pair of folders and
delete the other.** The pick is about folders only: all four documents —
`FRONTEND.md`, `BACKEND.md`, `INTERFACES.md`, `SERVICES.md` — live together
in `docs/` regardless.

### frontend/ + backend/ — the specific pair

For the classic fullstack webapp. One backend that owns everything — a
Django REST Framework or FastAPI project is the archetype: routing, auth, ORM, admin,
the whole service surface in a single place. One frontend that is almost always a web client. Documented in
`docs/FRONTEND.md` and `docs/BACKEND.md`.

### interfaces/ + services/ — the generalistic pair

For projects shaped like a constellation rather than a webapp: several small
services (an API, an MCP server, workers, bots) and several interfaces (web,
CLI, mobile, a Telegram bot). Each component gets its own subfolder —
`services/api/`, `interfaces/cli/`. Documented in `docs/INTERFACES.md` and
`docs/SERVICES.md`.

### Picking

The two pairs are the same duality at different plurality: a backend is the
single-service case, a frontend the single-interface case. Pick by shape —
one of each → `frontend/` + `backend/`; many of either → `interfaces/` +
`services/`. Either way the architecture sentence stays the same:
**interfaces talk to services, services own state.**

### state/

`state/` belongs to both worlds and survives the pick: everything
database-related lives here — PostgreSQL docker volumes, SQLite files,
dumps. Contents are gitignored; only the folder itself is tracked.

All code roots hold code and runtime state, not knowledge: they live outside
`docs/` and outside the vault, and they carry a `.gitkeep` instead of a
readme — their description lives here and in the docs tier.

## Issue delivery — triage-and-fix

This harness owns the **law** and the **delivery cast**. Taking one GitHub
issue to a PR is the in-tree party: skill `skills/k-triage-and-fix/`,
cast `agents/kwf-*.md`. Binding rules: [[adr-04-guardians-and-delivery]].
Operator steps: [[CLONE]]. Runtime spawn map (Kimi / Claude / Cursor-Grok):
`skills/k-triage-and-fix/references/runtimes.md`.

Phases: forest → tavern → camp → stalking → plaza → post-bard. After plaza,
the owner process runs `guardian-dispatch --bundle`, pastes that payload
into each owed guardian ([[adr-04-guardians-and-delivery]]), dispatches them in
parallel on the cheap tier, and runs `k-assertion-review` when assertions
were touched. Important features enter as assertion laws ([[TDD]]), not as
silent code.

## Agent tooling

Every artifact is prefixed by what it is — `k-*` skills, `khook-*` hooks,
`kbot-*` agents, `kwf-*` the delivery party ([[adr-02-harness-layout]]). The
prefix is how a name read cold says which tree owns it and which contract
applies.

- **`skills/`** — self-contained instruction packages an agent loads on demand.
  - **law skills** — `k-assertion-review` (laws → tests → code via
    [[TDD]]) and `k-triage-and-fix` (issue → PR party).
  - **docs skills** — `k-live-doc` (code ↔ doc linker),
    `k-markdown-vault` (query the `docs/` vault graph),
    `k-obsidian-markdown` (vault-flavored markdown),
    `k-report` / `k-reporte` (self-contained dark HTML reports in English/Spanish).
  - **orchestration skills** — `k-orchestrator` (main chat as team lead
    over `kbot-*` workers), `k-triage` (cheap go/no-go card before spending
    tokens), `k-wf-triage-and-fix` (workflow-driven delivery party).

- **`hooks/`** — deterministic automation attached to agent or tooling
  lifecycle events.
  - `khook-repo-health.py`: repo CI state, branch, uncommitted count, harness structure and symlink health.
  - `khook-load-ssot.py`: preloads PRD.md and API.md into context at session start.
  - `khook-load-adr-index.py`: preloads the active ADR trigger index at session start.
  - `khook-require-pr-flow.py`: issues non-blocking PR-flow reminders on git commits/pushes.
  - `khook-check-adr.py`: enforces ADR frontmatter schema and doctrine shape.
  - `khook-guardian-dispatch` / `khook-dispatch-guardians.py`: agnostic engine and Claude wrapper mapping changed files to owed guardian agents.
  - `khook-pre-commit`: git pre-commit hook running staged guardian checks.

  The Claude-native lifecycle hooks, wired in `.claude/settings.json`:

  | Hook | Event | Duty |
  |---|---|---|
  | `khook-repo-health.py` | SessionStart | Diagnostic of repo health, uncommitted status, and symlinks |
  | `khook-load-ssot.py` | SessionStart | Injects [[PRD]] and [[API]] into context |
  | `khook-load-adr-index.py` | SessionStart | Injects active ADR trigger index into context |
  | `khook-require-pr-flow.py` | PreToolUse (Bash) | PR-flow reminder on commit / push to main |
  | `khook-check-adr.py` | PostToolUse (Write\|Edit) | Validates ADR shape and frontmatter |
  | `khook-dispatch-guardians.py` | PostToolUse (Write\|Edit) | PostToolUse guardian dispatch safety net |

- **`agents/`** — autonomous agent role definitions.
  - Guardians (`kbot-prd`, `kbot-adr`) gate the PRD, constitution, and ADR set.
  - The `kwf-*` cast (18 nodes) executes issue delivery ([[adr-04-guardians-and-delivery]]).
  - The `kbot-*` roster provides specialized worker agents for `k-orchestrator`:
    `kbot-planner`, `kbot-builder`, `kbot-auditor`, `kbot-critic`, `kbot-low` / `-medium` / `-high`,
    `kbot-janitor`, `kbot-changelog`, `kbot-document-this`, `kbot-evaluate`.
  - `.claude/agents/` at root symlinks to `agents/`.

## The vault

The vault root is `docs/`: everything documental is indexed, while root harness folders (`adrs/`, `agents/`, `hooks/`, `skills/`) remain separate. It is served as an Obsidian-style vault by
[markdown-vault-mcp](https://github.com/pvliesdonk/markdown-vault-mcp). The server config ships in `.mcp.json`.

```bash
uv tool install markdown-vault-mcp
```

Working rules:

- **Query the vault first** for any documentation question before grepping by hand.
- **Basenames are unique vault-wide.** A wikilink resolves by basename.
- **Wikilinks are welcome** between notes: `[[adr-00-adr-doctrine]]`,
  `[[HARNESS]]`.
- **Reindex after a batch of edits** before trusting link queries again.

