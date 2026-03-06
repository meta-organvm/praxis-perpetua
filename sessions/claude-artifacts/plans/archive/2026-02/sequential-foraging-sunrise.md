# Plan: AI Tool Plan Hygiene + Shell/Kubernetes Fix

## Context

Two problems:
1. **Plan file chaos**: 216 plan files dumped flat in `~/.claude/plans/` with random names, no project association, no archiving. Plans get overwritten. Claude, Gemini, and Codex all need instructions to save plans per-project and archive instead of overwrite.
2. **Shell + Kubernetes broken**: `kind` binary is not installed. The kind-prd cluster is dead (no Docker containers, connection refused on port 63752). Shell config lacks kubernetes tooling (no completions, no kind aliases). User needs `exec zsh` to get a working environment.

---

## Part 1: Plan File Management (All AI Tools)

### 1A. Update Claude Code instructions (`~/.claude/CLAUDE.md`)

Add a `## Plan File Discipline` section with rules:
- Plans MUST be saved in the **project's** `.claude/plans/` directory (e.g., `~/Workspace/my-project/.claude/plans/`), NOT the global `~/.claude/plans/`
- When no project context exists (home dir, ad-hoc tasks), use `~/.claude/plans/` as fallback but with **date-prefixed names**: `YYYY-MM-DD-{descriptive-slug}.md`
- Plans are **never overwritten**. To revise, create a new file with incremented suffix: `YYYY-MM-DD-{slug}-v2.md`
- Agent sub-plans follow: `YYYY-MM-DD-{slug}-agent-{short-id}.md`

### 1B. Update Gemini instructions (`~/.gemini/GEMINI.md`)

Add equivalent plan discipline section. Gemini already organizes history by project in `~/.gemini/history/{project}/` — extend this pattern to plans.

### 1C. Create Codex global instructions (`~/AGENTS.md`)

File doesn't exist yet. Create it with:
- Same plan discipline rules adapted for Codex conventions
- Codex already archives sessions with timestamps in `~/.codex/archived_sessions/` — build on this pattern

### 1D. Archive existing 216 plan files

Write a Python script (`~/.claude/plans/archive-plans.py`) that:
1. Reads each `.md` file in `~/.claude/plans/`
2. Extracts project context from content (looks for project paths, repo names)
3. Moves files to `~/.claude/plans/archive/YYYY-MM/{original-filename}`
4. Produces a summary of what was archived

Files to modify:
- `/Users/4jp/.claude/CLAUDE.md` — add plan discipline section
- `/Users/4jp/.gemini/GEMINI.md` — add plan discipline section
- `/Users/4jp/AGENTS.md` — create new (Codex global instructions)
- `/Users/4jp/.claude/plans/archive-plans.py` — create new (cleanup script)

---

## Part 2: Shell + Kubernetes Fix

### 2A. Install kind via Homebrew

```
brew install kind
```

### 2B. Recreate the kind-prd cluster

```
kind create cluster --name prd
```

This will:
- Create Docker containers for the cluster
- Update kubeconfig at `~/.config/kube/config` (via KUBECONFIG env var)
- Make `kubectl` commands work against kind-prd

### 2C. Add kubernetes tooling to shell config

Edit `/Users/4jp/.config/zsh/20-tools.zsh` to add kubectl/kind completions and shell integration:

```zsh
# Kubernetes - kubectl completion
if command -v kubectl &>/dev/null; then
  _cache="${XDG_CACHE_HOME:-$HOME/.cache}/kubectl-zsh.zsh"
  if [[ ! -f "$_cache" ]] || [[ "$(command -v kubectl)" -nt "$_cache" ]]; then
    mkdir -p "${XDG_CACHE_HOME:-$HOME/.cache}"
    kubectl completion zsh > "$_cache" 2>/dev/null
  fi
  source "$_cache"
  unset _cache
fi
```

This follows the existing caching pattern used by starship, zoxide, fzf, atuin, direnv, and mise in that same file.

### 2D. Add kubernetes aliases

Edit `/Users/4jp/.config/zsh/30-aliases.zsh` to add a Kubernetes section:

```zsh
# Kubernetes
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgn='kubectl get nodes'
alias kctx='kubectl config get-contexts'
alias kns='kubectl config set-context --current --namespace'
```

### 2E. Clean up stale kubeconfig

The old `~/.kube/config` (default location) is stale — same cluster cert as the XDG one. After the new cluster is created:
- Verify `~/.config/kube/config` is updated with new cluster info
- Remove or rename `~/.kube/config` to prevent confusion (or symlink it)

Files to modify:
- `/Users/4jp/.config/zsh/20-tools.zsh` — add kubectl completion block
- `/Users/4jp/.config/zsh/30-aliases.zsh` — add kubernetes aliases section
- `/Users/4jp/.config/kube/config` — updated automatically by `kind create cluster`

---

## Verification

### Plan files
1. Confirm `~/.claude/plans/archive/` directory exists with archived files organized by month
2. Confirm CLAUDE.md, GEMINI.md, and AGENTS.md all contain plan discipline instructions
3. Verify `~/.claude/plans/` is clean (only archive dir + script remain)

### Shell + Kubernetes
1. `which kind` returns `/opt/homebrew/bin/kind`
2. `kind get clusters` shows `prd`
3. `kubectl get nodes` returns Ready nodes
4. `kubectl cluster-info --context kind-prd` connects successfully
5. Open a new terminal tab — verify kubernetes completions load without `exec zsh`
6. Run `chezmoi diff` to see what needs syncing back to dotfiles repo
