---
title: Product Requirements Document
description: What this product is, who it serves, and what it must do
updated: 2026-08-02
---

[What the product is: a few sentences naming the product, the problem it
answers, and the shape of the answer — generalist, holistic, top-down. Every
line is a standing context cost; each fact lives with its owner, reached by
wikilink.]

## Who it serves

[The people this exists for — each actor in one line: who they are and what
they come here to do. The narratives behind them live in [[USER-STORIES]].]

## The horizon

[Where the product is going: the state that counts as done for the current
horizon, and the direction beyond it. A horizon, not a backlog.]

## What it must do

Watch the assertions first. A conventional PRD inlines its use cases and
user stories here; this harness keeps behavior with its owners:

- **`docs/assertions/`** — the promises. Every assertion that exists is
  binding and checkable; none existing is healthy
  ([[assertion-00-discipline]]).
- **[[USE-CASES]]** — the behavior, in Gherkin, an open/close list.
- **[[USER-STORIES]]** — who wants what and why, accepted through their
  cases.
- **[[REQUIREMENTS]]** — the functional and non-functional ground the
  implementation must satisfy.

This section is agnostic to any product: it ships final and stays as
written.

> [!note] This document is its own template
> Filling the brackets is among the first acts of a cloned project, together
> with picking the code-root pair ([[HARNESS]]); the brackets and this note
> leave together. `What it must do` stays as written. The keeper of this
> document is the PRD guardian, `docs/agents/guardian-prd.md`.
