---
title: Glossary
description: Canonical names for every domain concept — how we call each thing
updated: 2026-08-18
---

One name per concept, used everywhere — code, docs, conversation. The rows
below canonize the harness's own vocabulary; a cloned project grows the table
with its product's domain concepts.

| Term | Meaning |
|---|---|
| tier | A sorting container for written knowledge: `docs/constitution/` or the loose documents directly in `docs/`. A document sorts by one question — is it both meaningful and stable? |
| family | A numbered, append-only line of files that accumulates rather than sorts — ADRs, assertions — each ruled by its own `-00` discipline file. |
| constitution | The stable tier: foundational, binding documents read first and amended rarely. Changing it is an event. |
| ADR | Architecture Decision Record — the memory of the why. Attached to a theme, states numbered rules; presence in `adrs/` is what makes it binding ([[adr-00-adr-doctrine]]). First law: [[adr-01-constitution]]; layout: [[adr-02-harness-layout]]; contracts: [[adr-03-agent-contract]]. |
| assertion | Owner-reserved law: a Gherkin use case collapsed to one paragraph that a skill must pass via proving tests ([[TDD]], `k-assertion-review`). Completely optional and kept few; presence is what binds ([[assertion-00-discipline]]). |
| TDD | Test-first method for assertion-driven work: failing tests that encode the law, then the code that passes them — [[TDD]]. |
| triage-and-fix | In-tree issue→PR party — skill `skills/k-triage-and-fix/`, cast `agents/kwf-*`, phases forest→tavern→camp→stalking→plaza→post-bard ([[adr-04-guardians-and-delivery]]). |
| kwf-* | Delivery cast nodes (hunter, falcon, hound, mage, sorcerer, familiars, inquisitor, camp builders, priest, shadow, bard) — the one agent prefix that also means "party member with a phase" ([[adr-04-guardians-and-delivery]]). |
| k-* / khook-* / kbot-* | Harness naming: a skill under `skills/`, a hook under `hooks/`, an agent under `agents/` that is not a `kwf-*` party member. The prefix names the kind, the stem the role — never the stack ([[adr-02-harness-layout]]). |
| stage / phase | One segment of the triage-and-fix pipeline (forest, tavern, camp, stalking, plaza, post-bard). |
| guardian | An agent that gates the health of one document set — `kbot-prd` for the objective, `kbot-adr` for the rules. Reports to the owner process, never dispatches ([[adr-04-guardians-and-delivery]]). |
| owner | The human the project belongs to — the one source of policy-change authorization. |
| owner process | The main agent driving a session: it dispatches guardians and honors their `notify` lists. |
| vault | `docs/` served wikilink-aware by markdown-vault-mcp; root harness folders are excluded. Basenames are unique vault-wide ([[HARNESS]]). |
| code root | A top-level folder holding code or runtime state, outside the vault: `frontend/` + `backend/`, or `interfaces/` + `services/`, plus `state/`. |
| use case | One behavior of the system as a Gherkin scenario — `UC-NN`, an open/close chapter of [[USE-CASES]]. |
| user story | A person and a want — *As a, I want, so that* — `US-NN` in [[USER-STORIES]], accepted when its linked cases pass. |
| open/close list | A list whose chapters open and close as the project evolves — churn is the norm; presence is what makes an entry current. |

