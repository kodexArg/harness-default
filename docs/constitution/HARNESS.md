---
title: Harness
description: What this harness is, how its pieces fit together, and how to work inside it
updated: 2026-08-06
---

This harness is a template for fullstack projects. Everything the project
**knows** lives under `docs/` — the constitution, the living documents, the
ADR and assertion families, and even the agent tooling. Outside `docs/`
there is only what the project **is**: the code roots and their state. The
written knowledge is served as a wikilink-aware vault by
`markdown-vault-mcp` — see [The vault](#the-vault) below.

## Tiers and families

Written knowledge comes in two kinds of containers inside `docs/`.
`docs/constitution/` and the documents sitting directly in `docs/` are
**tiers**: every document sorts into one of them by a single question — **is
this both meaningful and stable?** `docs/adrs/` and `docs/assertions/` are
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

## docs/adrs/

Architecture Decision Records: the memory of the why, not just the what. An
ADR is attached to a *theme* and states numbered rules; its policy may change
many times in place — each displaced policy recorded in the ADR's own
`REJECTED` section — without the file ever moving. Presence in `docs/adrs/`
is what makes a rule binding, and a whole file retires to `docs/obsolete/`
only when its theme ends. Discipline and template in
[adr-00](../adrs/adr-00-discipline.md). Standing order of the harness ADRs:

| ADR | Theme |
|---|---|
| [[adr-01-constitution]] | Source markdown — PRD, constitution, families, authority |
| [[adr-02-harness]] | Skills, hooks, agents — tooling that serves the law |
| [[adr-03-guardians]] | Guardian agents and the dispatch safety net |
| [[adr-04-issue-delivery]] | triage-and-fix cast and skill |

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
→ a test that fails above that bound). The `kskill-assertion-review` skill
interprets the paragraph, demands those tests via [[TDD]], drives the fix or
feature, and stamps `verified` only when the tests pass.

Assertions are always aligned with `PRD.md` and this constitution. They are
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
Django REST Framework project is the archetype: routing, auth, ORM, admin,
the whole service surface in a single place, so splitting it into "services"
adds nothing. One frontend that is almost always a web client. Documented in
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
issue to a PR is the in-tree party: skill `docs/skills/kskill-triage-and-fix/`,
cast `docs/agents/kwf-*.md`. Binding rules: [[adr-04-issue-delivery]].
Operator steps: [[CLONE]]. Runtime spawn map (Kimi / Claude / Cursor-Grok):
`docs/skills/kskill-triage-and-fix/references/runtimes.md`.

Phases: forest → tavern → camp → stalking → plaza → post-bard. After plaza,
the owner process runs `guardian-dispatch --bundle`, pastes that payload
into each owed guardian ([[adr-03-guardians]] rule 9), dispatches them in
parallel on the cheap tier, and runs `kskill-assertion-review` when assertions
were touched. Important features enter as assertion laws ([[TDD]]), not as
silent code.

## Agent tooling

Every artifact is prefixed by what it is — `kskill-*` skills, `khook-*` hooks,
`kbot-*` agents, `kwf-*` the delivery party ([[adr-02-harness]] rule 8). The
prefix is how a name read cold says which tree owns it and which contract
applies.

- **`docs/skills/`** — skills agnostic to the LLM but useful for this
  project: self-contained instruction packages an agent loads on demand.
  Wire each into the runtime's skill discovery (symlink or reference).
  - **law skills** — `kskill-assertion-review` (laws → tests → code via
    [[TDD]]) and `kskill-triage-and-fix` (issue → PR party). These two are the
    standing residents; the law is their subject.
  Every skill below the two law skills was **ported from another clone** and
  wears a banner saying so: its citations and its hardcoded specifics (cloud
  accounts, profiles, slugs, template paths) belong to the origin project and
  bind nothing here until remapped ([[adr-02-harness]] rule 5).

  - **stack skills** — `kskill-astro-7` (Astro 7 + Svelte islands),
    `kskill-django-6-drf` (Django 6 + DRF), and the AWS set
    (`kskill-aws-s3`, `-iam`, `-containers`, `-cost`, `-observability`,
    `-cloudwatch-query`, `-cloudwatch-alarms`, `-secrets-manager`,
    `-secrets-create`, `-troubleshoot`).
  - **docs skills** — `kskill-live-doc` (code ↔ doc linker),
    `kskill-markdown-vault` (query the `docs/` vault graph),
    `kskill-obsidian-markdown` (vault-flavored markdown),
    `kskill-report` / `kskill-reporte` (one self-contained dark HTML report,
    English and Spanish twins; they save to disk and report the path —
    this harness ships no send channel).
  - **orchestration skills** — `kskill-orchestrator` (main chat as team lead
    over `kbot-*` workers), `kskill-triage` (cheap go/no-go before spending
    tokens), `kskill-wf-triage-and-fix` (the same delivery party driven by the
    Workflow tool instead of by hand). These serve
    [[adr-04-issue-delivery]] — they do not outrank it, and where a mechanic
    differs the ADR is right and the skill is the defect.
- **`docs/hooks/`** — LLM-agnostic automation attached to agent or tooling
  lifecycle events. The first resident is the dispatch safety net
  ([[adr-03-guardians]] rules 3, 8, 9): `khook-guardian-dispatch` maps a batch's
  changed files against the `watch:` globs each agent declares in its own
  frontmatter and names the guardians owed; `--bundle` adds hit paths, diff,
  and a live ADR `use_case` index for the owner to paste into each guardian
  prompt. `khook-pre-commit` speaks the name-only form at every commit — wired
  once per clone with
  `ln -s ../../docs/hooks/khook-pre-commit .git/hooks/pre-commit`. It warns rather
  than blocks: the duty it voices binds the agent that reads it. The same
  script is the post-bard entry for [[adr-04-issue-delivery]].

  The Claude-native lifecycle hooks, wired in `.claude/settings.json`:

  | Hook | Event | Duty |
  |---|---|---|
  | `khook-load-ssot.py` | SessionStart | injects [[PRD]] and [[API]] so the standing requirement is met deterministically |
  | `khook-require-api-read.py` | UserPromptSubmit | a prompt touching the route surface must re-read [[API]] first |
  | `khook-require-pr-flow.py` | PreToolUse (Bash) | issue → PR reminder on commit / push to main ([[adr-04-issue-delivery]]) |
  | `khook-check-adr.py` | PostToolUse (Write\|Edit) | every ADR written matches the [[adr-00-discipline]] shape |
  | `khook-check-api.py` | PostToolUse (Write\|Edit) | no route in `urls.py` without its [[API]] row |
  | `khook-dispatch-guardians.py` | PostToolUse (Write\|Edit) | Claude-native voice of the dispatch safety net; delegates the watchlist to `khook-guardian-dispatch` |

  Its ADR-review nudge table ships **empty** on purpose: a nudge may only name
  ADRs this clone actually has ([[adr-02-harness]] rule 6). Each project fills
  it in as it writes its own ADRs.
- **`docs/agents/`** — agent role definitions. Guardians (`kbot-prd`,
  `kbot-adr`) gate the PRD and ADR set ([[adr-03-guardians]]); both
  declare `model_preference: cheap` and triage before opening law bodies.
  The `kwf-*` cast (18 nodes) runs issue delivery ([[adr-04-issue-delivery]]).
  The rest of the `kbot-*` roster are the orchestration workers
  `kskill-orchestrator` dispatches: `kbot-planner`, `kbot-builder`,
  `kbot-auditor`, `kbot-critic`, `kbot-low` / `-medium` / `-high`,
  `kbot-janitor`, `kbot-changelog`, `kbot-document-this`, `kbot-evaluate`.
  `.claude/agents/` at the root is the Claude Code link to this folder —
  one real copy, links everywhere else; Kimi uses `extra_agent_dirs`;
  Cursor/Grok injects the files per `runtimes.md`.

Tooling lives under `docs/` with the knowledge it belongs to, but the vault
excludes it: tooling conventions fix their filenames (a skill is always a
`SKILL.md`), which would collide with the vault's naming rule below.

## The vault

The vault root is `docs/`: everything documental is indexed, except the
tooling folders above. It is served as an Obsidian-style vault by
[markdown-vault-mcp](https://github.com/pvliesdonk/markdown-vault-mcp)
(recommended). The server config ships in `.mcp.json`; the local index lives
in `.mvmcp/` and is gitignored, so each clone builds its own.

```
uv tool install markdown-vault-mcp
```

Working rules:

- **Query the vault first** for any documentation question — search, read,
  backlinks, similarity — before grepping the markdown by hand.
- **Basenames are unique vault-wide.** A wikilink resolves by basename;
  duplicates make it resolve to the wrong file. This is why folders are kept
  alive with `.gitkeep`, never with placeholder readmes, and why the
  repository's only `README.md` sits at the root, outside the vault.
- **Wikilinks are welcome** between notes: `[[adr-00-discipline]]`,
  `[[HARNESS]]`. The vault tracks them as a graph — backlinks, orphans,
  broken links are all queryable.
- **Reindex after a batch of edits** before trusting link queries again.
