---
title: Harness
description: What this harness is, how its pieces fit together, and how to work inside it
updated: 2026-08-02
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
[adr-00](../adrs/adr-00-discipline.md).

## docs/assertions/

Assertions are the project's enforceable promises, and the mechanism matters:
they are how the constitution stops being prose and starts being checkable.

A single paragraph can define an assertion — something that must be
accomplished, stated with every rule it imposes:

> The user can get their last three messages, three clicks away from the home
> page, in a query, in less than 2 seconds.

Each assertion lives in its own file in `docs/assertions/`, states its rules
first, and ends with a `## RELATED` open/close list — `###` chapters linking
the tests, files, and anything else that realizes or verifies the promise. A
skill reviews every assertion periodically: the links must resolve, and the
promise must still hold.

Assertions are always aligned with `PRD.md` and this constitution. They are
the constitution made verifiable — when an assertion and the constitution
disagree, the assertion is the one that is wrong. Their boundary with
`REQUIREMENTS.md` is one of form: requirements *enumerate* what must hold;
an assertion takes one promise and makes it *checkable* — concrete rules,
linked evidence, periodic review. The discipline and template live in
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

## Agent tooling

- **`docs/skills/`** — skills agnostic to the LLM but useful for this
  project: self-contained instruction packages an agent loads on demand,
  some attached to specific files or workflows. TBD.
- **`docs/hooks/`** — LLM-agnostic automation attached to agent or tooling
  lifecycle events. TBD.
- **`docs/agents/`** — LLM-agnostic agent role definitions. TBD.

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
