# Plan: Clean all dirty submodules in organvm-iii-ergon

## Context

After syncing superproject pointers, `git status` still shows all 26 submodules as dirty because they have uncommitted changes **inside** them. The superproject sees submodule working trees with modifications and reports them as dirty.

Three categories of dirt identified across all submodules:

### Category 1: Auto-synced context files (ALL 26 submodules)
- `CLAUDE.md` — modified in ~18 submodules, untracked in ~8
- `AGENTS.md` — untracked or modified in all submodules
- `GEMINI.md` — untracked in all submodules

These come from the registry sync pipeline and should be committed.

### Category 2: `docs/pitch/` directories (~17 submodules)
Untracked pitch deck directories. Appear to be generated/placed by a pipeline.

### Category 3: Repo-specific files (varies)
| Submodule | Files | Action |
|-----------|-------|--------|
| `anon-hookup-now` | Binary assets (`.so`, `.webp`, `.png`, `.zip`) — 15+ files | Commit (build artifacts tracked in repo) |
| `select-or-left-or-right-or` | 15+ image files in `images/` | Commit |
| `sovereign-ecosystem--real-estate-luxury` | Debug screenshots (`.png`) | Commit |
| `enterprise-plugin` | Full plugin structure (agents/, commands/, hooks/, scripts/, etc.) | Commit |
| `gamified-coach-interface` | `.Jules/bolt.md`, `absorb-alchemize/`, `verification/terminal_open.png` | Commit |
| `life-my--midst--in` | `.serena/project.yml` | Commit |
| `card-trade-social` | 3 spec markdown files | Commit |
| `public-record-data-scrapper` | `.env.sandbox`, `apps/desktop/.vscode/` | Gitignore `.env.sandbox` and `.vscode/` (standard practice), commit rest |
| `mirror-mirror` | `absorb-alchemize/` | Commit |
| `classroom-rpg-aetheria` | `intake/classroom-rpg/` | Commit |
| `fetch-familiar-friends` | `_local/` | Commit |
| `my--father-mother` | `docs/` | Commit |
| `commerce--meta` | `docs/` | Commit |
| `universal-mail--automation` | `docs/` | Commit |

## Implementation

### Step 1: Bulk commit context files + docs/pitch in all submodules
Use `git submodule foreach` to add and commit `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, and `docs/pitch/` across all submodules in one pass:

```bash
git submodule foreach --quiet '
  git add CLAUDE.md AGENTS.md GEMINI.md docs/pitch/ 2>/dev/null;
  git diff --cached --quiet || git commit -m "chore: auto-sync context files (CLAUDE, GEMINI, AGENTS) and pitch docs"
'
```

### Step 2: Gitignore sensitive files in `public-record-data-scrapper`
Append `.env.sandbox` and `.vscode/` to its `.gitignore` (if not already present).

### Step 3: Commit remaining repo-specific files per-submodule
Use `git submodule foreach` to stage all remaining changes and commit:

```bash
git submodule foreach --quiet '
  git add -A 2>/dev/null;
  git diff --cached --quiet || git commit -m "chore: commit local working changes"
'
```

### Step 4: Sync superproject pointers
Back at the superproject root:
```bash
git add -A
git commit -m "chore: sync all submodule pointers after cleaning working trees"
git push origin main
```

### Step 5: Verify clean state
```bash
git status
git submodule foreach --quiet 'echo "=== $name ===" && git status --short'
```

## Verification
- `git status` at superproject root shows `nothing to commit, working tree clean`
- `git submodule foreach git status --short` shows no output (all clean)
- `git log --oneline -1` shows the sync commit
- Remote is up to date (`Your branch is up to date with 'origin/main'`)
