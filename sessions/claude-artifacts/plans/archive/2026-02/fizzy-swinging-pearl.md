# Fix chezmoi after dotfiles repo rename

## Context

The dotfiles repo was renamed from `~/dotfiles` to `~/domus-semper-palingenesis` and the GitHub remote was updated to `[email redacted]:4444J99/domus-semper-palingenesis.git`. Chezmoi is broken because its config still points to the old path. Additionally, 34 files in the repo contain references to `~/dotfiles` that need selective updating.

## Step 1: Fix chezmoi config (critical fix)

**File**: `~/.config/chezmoi/chezmoi.toml`

Change line 1:
```
sourceDir = "~/dotfiles"  →  sourceDir = "~/domus-semper-palingenesis"
```

## Step 2: Update path references in repo files

Only update lines where `~/dotfiles` is used as a **literal filesystem path**. Leave generic/conceptual uses of "dotfiles" untouched.

### Shell aliases & abbreviations
- `dot_config/zsh/30-aliases.zsh:74-76` — `~/dotfiles` → `~/domus-semper-palingenesis` in cmcd, cmpush, cmlog aliases
- `dot_config/fish/config.fish.tmpl:220-222` — same for fish abbreviations

### Scripts & justfile
- `justfile:96` — `$EDITOR ~/dotfiles` → `$EDITOR ~/domus-semper-palingenesis`

### Documentation with executable paths
- `BACKUP_STRATEGY.md:7` — `cd ~/dotfiles && git push`
- `BOOTSTRAP.md:80` — `chezmoi init https://github.com/4444JPP/dotfiles.git` → `chezmoi init https://github.com/4444J99/domus-semper-palingenesis.git`
- `BOOTSTRAP.md:186` — comment about cmcd

### Templates
- `dot_config/ai-context/system-info.md.tmpl:6` — `at ~/dotfiles` → `at ~/domus-semper-palingenesis`

### Notes & manifests
- `private_Documents/Notes/System/AGENTS.md:15` — path to `~/dotfiles/docs/...`
- `dot_local/share/file-context/manifests/private_system-notes.yaml:17,70,82` — paths to `~/dotfiles/...`
- `dot_local/share/file-context/manifests/private_projects.yaml:7-9` — project name and GitHub URL `https://github.com/4444JPP/dotfiles`

### Organization docs
- `docs/ORGANIZATION_STRATEGY.md:226-228,273` — project paths referencing `~/Documents/dotfiles`
- `docs/ORGANIZATION_QUICKSTART.md:120-121` — project path referencing `~/Projects/Active/dotfiles`

## Step 3: Update global CLAUDE.md

**File**: `~/.claude/CLAUDE.md`

Change: `Managed by chezmoi at ~/dotfiles` → `Managed by chezmoi at ~/domus-semper-palingenesis`

## Files NOT modified (generic "dotfiles" concept usage)

These files use "dotfiles" as a general term, not a path — no changes needed:
- `DOTFILES_CLEANUP.md` — entirely about the concept
- `.chezmoiscripts/*.sh.tmpl` — comments and log messages
- `.shellcheckrc`, `.gitleaks.toml` — config comments
- `README.md`, `1PASSWORD_SETUP.md`, `PLUGINS.md` — documentation prose
- `docs/DOMUS_CLI.md`, `docs/TROUBLESHOOTING.md`, `docs/system-guides/INIT.md` — docs
- `dot_config/git/hooks/executable_post-*` — log messages about "dotfiles source"
- `dot_config/navi/cheats/personal.cheat` — tags
- `dot_config/zsh/completions/_domus` — descriptions
- `dot_local/bin/executable_domus*` — function names, log messages, feature descriptions
- `tests/test-domus-cli.bats` — test checking for "dotfiles" in output (conceptual)

## Verification

1. Run `chezmoi doctor` — confirm `source-dir`, `working-tree`, and `hardlink` all pass
2. Run `chezmoi diff` — confirm chezmoi can read the source and show pending changes
3. Run `chezmoi apply --dry-run` — confirm the updated aliases/templates would deploy correctly
