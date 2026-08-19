---
title: User Stories
description: Who wants what and why — an open/close list, one story per chapter
version: v0.1.0
updated: 2026-08-02
---

A user story names a person and a want: *As a [role], I want [capability],
so that [value]*. The story owns the who and the why; the behavior that
delivers it is written in Gherkin in [[USE-CASES]]. Each story ends with a
`Realized by` line naming its cases, and the story is accepted when those
cases pass.

This is an open/close file: stories live as `##` chapters that open and
close as the product evolves. A story is cited from anywhere as `US-NN`;
numbers are appended, never reused, so a citation stays true even after its
story closes.

The first story ships filled: the harness's canonical example, realized by
the case of the same standing. A cloned project opens its own wants at
`US-02`.

## US-01 — Trust in stored data

As a user, I want the values I store shown back to me unchanged, so that I
can trust the product with my data.

Realized by: UC-01.
