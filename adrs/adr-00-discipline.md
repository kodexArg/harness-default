---
title: ADR-00 — ADR Discipline
description: How ADRs are written, named, and maintained in this project
status: accepted
date: 2026-08-02
updated: 2026-08-02
---

## Why ADRs

An ADR (Architecture Decision Record) documents a decision with lasting impact
on the structure or direction of the project. The goal is that any future
agent or developer understands **why** the project reached its current state,
without reconstructing it from the commit history. ADRs are the memory of the
why, not just the what.

## When to write one

- A non-trivial dependency is chosen (and why that one and not another).
- A pattern is defined that every feature must follow.
- An alternative is discarded for reasons that are not obvious.
- A previous decision is changed (the new ADR references the one it supersedes).

Not every line of code needs an ADR — only decisions with impact on the
direction of the project.

## Naming

```
adr-NN-descriptive-slug.md
```

- `NN` is a two-digit, zero-padded number: `01`, `02`, …
- The slug is lowercase, hyphenated, no accents or special characters.
- `adr-00` is reserved for this discipline.

Examples: `adr-01-state-management.md`, `adr-02-http-client-strategy.md`

## Status lifecycle

ADRs extend the base frontmatter convention
([CONVENTION.md](../constitution/CONVENTION.md)): `status` uses the lifecycle
below, and the keys `date` (decision date), `supersedes`, and `superseded-by`
are available.

| Value | Meaning |
|---|---|
| `proposed` | Under discussion, not yet adopted |
| `accepted` | Decision made and in force |
| `deprecated` | Was valid, no longer applies |
| `superseded` | Replaced by another ADR (name it in `superseded-by`) |

Once accepted, an ADR is immutable: history is never rewritten — write a new
ADR that supersedes it.

## Template

Copy this block as the starting point for a new ADR.

```markdown
---
title: ADR-NN — [Decision title]
description: [One line — the decision, not the topic]
status: proposed
date: YYYY-MM-DD
updated: YYYY-MM-DD
---

## Context

What situation or problem led to this decision. Include the relevant
constraints (technical, ecosystem, project stage).

## Decision

What was decided, in one direct sentence. Then the detail.

## Alternatives considered

| Option | Why it was discarded |
|---|---|
| Alternative A | … |
| Alternative B | … |

## Consequences

What adopting this decision implies: what is gained, what is given up, what
to keep in mind going forward.

## References

- Links to issues, PRs, external docs, or related ADRs.
```
