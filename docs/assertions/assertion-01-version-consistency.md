---
title: Assertion-01 — Harness Markdown Version Consistency
description: Every markdown file in the harness carries a mandatory frontmatter 'version' matching CHANGELOG.md
version: v0.1.0
verified: 2026-08-18
updated: 2026-08-18
---

Every markdown document in the repository harness declares a mandatory `version` frontmatter field whose value strictly equals the latest release version declared in the root `CHANGELOG.md`. Automated harness test suites verify that every markdown document carries a valid YAML frontmatter block, contains the `version` field, and prevents any version drift across the entire project.

## RELATED

### Tests

- [tests/harness/test_version_consistency.py](../../tests/harness/test_version_consistency.py)

### Files

- [CHANGELOG.md](../../CHANGELOG.md)
- [docs/constitution/CONVENTION.md](../constitution/CONVENTION.md)

### Docs

- [docs/constitution/HARNESS.md](../constitution/HARNESS.md)
- [adrs/adr-00-adr-doctrine.md](../../adrs/adr-00-adr-doctrine.md)
- [adrs/adr-03-agent-contract.md](../../adrs/adr-03-agent-contract.md)
