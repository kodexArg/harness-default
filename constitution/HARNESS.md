---
title: Harness
description: What this harness is, how its pieces fit together, and how to work inside it
status: active
updated: 2026-08-02
---

This harness keeps a project's written knowledge in two tiers, and the sorting
rule is a single question: **is this both meaningful and stable?**

## constitution/

The constitution holds what the project does not expect to change. These
documents are foundational and binding: they are read first, they settle
arguments, and they are amended rarely and deliberately. Changing the
constitution is an event, not routine upkeep.

A document earns its place here only by being both things at once — meaningful
*and* stable. Meaningful but volatile belongs in `docs/`; stable but
unimportant belongs in `docs/` too.

## docs/

Everything else lives in `docs/`, which covers two kinds of material:

- **Documents that iterate with the code.** `API.md` is the clearest case: the
  surface it describes moves constantly, and the document is expected to move
  with it.
- **Documentation that is stable but not load-bearing.** Useful reference, kept
  current, but a change to it would not alter how the project is run.

## How the current files sort

| File | Tier | Why |
|---|---|---|
| `INFRASTRUCTURE.md` | constitution | Set up once; barely varies afterwards. |
| `ARCHITECTURE.md` | docs | Expected to vary as the system evolves. |
| `API.md` | docs | Iterates constantly with the code. |
| `FRONTEND.md` / `BACKEND.md` | docs | Describe the living code; iteration is the norm. |
| `GLOSSARY.md` | docs | Canonical naming is meaningful, but the glossary grows for the entire life of the project — it fails the stability test. |

When a new document appears, apply the same two tests: *would changing this
alter how the project is run?* and *do we expect it to change again soon?*
Only a yes to the first and a no to the second puts it in the constitution.
