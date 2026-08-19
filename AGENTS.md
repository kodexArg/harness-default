---
title: AGENTS
type: index
status: active
created: 2026-08-18
version: v0.1.0
tags: [harness, index, multi-runtime]
---

# AGENTS.md — harness entry point

> [!danger] `docs/` MANDATORY-FIRST tool: the vault MCP, not Grep/Read
> Before touching **any** `docs/` prose or wikilink question — the very first tool call, ahead of Grep/Read, ahead of forming a plan — reach for the **`markdown-vault` MCP** (or `markdown-vault-docs`). It is the **mandatory first source of truth** for searching, reading, and traversing the vault graph (backlinks, outlinks, similarity); an agent that greps `docs/` before asking the vault is out of compliance. `search` to find, `read` to open, `get_backlinks`/`get_outlinks`/`get_similar` to traverse.
>
> **Where this does NOT apply:**
> - **Code, configs, and any non-`docs/` file** — Grep/Glob/Read is first there.
> - **The harness trees — `skills/`, `hooks/`, `agents/`, `adrs/`** — reached by path, never through the vault index; they live at the root and are excluded from the vault ([[adr-02-harness-layout]]).
> - **The reverse direction, doc/ADR → governed code** — `docs/CODEMAP.md`, the generated inverse index, not the vault graph.

This repository uses a generic, stack-agnostic agentic harness. This file is the single index you can trust across runtimes (Claude, Antigravity/Agy, Grok, Cursor): reach content through its links instead of re-scanning the repo.

> [!warning] The ABC — verify before adding ANYTHING
> 1. **Does it follow [[PRD]]?** (`docs/constitution/PRD.md`)
> 2. **Does it comply with the ADRs?** (`adrs/`)
> 3. **Does it modify [[API]]?** (`docs/API.md`)
>
> This is the ABC of every request, no matter how small. To make it possible, **[[PRD]] and [[API]] MUST be held in memory at all times**: the main session preloads both at session start, and a dispatched subagent reads both as its first act; either way they are re-read whenever they change.

## Authority & Architecture Hierarchy

Authority flows strictly top-down ([[adr-01-constitution]]):
1. `[[PRD]]` (`docs/constitution/PRD.md`): Ultimate objective and scope.
2. `docs/constitution/`: Governance and operational contracts.
3. `adrs/`: Architecture Decision Records stating numbered rules and triggers ([[adr-00-adr-doctrine]]).
4. `docs/`: Living documentation, APIs, and glossaries.
5. `code`: Implementation.

Where layers disagree, the higher layer wins. When code and an ADR disagree, the ADR is right and the code is the defect. Subagents never invent project law.

## The Development Loop

1. **Issue first:** Every non-trivial change enters via an issue.
2. **Isolated Worktree:** Changes develop on a separate branch/worktree (`kwf/<issue>-<slice>`), never directly on main.
3. **Proving Tests first (TDD):** For assertion-driven features and bug fixes, write failing tests before code ([[TDD]]).
4. **Guardian Dispatch Safety Net:** Run `python3 hooks/khook-guardian-dispatch --bundle` before closing a batch. Paste payload into owed guardians (`kbot-prd`, `kbot-adr`) in parallel on cheap tier.
5. **PR to Main:** Merge strictly via a verified Pull Request.

## Multi-Runtime Directory Layout

The repository maintains **one real copy** of every harness artifact at the root. Runtime-specific folders link to these root SSOTs:

- `adrs/` — Architecture Decision Records (canonical rules & triggers)
  - `.claude/rules -> ../adrs`
- `agents/` — Autonomous agent role definitions & souls (`agents/souls/`)
  - `.claude/agents -> ../agents`
  - `.agents/agents -> ../agents` (Cursor / Grok task discoverability)
- `hooks/` — Automation hooks attached to agent lifecycle events
  - `.claude/hooks -> ../hooks`
- `skills/` — Self-contained instruction packages
  - `.claude/skills -> ../skills`
  - `.grok/skills -> ../skills` (Grok skill discovery)

## Agent Roster

- **Guardians:**
  - `kbot-prd`: Gates product scope and constitution (`docs/constitution/PRD.md`, `docs/constitution/*.md`).
  - `kbot-adr`: Gates architectural rules and decisions (`adrs/adr-*.md`, `agents/*.md`).
- **Delivery Cast (`kwf-*`):**
  - `kwf-hunter`, `kwf-falcon`, `kwf-hound`: Forest phase — issue triage, duplicate checking, codebase recon.
  - `kwf-mage`, `kwf-sorcerer`, `kwf-mouse`: Tavern phase — task planning & ADR lookup.
  - `kwf-warrior`, `kwf-archer`, `kwf-dwarf`, `kwf-thief`, `kwf-elf-mage`, `kwf-paladin`: Camp phase — slice implementation.
  - `kwf-priest`, `kwf-shadow`: Stalking phase — secrets review & blind code review.
  - `kwf-bard`: Plaza phase — PR generation and issue reporting.
- **Orchestration Workers (`kbot-*`):**
  - `kbot-planner`, `kbot-builder`, `kbot-auditor`, `kbot-critic`, `kbot-janitor`, `kbot-changelog`, `kbot-document-this`, `kbot-evaluate`.

## Verification Gates

| Gate | Runner | Trigger | Blocks Merge? |
|---|---|---|---|
| Harness Suite (`python3 tests/harness/run_all.py`) | CI / Local | Every PR / commit touching harness | **Yes** |
| ADR Schema & Doctrine (`khook-check-adr.py`) | Hook / CI | Changes to `adrs/*.md` | **Yes** |
| API Conformance (`khook-check-api.py`) | Hook / CI | Changes declaring routes | **Yes** |
| Guardian Safety Net (`khook-guardian-dispatch`) | Hook / Operator | Pre-commit (warns), PR close | **Yes** (at PR close) |
| Live-Doc Sync (`python3 skills/k-live-doc/link.py --check`) | CI / Local | Changes to code / docs | **Yes** |
