---
title: adr-01-constitution
type: adr
status: active
created: 2026-08-18
tags: [adr, constitution, hierarchy, authority]
paths:
  - "docs/PRD.md"
  - "docs/constitution/*.md"
  - "docs/*.md"
related_adrs:
  - "adr-00-adr-doctrine"
  - "adr-02-harness-layout"
related_agents:
  - "kbot-prd"
  - "kbot-adr"
description: "Establishes the supreme authority hierarchy: PRD at top, constitution tier second, ADRs third, and living documentation fourth. Forbids code or subagents from inventing project law."
applies_when: "Writing or amending PRD or constitution docs, settling authority disputes between markdown and code, deciding document placement in tiers."
---

# ADR-01 — constitution (source markdown & authority hierarchy)

Rules only; background context and prose live in [[HARNESS]].

1. **Authority hierarchy.** Authority flows strictly top-down:
   - `[[PRD]]`: The ultimate objective and product scope at the top.
   - `docs/constitution/`: How the project is governed and operated.
   - `adrs/`: Binding architecture and engineering decision rules.
   - `docs/`: Living documentation, specifications, APIs, and glossaries.
   - `code`: Implementation.
   Where layers disagree, the higher layer wins. Where an ADR and the code disagree, the ADR is right and the code is the defect.

2. **PRD is mandatory and concise.** `docs/constitution/PRD.md` states what the product is, whom it serves, and its boundaries. Granular technical behavior and assertion laws live with their respective living docs and are linked, never inlined into the PRD.

3. **Constitution tier stability.** Documents in `docs/constitution/` represent foundational project contracts. Modifying the constitution is an explicit event requiring owner authorization.

4. **No invented law.** Subagents, skills, and tools must not invent project law, bypass ADR assertions, or silently modify the product scope without owner approval.
