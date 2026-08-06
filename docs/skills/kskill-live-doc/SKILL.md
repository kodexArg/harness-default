---
name: kskill-live-doc
description: Stamp and re-sync the live-doc block (wikilinks-only) on every code file in this template, linking each file to the ADRs and docs that govern it, and regenerate docs/CODEMAP.md. The stamped project name comes from the PROJECT_SLUG env var; the linker's fallback when unset is this template's reference slug. Use when adding or moving code, changing which ADR governs a file, or when a live-doc block is missing/stale. Ruled by adr-19-live-doc-backlinks.
---

> [!warning] Inherited law — remap before trusting
> This skill was ported from another clone of the harness. Where its body cites
> an ADR or a document, that citation names the **origin project's** law, not
> this one: only `adr-00`..`adr-04` exist here, and referenced docs may not.
> Those citations are placeholders — nothing outside `docs/adrs/` in this clone
> is in force ([[adr-01-constitution]]). On adoption, remap each one to this
> project's own ADR or delete it; do not treat a dangling wikilink as a rule
> ([[adr-02-harness]] rules 3 and 6).

# kskill-live-doc — code ↔ live-doc linker

Stamps a **live-doc block** ([[GLOSSARY]]) at the top of every code file the manifest
matches: a delimited `LIVE-DOC:START … LIVE-DOC:END` region, wrapped in the file's
native comment syntax, holding **wikilinks only** — the ADRs that govern the file, the
docs those ADRs own, and `[[API]]` for the route surface. Then regenerates
`docs/CODEMAP.md`, the generated doc→code inverse index. Force: [[adr-19-live-doc-backlinks]].

## Run it

```
python3 docs/skills/kskill-live-doc/link.py            # apply blocks + write CODEMAP.md
python3 docs/skills/kskill-live-doc/link.py --check    # report drift, exit 1 if any (no writes)
```

Idempotent: re-running re-syncs in place, never duplicates. Deterministic — no reasoning
per file, so any tier (haiku included) can run it.

## The manifest is the mapping

`manifest.json` owns **which links each file gets**, as `glob → links[]`. A file's block is
the ordered union of every matching rule. To change a file's governance, edit the manifest
and re-run — **never hand-edit a block** (that is drift; the next run reverts it). Links
starting `adr-` render under *Governed by*, `API` under *API*, everything else under *Docs*.

## Wrappers (same content, native comment per type)

| Type | Wrapper | Type | Wrapper |
|---|---|---|---|
| `.py` | module docstring `"""…"""` | `.svelte` | `<!-- … -->` |
| `.astro` | `/* … */` after the `---` fence | `.ts` / `.js` | `/* … */` |
| backend `.html` | `{# … #}` | `.yaml` / `compose` | `# …` |

`*.d.ts` is skipped (its `///` reference directive must stay line 1), as are `migrations/`,
`.venv/`, `node_modules/`, `.astro/`, and empty files.

## Rules it enforces

- Block carries **links, never prose** — no restatement of a doc ([[adr-19-live-doc-backlinks]] rule 2).
- `models/views/viewsets/serializers/urls/permissions` additionally cite `[[API]]` (rule 4).
- `CODEMAP.md` is **generated**, never hand-edited (rule 5).

Adding a new file type or root is a manifest edit; adding a rule ADR would own is a
supersession of [[adr-19-live-doc-backlinks]], not a change here.
