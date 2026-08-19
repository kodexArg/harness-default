---
title: adr-02-harness-layout
type: adr
status: active
created: 2026-08-18
version: v0.1.0
tags: [adr, harness, layout, naming, skills, hooks, agents]
paths:
  - "skills/*"
  - "hooks/*"
  - "agents/*"
  - "adrs/*"
  - ".claude/*"
related_adrs:
  - "adr-00-adr-doctrine"
  - "adr-03-agent-contract"
related_agents:
  - "kbot-adr"
  - "kbot-janitor"
description: "Enforces the root-level layout for skills, hooks, agents, and ADRs with kind-prefixed naming. Forbids duplicated writable copies, stack-bound stems, vendor branding, and vault note index collision."
applies_when: "Adding, renaming, or relocating any skill, hook, agent, or ADR, or configuring runtime discovery and symlinks."
---

# ADR-02 — harness layout and kind-prefixed naming

Rules only; inventory and wiring details live in [[HARNESS]].

1. **Root-level single real copy.** Harness artifacts live at the repository root:
   - Skills in `skills/`
   - Hooks in `hooks/`
   - Agent definitions in `agents/`
   - ADRs in `adrs/`
   Every other path that reaches them (`.claude/skills`, `.claude/hooks`, `.claude/agents`, `.claude/rules`) is a symlink, never a duplicate writable copy.

2. **Every harness artifact carries a kind prefix.**
   - `k-` for skills (`skills/k-<role>/SKILL.md`)
   - `khook-` for automation hooks (`hooks/khook-<name>.py`)
   - `kbot-` for autonomous agents / guardians (`agents/kbot-<role>.md`)
   - `kwf-` for workflow party members (`agents/kwf-<role>.md`)

3. **Role stems, never stack or brand stems.** The stem after the prefix names the generic role, never a cloud vendor, proprietary brand, or project slug (`kbot-adr`, not `aws-adr`; `k-refactor`, not `django-refactor`).

4. **Vault separation.** `skills/`, `hooks/`, `agents/`, and `adrs/` sit at the repo root outside `docs/` to avoid note collision and keep `docs/` dedicated solely to project knowledge.
