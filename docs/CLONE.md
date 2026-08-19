---
title: Clone
description: First-run checklist after cloning harness-default — code roots, hooks, vault, skills, issue delivery
updated: 2026-08-18
---

Operator steps for a new project from this template. Order matters where
noted. Detail lives in [[HARNESS]] and [[adr-04-guardians-and-delivery]].

## 1. Pick a code-root pair

Keep one pair; delete the other:

- Classic webapp → keep `frontend/` + `backend/`; remove `interfaces/` +
  `services/`.
- Constellation → keep `interfaces/` + `services/`; remove `frontend/` +
  `backend/`.

Leave `state/`. Keep all four stack documents under `docs/`.

## 2. Wire the guardian safety net

```bash
ln -s ../../hooks/khook-pre-commit .git/hooks/pre-commit
```

Warns at commit when guardians are owed ([[adr-04-guardians-and-delivery]]). Does not
block; the owner process still must dispatch.

Claude Code's lifecycle hooks ship wired in `.claude/settings.json` (table in
[[HARNESS]]); `.claude/hooks -> ../hooks`, so there is no second copy.
Two things a clone must do itself:

- Fill the ADR-review nudge table in `hooks/khook-dispatch-guardians.py`
  as the project writes its own ADRs — it ships empty because a nudge may only
  name ADRs that exist here ([[adr-02-harness-layout]] rule 3).
- Declare endpoints in [[API]] before writing routes.

Link guardians (and the `kwf-*` cast) into the runtime that will use them —
one real copy under `agents/`:

```bash
# Claude Code (ships in template)
# .claude/agents -> ../agents

# Kimi: extra_agent_dirs includes <clone>/agents
# Cursor/Grok: no registry — playbook injects agents/kwf-*.md via Task
#   (see skills/k-triage-and-fix/references/runtimes.md)
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

Claude Code sees the whole tree already (`.claude/skills -> ../skills`).
Other runtimes: point their skill discovery at `skills/` — one real copy,
links everywhere else.

The law skills, always in force:

- `skills/k-assertion-review` — laws → tests → code ([[TDD]]).
- `skills/k-triage-and-fix` — GitHub issue → PR party.

The stack, docs, and orchestration skills ship too — inventory and grouping in
[[HARNESS]]. Two jobs per skill you evaluate:

1. **Configure** its specifics to this project's own tools and workflow values.
2. **Delete what this project does not use** — a clone that never needs
   reporting or specialized orchestration should remove those skills. Dead skills
   are noise in every discovery listing.

Do **not** add product assertions until the owner reserves compute for a law
([[assertion-00-discipline]]).

## 6. Issue delivery (triage-and-fix)

Cast and skill already ship in this clone ([[adr-04-guardians-and-delivery]]):

1. Confirm the runtime can see `agents/kwf-*.md` (Claude symlink, Kimi
   `extra_agent_dirs`, or Cursor/Grok prompt injection per `runtimes.md`).
2. Confirm skill `k-triage-and-fix` is on the runtime skill path.
3. Optional: vendor `skills/k-triage-and-fix/extras/gha-kwf-deps.yml` into
   `.github/workflows/` for human-side defer cascades.
4. After every plaza/bard publish, the owner process runs
   `hooks/khook-guardian-dispatch --bundle`, pastes the payload into each
   owed guardian (cheap tier, parallel), and runs
   `k-assertion-review` if `docs/assertions/` was touched.

## Done when

Code-root pair chosen, pre-commit linked, PRD brackets filled (or
explicitly deferred), skills discoverable, and — if using issue delivery —
cast discovery verified for the chosen runtime.
