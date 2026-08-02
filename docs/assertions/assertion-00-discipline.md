---
title: Assertion-00 — Assertion Discipline
description: What an assertion is, how it is written, linked, and periodically verified
updated: 2026-08-02
---

## What an assertion is

A paragraph can define an assertion: something that must be accomplished. It
is a promise the project makes, written concretely enough to be checked.

> The user can get their last three messages, three clicks away from the home
> page, in a query, in less than 2 seconds.

That single paragraph states the rules: what (the last three messages), how
far (three clicks from home), how (one query), how fast (under 2 seconds).
An assertion that cannot be checked is not an assertion — it is a wish.

## Naming

```
assertion-NN-descriptive-slug.md
```

- `NN` is a two-digit, zero-padded number: `01`, `02`, …
- The slug is lowercase, hyphenated, no accents or special characters.
- `assertion-00` is reserved for this discipline.

## Format

The assertion paragraph comes first and states the rules. The file ends with
a `## RELATED` section: an open/close list, organized in `###` chapters,
linking everything that realizes or verifies the assertion — tests, source
files, docs, ADRs. Entries open and close as the project evolves; the list is
expected to churn even though the assertion itself stays put.

## Periodic review

A skill reviews every assertion periodically: each link under `## RELATED`
must resolve, and the promise itself must still hold. Assertions extend the
base frontmatter convention
([CONVENTION.md](../constitution/CONVENTION.md)) with a `verified` key — the
date of the last successful review, or `never`.

## Alignment

Assertions are always aligned with [PRD.md](../constitution/PRD.md) and the
constitution of this project. They are the constitution made verifiable: if
an assertion drifts from what the constitution says, the assertion is the one
that is wrong. The boundary with
[REQUIREMENTS.md](../constitution/REQUIREMENTS.md) is one of form:
requirements *enumerate* what must hold; an assertion takes one promise and
makes it *checkable* — concrete rules, linked evidence, periodic review.

## Template

Copy this block as the starting point for a new assertion.

```markdown
---
title: Assertion-NN — [Short name]
description: [The promise, in one line]
verified: never
updated: YYYY-MM-DD
---

[The assertion: one paragraph stating what must be accomplished, with every
rule it imposes — concrete enough to be checked.]

## RELATED

### Tests

- [link]

### Files

- [link]

### Docs

- [link]
```
