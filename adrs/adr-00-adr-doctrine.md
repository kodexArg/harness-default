---
title: adr-00-adr-doctrine
type: adr
status: active
created: 2026-08-18
tags: [adr, doctrine, harness, rules, frontmatter]
paths:
  - "adrs/adr-*.md"
  - ".claude/rules/adr-*.md"
  - "hooks/khook-check-adr.py"
  - "agents/kbot-adr.md"
  - "tests/harness/test_adr_schema.py"
related_adrs:
  - "adr-01-constitution"
  - "adr-02-harness-layout"
  - "adr-03-agent-contract"
related_agents:
  - "kbot-adr"
description: "Defines the architecture and lifecycle of Architecture Decision Records as harness rules: a rules-only body, structured frontmatter for trigger routing and for the bidirectional ADR-to-agent edge, and a strict supersession protocol for every semantic change."
applies_when: "Authoring, editing, superseding, or validating any ADR or rule in the repository harness. Triggers: adr frontmatter, adr format, new adr, supersession, related_agents, applies_when."
---

# ADR-00 — the ADR doctrine

Rules only; facts, tables, specs, and explanations live in `docs/` and are reached by wikilink.

1. **Rules only, never facts.** An ADR states rules, never informational background or volatile facts. Facts, tables, architecture specs, and domain concepts live in `docs/` and are reached by wikilink. If an ADR needs a fact, it links the document that owns it — it never inlines it.

2. **Root location and naming.** ADRs live in `adrs/` at the repository root. `.claude/rules/` links to `adrs/` so the agent runtime loads active ADRs as system rules. Naming convention: `adr-NN-slug.md` — sequential two-digit `NN`, kebab-case English slug (`adr-00` reserved for this doctrine).

3. **Frontmatter contract for harness triggers.** Every file under `adrs/` declares exactly this structured frontmatter:
   - `title`: exact filename slug without `.md` (`adr-NN-slug`).
   - `type`: always `adr`.
   - `status`: `active` or `defered`.
   - `created`: `YYYY-MM-DD`, the date first written; never changes.
   - `tags`: inline list for retrieval, lowercase, `adr` first.
   - `paths`: list of file globs governed by this rule (deterministic hook and subagent trigger).
   - `related_adrs`: list of related ADR slugs. Cross-ADR relationships are declared here rather than inlining ADR links in the rule body.
   - `related_agents`: list of agent names (`kbot-*`, `kwf-*`) that carry this rule's force — an agent that enforces, applies, or is bound by it in its own behavior. An ADR no agent carries declares the empty list `related_agents: []`; it never omits the key. This is one end of a **bidirectional** edge whose other end is the agent's own `related_adrs` ([[adr-03-agent-contract]]): the two sides must name each other, and a one-sided edge is a defect in both files.
   - `description`: 25–45 word declarative summary of what the rule enforces and forbids (for semantic triage and trigger routing).
   - `applies_when`: natural language context cues and intent triggers for planning.

4. **Supersession protocol.** Any change that alters, narrows, widens, or reverses the force of a rule — what it requires or forbids — is semantic and MUST supersede:
   - its full body moves to `docs/obsolete/defered-adr-NN-slug.md`;
   - the original keeps ONLY its frontmatter, set `status: defered`, body empty;
   - the replacement rule, if any, is written as a new ADR.
   A defered ADR contributes zero content to LLM context while preserving trigger index coherence. Never resurrect a body — write a new ADR.

5. **In-place edits.** In-place edition without supersession is permitted ONLY for:
   - (a) cosmetic, non-semantic changes — typos, formatting, wikilink repair, wording clarification that leaves what the rule requires or forbids unchanged;
   - (b) a change made under the owner's express consent given in the current conversation.
   Either path MUST NOT leave negated or historical content standing in the active assertions — the body always reads as current truth. Doubt about whether a change is semantic resolves to supersede.

6. **Compliance is a precondition.** Complying with every active ADR in `adrs/` is a mandatory precondition for adding or modifying code in this project.
