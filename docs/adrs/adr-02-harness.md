---
title: adr-02-harness
type: adr
category: harness
use_case: adding or editing a skill hook or agent, wiring runtime discovery to docs/agents or docs/skills, changing guardian-dispatch or pre-commit, deciding whether tooling may invent law, closing a batch that touched agent tooling
created: 2026-08-02
modified: 2026-08-02
tags: [adr, harness, skills, hooks, agents]
---

# ADR-02 — harness tooling (skills, hooks, agents)

## CONTEXT

> The harness is the agent surface that serves the written law. Skills,
> hooks, and agents live under `docs/` beside that law — they do not replace
> it, invent it, or keep a second copy of it.

Rules only. What each tool does in detail lives in its own file; guardian
and delivery themes have their own ADRs.

## ASSERTIONS

1. **Tooling homes.** Skills live in `docs/skills/`, hooks in `docs/hooks/`,
   agent definitions in `docs/agents/`. These folders are part of the
   harness, excluded from the vault index (filename conventions would
   collide), and reached by path — not as vault notes.
2. **Law first.** Every skill, hook, and agent **obeys** [[adr-01-constitution]]
   and every ADR in force. Tooling may interpret and enforce the law; it
   must not silently redefine the objective, invent constitution policy, or
   invent product assertions. When tooling and law disagree, the law is
   right and the tooling is the defect.
3. **Explicit links.** Agent and skill bodies that act on written law name
   the governing documents by wikilink or path: [[PRD]], constitution files,
   the ADR set, [[TDD]], assertion files as relevant. A tool that gates a
   surface without pointing at its governing ADR or doc is incomplete.
4. **One real copy of agents.** SSOT for agent definitions is
   `docs/agents/`. Runtimes (`.claude/agents/`, Kimi `extra_agent_dirs`,
   Cursor/Grok prompt injection) link or reference that tree — they do not
   duplicate it ([[adr-03-guardians]] rule 2 for guardians; same rule for
   the `kwf-*` cast).
5. **Skills are playbooks.** A skill is an instruction package under
   `docs/skills/<name>/SKILL.md` (plus its local `references/`, `bin/`,
   tests). Wire each into the runtime's skill discovery. Standing residents:
   `assertion-review` (laws → tests → code) and `triage-and-fix` (issue →
   PR). Delivery mechanics: [[adr-04-issue-delivery]].
6. **Hooks are automation.** Hooks are LLM-agnostic scripts attached to
   agent or git lifecycle events. The dispatch safety net
   (`docs/hooks/guardian-dispatch`, voiced by `docs/hooks/pre-commit`)
   belongs here; its binding duty is [[adr-03-guardians]].
7. **Guardians are agents, not a separate tier.** `guardian-prd` and
   `guardian-adr` live under `docs/agents/` with the rest of the cast.
   Their verdicts and watchlists are governed by [[adr-03-guardians]].
8. **Souls are optional personality sidecars.** Voice/posture for an agent
   may live in `docs/agents/souls/<name>.md`, declared as `soul:` in the
   agent's frontmatter. Runtimes that do not load souls natively: the owner
   process prepends that file when dispatching. Soul never invents law;
   contracts and ADRs outrank voice. (Agent Skills have `SKILL.md`; souls
   are the parallel for agent personality — not a second SSOT for rules.)

## FORBIDDEN

- **NEVER** keep a second SSOT for agent definitions outside `docs/agents/`
  (rule 4).
- **NEVER** let a skill or agent stamp or invent product law without the
  owner and the proving path in [[adr-01-constitution]] rule 6 (rule 2).
- **NEVER** put durable project decisions only inside a skill prompt with
  no ADR (rule 2). Decisions belong in `docs/adrs/`.

## RELATED

### governed paths

- `docs/skills/` — skill packages
- `docs/hooks/` — lifecycle automation
- `docs/agents/` — agent definitions (guardians + `kwf-*`)
- `docs/agents/souls/` — personality sidecars (`soul:` frontmatter)
- `.claude/agents` — Claude Code link to `docs/agents/` (not a second copy)

### related files

- [[adr-01-constitution]] — the written law this tooling serves
- [[adr-03-guardians]] — guardian agents and dispatch safety net
- [[adr-04-issue-delivery]] — triage-and-fix skill and cast
- [[HARNESS]] — tooling section in prose
- [[CLONE]] — runtime wiring checklist
