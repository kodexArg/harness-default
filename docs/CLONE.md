---
title: Clone
description: First-run checklist after cloning harness-default — code roots, hooks, vault, skills, triage-and-fix
updated: 2026-08-02
---

Operator steps for a new project from this template. Order matters where
noted. Detail lives in [[HARNESS]] and [[adr-04-issue-delivery]].

## 1. Pick a code-root pair

Keep one pair; delete the other:

- Classic webapp → keep `frontend/` + `backend/`; remove `interfaces/` +
  `services/`.
- Constellation → keep `interfaces/` + `services/`; remove `frontend/` +
  `backend/`.

Leave `state/`. Keep all four stack documents under `docs/`.

## 2. Wire the guardian safety net

```bash
ln -s ../../docs/hooks/pre-commit .git/hooks/pre-commit
```

Warns at commit when guardians are owed ([[adr-03-guardians]]). Does not
block; the owner process still must dispatch.

Link guardians (and the `kwf-*` cast) into the runtime that will use them —
one real copy under `docs/agents/`:

```bash
# Claude Code (ships in template)
# .claude/agents -> ../docs/agents

# Kimi: extra_agent_dirs includes <clone>/docs/agents
# Cursor/Grok: no registry — playbook injects docs/agents/kwf-*.md via Task
#   (see docs/skills/triage-and-fix/references/runtimes.md)
```

## 3. Vault (recommended)

```bash
uv tool install markdown-vault-mcp
```

Config ships in `.mcp.json`. Reindex after large doc batches.

## 4. Fill the constitution

- Replace brackets in [[PRD]] (then delete the template note).
- Fill [[REQUIREMENTS]] and [[INFRASTRUCTURE]] when known.
- Write the first product ADR when the first decision lands.

## 5. Skills

Wire both skills into the runtime's skill discovery (symlink or reference):

- `docs/skills/assertion-review` — laws → tests → code ([[TDD]]).
- `docs/skills/triage-and-fix` — GitHub issue → PR party.

Do **not** add product assertions until the owner reserves compute for a law
([[assertion-00-discipline]]).

## 6. Issue delivery (triage-and-fix)

Cast and skill already ship in this clone ([[adr-04-issue-delivery]]):

1. Confirm the runtime can see `docs/agents/kwf-*.md` (Claude symlink, Kimi
   `extra_agent_dirs`, or Cursor/Grok prompt injection per `runtimes.md`).
2. Confirm skill `triage-and-fix` is on the runtime skill path.
3. Optional: vendor `docs/skills/triage-and-fix/extras/gha-kwf-deps.yml` into
   `.github/workflows/` for human-side defer cascades.
4. After every plaza/bard publish, the owner process runs
   `docs/hooks/guardian-dispatch --bundle`, pastes the payload into each
   owed guardian (cheap tier, parallel), and runs
   `assertion-review` if `docs/assertions/` was touched.

## Done when

Code-root pair chosen, pre-commit linked, PRD brackets filled (or
explicitly deferred), skills discoverable, and — if using issue delivery —
cast discovery verified for the chosen runtime.
