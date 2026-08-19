---
title: adr-03-agent-contract
type: adr
status: active
created: 2026-08-18
version: v0.1.0
tags: [adr, agents, frontmatter, contract, rules]
paths:
  - "agents/*.md"
  - ".claude/agents/*.md"
  - "tests/harness/test_agent_definition_contract.py"
related_adrs:
  - "adr-00-adr-doctrine"
  - "adr-02-harness-layout"
related_agents:
  - "kbot-adr"
  - "kbot-auditor"
description: "Fixes the frontmatter contract of every agent definition: a closed key set, block-sequence tools, dispatch-matchable description, quick-exit statement, vendor-agnostic model inherit, and symmetric ADR-to-agent edges."
applies_when: "Authoring, editing, renaming, or validating any agent definition under agents/. Triggers: agent frontmatter, model inherit, quick exit, tools sequence, related_adrs."
---

# ADR-03 — agent definition contract

Rules only; agent registry and capability tables live in [[HARNESS]].

1. **Closed key set.** Every file under `agents/` declares exactly these frontmatter keys: `name`, `description`, `model`, `tools`, `version`, `related_adrs`. The key `color` is tolerated as cosmetic. Any other key is a defect.

2. **Name matches filename stem.** `name` must exactly match the filename stem (`kbot-<role>` or `kwf-<role>`).

3. **Canonical tools shape.** `tools` must be a YAML block sequence (one tool per line). Inline comma lists and flow lists (`[a, b]`) are forbidden. The empty list `tools: []` is forbidden because it is interpreted as unrestricted; an agent with minimal permissions declares the narrowest non-empty grant.

4. **Dispatch-matchable description.** `description` must be 25–60 words, declaring what the agent does, when to dispatch it, and at least one boundary it will not cross.

5. **Mandatory Quick Exit in body.** The agent definition body must explicitly declare a `Quick exit` condition under which it halts and returns when preconditions are unmet.

6. **Vendor-agnostic model.** `model` defaults to `inherit`. Vendor product names (e.g. proprietary model names) are forbidden in `name` and `description`.

7. **Symmetric bidirectional ADR edge.** `related_adrs` lists the ADR slugs whose force the agent carries. If `agent` lists `adr-NN`, then `adr-NN` must list `agent` in `related_agents`. One-sided edges are defects in both files.
