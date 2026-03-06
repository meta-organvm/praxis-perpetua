# Fix LFS Budget Issues in organvm-i-theoria

## Context

Three ORGAN-I submodules (`.github`, `a-recursive-root`, `call-function--ontological`) fail to push because the org's GitHub LFS budget is exceeded. The root cause is the **global gitattributes** at `~/.config/git/attributes` (chezmoi-managed) which has `filter=lfs` rules on lines 53-93, forcing ALL repos system-wide to route images, archives, fonts, etc. through LFS — even trivially small files (68 bytes, 11 bytes, 643 bytes). The org is on the free GitHub plan (1GB LFS storage/bandwidth).

## Plan

### Phase 1: Fix global gitattributes

**File:** `~/.config/git/attributes` (chezmoi source: `~/domus-semper-palingenesis/dot_config/git/attributes`)

Replace the entire `filter=lfs` section (lines 50-93) with `binary` markers:
- `*.gif filter=lfs diff=lfs merge=lfs -text` → `*.gif binary` (and same for all other types)
- `*.svg` specifically becomes `text` (SVGs are XML, should be diffable)
- Add comment: "LFS tracking is intentionally NOT set globally. Repos needing LFS should declare it in their own .gitattributes."

Then: `chezmoi apply ~/.config/git/attributes`

### Phase 2: Remove LFS from 3 submodules (history rewrite + force push)

For each repo, run `git lfs migrate export` to convert LFS pointer files back to real content across all history, then force-push.

**2a. `a-recursive-root/`** (3 commits, 2 LFS files: 11B placeholder .zips)
```
git lfs migrate export --everything --include="*.zip"
git push --force-with-lease origin main
git lfs prune
```

**2b. `call-function--ontological/`** (51 commits, 1 LFS file: 643B .svg)
```
git lfs migrate export --everything --include="*.svg"
git stash drop stash@{2}  # all 3 stashes contain only SVG re-encoding
git stash drop stash@{1}
git stash drop stash@{0}
git push --force-with-lease origin main
git lfs prune
```

**2c. `.github/`** (shallow history, 3 LFS files: 60KB + 68B + 68B .pngs)
```
git lfs migrate export --everything --include="*.png"
git push --force-with-lease origin main
git lfs prune
```

### Phase 3: Update superproject pointers

```
cd /Users/4jp/Workspace/organvm-i-theoria
# Fetch rewritten histories and checkout new HEADs
cd .github && git fetch origin && git checkout origin/main && cd ..
cd a-recursive-root && git fetch origin && git checkout origin/main && cd ..
cd call-function--ontological && git fetch origin && git checkout origin/main && cd ..

# Commit updated pointers
git add .github a-recursive-root call-function--ontological
git commit -m "fix: update submodule pointers after LFS removal"
git push origin main
```

### Phase 4: Verify

- `git lfs ls-files` in each repo outputs nothing
- `grep "filter=lfs" ~/.config/git/attributes` outputs nothing
- `git push --dry-run origin main` succeeds in each repo
- Superproject `git status` is clean

## Critical Files

| File | Action |
|------|--------|
| `~/domus-semper-palingenesis/dot_config/git/attributes` | Edit: replace `filter=lfs` with `binary` |
| `~/.config/git/attributes` | Apply via chezmoi |
| `.github/.gitattributes` | No change needed (already uses `binary`) |
| `a-recursive-root/.gitattributes` | No change needed (already has `*.zip binary`) |

## Safety

- All 3 repos: sole collaborator, zero forks, single branch — force-push is safe
- Using `--force-with-lease` as additional safety net
- `binary` attribute is strictly less disruptive than `filter=lfs`
- `git lfs migrate export` is the standard tool for this operation

## Future: ORGAN-II/III cleanup

The global fix prevents new LFS contamination. ORGAN-II (113 LFS files across 5 repos) and ORGAN-III (67 files across 6 repos) may need the same `migrate export` treatment if their orgs also hit budget limits.
