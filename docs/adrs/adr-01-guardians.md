---
title: adr-01-guardians
type: adr
category: harness
use_case: closing a batch of changes that touched PRD, the constitution, an ADR, docs/agents/, or docs/hooks/, defining or dispatching an agent, editing a guardian's watch list or the dispatch safety net, acting on a guardian verdict
created: 2026-08-02
modified: 2026-08-02
tags: [adr, harness, guardians, agents]
---

# ADR-01 — guardian agents

## CONTEXT

> Two guardians watch the health of this harness's law: `guardian-prd`
> guards the objective, `guardian-adr` guards the rules. This ADR is what
> makes their verdicts binding.

Rules only; what each guardian is — posture, watchlist, output shape — lives
in its definition under `docs/agents/`.

## ASSERTIONS

1. The two guardians — `guardian-prd` and `guardian-adr` — are the
   verification gate for their documents: [[PRD]] and the set of ADRs in
   force. One guardian per concern; adding a guardian appends a rule here.
2. SSOT for guardian definitions is `docs/agents/`. A runtime that discovers
   agents elsewhere (a `.claude/agents/` directory, an `extra_agent_dirs`
   entry) reaches them by link or reference — one real copy, links everywhere
   else.
3. Guardians are sought, not only triggered: an owner process that modifies a
   guardian's document or watched surface engages that guardian before the
   batch of changes closes. Automation that nudges the dispatch is a safety
   net for the case it forgot, and is equally binding.
4. Guardians report; they never dispatch. Sibling notification flows only
   through the owner process, which honors the returned `notify` list.
5. A guardian verdict of `violation` or `danger` blocks the change until
   resolved; `needs-new-adr` routes through the ADR lifecycle
   ([[adr-00-discipline]]), never through a local exception.
6. A guardian's output shape (`status` / `resolution` / `notify`) is fixed by
   its definition file.
7. Guardians triage before they sweep: a dispatch that touches nothing in the
   guardian's domain returns its passing verdict in one line, immediately —
   depth is spent only on plausible concerns.
8. Each guardian's watchlist has one machine copy: the `watch:` glob list in
   the frontmatter of its own definition, beside the prose that explains it.
   The dispatch safety net (`docs/hooks/guardian-dispatch`) reads only that
   key; a watched surface enters or leaves the watchlist by editing the
   guardian's file, nowhere else.

## RELATED

### governed paths

- `docs/agents/guardian-prd.md` — the PRD guardian
- `docs/agents/guardian-adr.md` — the ADR guardian
- `docs/hooks/guardian-dispatch` — the dispatch safety net (rules 3, 8)
- `docs/hooks/pre-commit` — the safety net's voice at commit time

### related files

- [[adr-00-discipline]] — the discipline both guardians enforce and obey
- [[PRD]] — the document the PRD guardian owns
- [[HARNESS]] — the agent-tooling tier these definitions live in
