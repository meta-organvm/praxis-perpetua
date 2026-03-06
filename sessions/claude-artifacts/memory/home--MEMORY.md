# Memory

## World Root System
- `$WORLD_ROOT` = `~/world` — canonical ontology topology deployed 2026-02-08
- Env vars in `~/dotfiles/dot_zshenv` (managed by chezmoi)
- Registry: `$WORLD_ROOT/_registry/` — 12 policy docs, 4 JSON configs, 7 tools, 8 templates
- Audit runs: `$WORLD_ROOT/.audit/run_<ts>/`
- Generators: `_registry/tools/gen_manifests.sh` runs all 4 generators
- Phase 1 audit found 140 repos, 37 nesting violations, 19 duplicates, 139 need move
- ORG_I=ivviiviivvi, ORG_II=omni-dromenon-machina, ORG_III=labores-profani-crux
- ORG_IV-VII empty (names TBD), ORG_LIMINAL=4444j99, ORG_LIMINAL_ALT=4444jpp
- Phase 2-4 NOT yet executed. No repos moved. Source doc: `~/Workspace/Organizing-Local-Remote-Structure.md`

## Shell env gotcha
- `$HOME` expansion fails in Bash tool when vars set via `export VAR=...` in same command
- Use literal paths (`/Users/4jp/world`) instead of `$WORLD_ROOT` in Bash tool calls
- Or pass env vars inline: `WORLD_ROOT=/Users/4jp/world command`

## Chezmoi
- Dotfiles at `~/dotfiles/`, apply with `chezmoi apply --verbose --source-path <file>`
- `dot_zshenv` → `~/.zshenv`
