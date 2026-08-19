---
title: adr-04-guardians-and-delivery
type: adr
status: active
created: 2026-08-18
version: v0.1.0
tags: [adr, guardians, delivery, git, triage, pr]
paths:
  - "hooks/khook-repo-health.py"
  - "hooks/khook-dispatch-guardians.py"
  - "hooks/khook-require-pr-flow.py"
  - "agents/kbot-prd.md"
  - "agents/kbot-adr.md"
  - "skills/k-triage-and-fix/*"
related_adrs:
  - "adr-00-adr-doctrine"
  - "adr-01-constitution"
related_agents:
  - "kbot-prd"
  - "kbot-adr"
  - "kwf-hunter"
  - "kwf-warrior"
description: "Defines the guardian gating architecture, repo-health checks, and the issue-to-PR delivery workflow. Forbids direct unreviewed merges to main, undocumented endpoints, and silent degradation of repository health."
applies_when: "Executing changes against PRD, ADRs, or harness tools, running issue delivery workflows, creating PRs, or checking merge readiness."
---

# ADR-04 — guardians and delivery workflow

Rules only; agent workflow details live in [[HARNESS]].

1. **Guardians gate written law.** `kbot-prd` and `kbot-adr` gate changes touching `docs/constitution/PRD.md`, `docs/constitution/`, `adrs/`, `agents/`, and `hooks/`.

2. **Session-start health check.** Repository integrity (symlinks, ADR frontmatters, agent contracts, clean git status) is validated by `khook-repo-health.py` at session start.

3. **Issue $\to$ Worktree $\to$ PR pipeline.** All non-trivial changes enter via an issue, develop on an isolated branch/worktree, and reach `main` exclusively through a verified pull request.

4. **Advisory review cast.** Code changes undergo automated multi-perspective review (`kbot-auditor`, `kbot-critic`, `kbot-janitor`) before merge.
