---
title: TDD
description: Test-first workflow for assertion-driven work — tests demand the fix, then prove it forever
updated: 2026-08-02
---

This document is the working method the
[[assertion-00-discipline|assertion family]] and the
`kskill-assertion-review` skill share. When a law under `docs/assertions/` is
unmet, work proceeds here — not by coding first and hoping a test appears
later.

## Rule

**Tests first. Code second. The assertion stays.**

An assertion is a law. The tests linked from its `## RELATED` section are
how the project answers that law. The implementation is what makes those
tests pass. Order is not optional:

1. Interpret the assertion until every concrete rule is named (latency
   bound, click depth, query shape, equality of stored vs shown, …).
2. Write or demand the **failing** tests that encode those rules — one
   assertion may need more than one test; every rule the paragraph states
   must be covered.
3. Link those tests under the assertion's `### Tests` chapter before
   treating the batch as ready for implementation.
4. Implement the fix or feature until the tests pass.
5. Leave the tests in the tree. They are the permanent check that the law
   still holds — not a scaffold to delete after green.

## What counts as a proving test

A link under `### Tests` counts only if an agent (or CI) can run it and
the run **demonstrates** the assertion's rules. Examples:

- Backend latency ≤ 500ms → a performance or contract test that fails when
  the response exceeds 500ms.
- Stored value equals displayed value → a test that writes X, reads the
  display path, and asserts equality.

A README bullet, a manual checklist, or a comment in production code is
not a proving test. If the only evidence is prose, the assertion is unmet.

## When the skill invokes this document

The `kskill-assertion-review` skill loads this file whenever it finds an
assertion whose promise is not yet carried by runnable, linked tests — or
whose tests no longer match the law after an edit. It does not invent a
parallel process: it executes this one.

## Alignment

Assertions remain under [[assertion-00-discipline]] and [[PRD]]. TDD here
does not invent product scope; it only decides the order of work once the
owner has reserved compute for a law.
