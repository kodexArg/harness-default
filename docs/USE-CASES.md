---
title: Use Cases
description: The system's behavior as Gherkin scenarios — an open/close list, one case per chapter
version: v0.1.0
updated: 2026-08-02
---

A use case is one behavior of the system, and Gherkin is its required
language: every case is a `Given / When / Then` scenario, concrete enough to
walk through. Prose around a scenario may set context; the scenario is the
case.

This is an open/close file, not a folder: cases live as `##` chapters that
open and close as the product evolves, and the file churns for the life of
the project. A case is cited from anywhere as `UC-NN`; numbers are appended,
never reused, so a citation stays true even after its case closes. A case
the project promises to keep forever collapses into an assertion — the
scenario made one paragraph that must always hold
([[assertion-00-discipline]]) — and the assertion links back here from its
`RELATED`.

Stories in [[USER-STORIES]] reach their acceptance through this file: a
story names its cases in its `Realized by` line, and the story is accepted
when those cases pass.

The first case ships filled: the harness's canonical example, the same
scenario the README and the assertion discipline collapse into an assertion.
A cloned project opens its own behavior at `UC-02`, and closes `UC-01` the
day it stops being true of the product.

## UC-01 — Stored value displayed intact

```gherkin
Given a value X stored in the database
When the frontend displays X
Then the value shown equals the value stored
```
