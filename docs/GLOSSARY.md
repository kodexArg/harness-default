---
title: Glossary
description: Canonical names for every domain concept — how we call each thing
updated: 2026-08-02
---

One name per concept, used everywhere — code, docs, conversation. The rows
below canonize the harness's own vocabulary; a cloned project grows the table
with its product's domain concepts.

| Term | Meaning |
|---|---|
| tier | A sorting container for written knowledge: `docs/constitution/` or the loose documents directly in `docs/`. A document sorts by one question — is it both meaningful and stable? |
| family | A numbered, append-only line of files that accumulates rather than sorts — ADRs, assertions — each ruled by its own `-00` discipline file. |
| constitution | The stable tier: foundational, binding documents read first and amended rarely. Changing it is an event. |
| ADR | Architecture Decision Record — the memory of the why. Attached to a theme, states numbered rules; presence in `docs/adrs/` is what makes it binding ([[adr-00-discipline]]). |
| assertion | A Gherkin use case made one checkable paragraph — a promise the project keeps. Completely optional; presence is what binds ([[assertion-00-discipline]]). |
| guardian | An agent that gates the health of one document set — `guardian-prd` for the objective, `guardian-adr` for the rules. Reports to the owner process, never dispatches ([[adr-01-guardians]]). |
| owner | The human the project belongs to — the one source of policy-change authorization. |
| owner process | The main agent driving a session: it dispatches guardians and honors their `notify` lists. |
| vault | `docs/` served wikilink-aware by markdown-vault-mcp; the tooling folders are excluded. Basenames are unique vault-wide ([[HARNESS]]). |
| code root | A top-level folder holding code or runtime state, outside the vault: `frontend/` + `backend/`, or `interfaces/` + `services/`, plus `state/`. |
