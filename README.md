---
title: harness-default
description: Generic, stack-agnostic, and vendor-neutral default harness for fullstack engineering projects
version: v0.1.0
updated: 2026-08-18
---

# harness-default

A generic, stack-agnostic, and brand-neutral agentic engineering harness template. It combines a structured constitution, Architecture Decision Records (ADRs) as binding rules, strict agent definition contracts, automated diagnostics, and an issue-to-PR delivery workflow.

## Core Pillars

1. **[PRD](docs/constitution/PRD.md):** The supreme objective at the top of the authority hierarchy.
2. **[ADRs](adrs/):** Architecture Decision Records as binding rules. Complying with active ADRs is a precondition for code changes ([ADR-00](adrs/adr-00-adr-doctrine.md)).
3. **[Agent Contracts](adrs/adr-03-agent-contract.md):** Rigid frontmatter contracts for autonomous agents (`kbot-*`, `kwf-*`) with closed key sets, `model: inherit`, and symmetric bidirectional edges.
4. **[Harness Layout](adrs/adr-02-harness-layout.md):** Root-level SSOT directories for `adrs/`, `agents/`, `hooks/`, and `skills/`, keeping `docs/` dedicated purely to human/agent knowledge without vault index collision.
5. **[Self-Validating Harness Suite](tests/harness/):** Built-in automated tests validating ADR schemas and agent symmetry out of the box.

---

## Directory Structure

```
.
├── adrs/                    # Architecture Decision Records (adr-00 through adr-NN)
├── agents/                  # Autonomous agent definitions (kbot-*, kwf-*)
├── hooks/                   # Automation & guard hooks (khook-repo-health, khook-load-adr-index, etc.)
├── skills/                  # Reusable skill playbooks (k-*)
├── docs/                    # Project knowledge SSOTs (PRD, ARCHITECTURE, GLOSSARY, TDD)
│   ├── constitution/        # Foundational contracts (PRD, HARNESS, CONVENTION)
│   └── assertions/          # Law family & proving test definitions
├── tests/
│   └── harness/             # Automated test suite for harness integrity
├── backend/ + frontend/     # Standard fullstack code-root pair
├── interfaces/ + services/  # Alternative microservices code-root pair
├── state/                   # Local database state & persistent volume fixtures
├── .claude/                 # Runtime symlinks pointing to root harness directories
└── LICENSE                  # MIT License
```

---

## Quick Start & Verification

Run the harness self-test suite:

```bash
python3 tests/harness/run_all.py
```

Run the session health diagnostic:

```bash
python3 hooks/khook-repo-health.py
```

Preload the active ADR trigger index:

```bash
python3 hooks/khook-load-adr-index.py
```

---

## License

[MIT](LICENSE) © 2026 kodexArg
