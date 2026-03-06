# Plan: Clean Up Dirty Submodule State in organvm-ii-poiesis

## Context

The superproject has 31 submodules, all showing as dirty in `git status`. This accumulated from two batch operations that were never committed inside submodules:
1. A registry auto-sync pushed `CLAUDE.md`, `GEMINI.md`, `AGENTS.md` to every submodule
2. A pitch deck generator created `docs/pitch/index.html` in ~25 submodules

Additionally: 5 submodules have tracked `.DS_Store` files, a few repos have substantive dev work or loose personal files, and 16 submodules have pointer mismatches (HEAD moved past what superproject records).

**Goal:** Commit the intentional batch changes, handle special cases, update superproject pointers, push everything. End state: clean `git status` except MET4 (active dev work).

---

## Phase 1: Remove Tracked .DS_Store Files (5 submodules)

Global gitignore at `~/.config/git/ignore` already covers `.DS_Store`. These need `git rm --cached` to stop tracking.

```bash
cd /Users/4jp/Workspace/organvm-ii-poiesis
cd .github && git rm --cached .DS_Store && cd ..
cd academic-publication && git rm --cached .DS_Store && git rm --cached papers/.DS_Store && cd ..
cd artist-toolkit-and-templates && git rm --cached .DS_Store && cd ..
cd client-sdk && git rm --cached .DS_Store && cd ..
cd docs && git rm --cached .DS_Store assets/.DS_Store guides/.DS_Store research/.DS_Store specifications/.DS_Store theory/.DS_Store && cd ..
```

Don't commit yet — bundle with Phase 2.

## Phase 2: Batch Commit Context Files + Pitch Decks (all submodules)

Single `foreach` loop. Stages only explicit filenames to avoid capturing anything else.

```bash
git submodule foreach --quiet '
  for f in AGENTS.md CLAUDE.md GEMINI.md; do
    [ -f "$f" ] && git add "$f"
  done
  [ -d docs/pitch ] && git add docs/pitch/
  if ! git diff --cached --quiet; then
    git commit -m "chore: sync context files and pitch deck from registry"
  fi
'
```

This also picks up the `.DS_Store` removals staged in Phase 1. MET4 will be skipped (nothing to stage).

## Phase 3: Individual Substantive Repos

### 3a. core-engine — Architectural refactor
Deleted `dreamcatcher/` + `orchestrator/` dirs (11 files), modified `server.ts`, new `system-bus.ts`, `routes/`, `metasystem.ts`. Real dev work.

```bash
cd core-engine
git add -A  # all changes are intentional development work
git commit -m "refactor: replace dreamcatcher/orchestrator with system-bus architecture"
cd ..
```

### 3b. showcase-portfolio — Asset updates
15 modified files (binary assets, SVGs, index.ts). Content/design work.

```bash
cd showcase-portfolio
git add docs/source-materials/
git commit -m "chore: update portfolio source materials and assets"
cd ..
```

### 3c. artist-toolkit-and-templates — New template
Untracked `templates/profane-standards.yml`.

```bash
cd artist-toolkit-and-templates
git add templates/profane-standards.yml
git commit -m "feat: add profane-standards template"
cd ..
```

### 3d. MET4 — Active dev work (LEAVE ALONE)
3 modified files (`.serena/project.yml`, `layout.tsx`, `layout-transition.tsx`). Work-in-progress — do not commit as part of cleanup. MET4's pointer already matches superproject (no `+` prefix); it'll just show as `-dirty`.

### 3e. life-betterment-simulation — Personal intake files (GITIGNORE)
16 untracked personal documents (PDFs, docx, html). Repo has no `.gitignore`.

```bash
cd life-betterment-simulation
# Create targeted .gitignore
cat > .gitignore << 'EOF'
*.pdf
*.docx
*.txt
!README*.md
EOF
git add .gitignore
git commit -m "chore: add .gitignore for intake files"
cd ..
```

### 3f. shared-remembrance-gateway — Research material
Untracked concept doc (.md + .pdf). Repo has no `.gitignore`.

```bash
cd shared-remembrance-gateway
cat > .gitignore << 'EOF'
*.pdf
EOF
git add .gitignore "Metaverse Hub App Concept Exploration.md"
git commit -m "chore: add .gitignore and concept exploration doc"
cd ..
```

### 3g. universal-waveform-explorer — Research material + code
Untracked `SYNTHW4V3/` dir, PDFs, architecture docs. Repo has no `.gitignore`.

```bash
cd universal-waveform-explorer
cat > .gitignore << 'EOF'
*.pdf
EOF
git add .gitignore SYNTHW4V3/ aether-canvas-the-universal-waveform-explorer.md universal-system-architecture.md
git commit -m "chore: add .gitignore, project docs, and SYNTHW4V3 module"
cd ..
```

## Phase 4: Update Superproject Pointers + Push

### 4a. Stage all submodule pointer updates (except MET4)

```bash
cd /Users/4jp/Workspace/organvm-ii-poiesis
git add .github a-i-council--coliseum a-mavs-olevm academic-publication alchemical-synthesizer archive-past-works art-from--auto-revision-epistemic-engine art-from--narratological-algorithmic-lenses artist-toolkit-and-templates audio-synthesis-bridge case-studies-methodology chthon-oneiros client-sdk core-engine docs example-ai-collaboration example-choreographic-interface example-generative-music example-generative-visual example-interactive-installation example-theatre-dialogue ivi374ivi027-05 krypto-velamen learning-resources life-betterment-simulation metasystem-master performance-sdk shared-remembrance-gateway showcase-portfolio universal-waveform-explorer
git commit -m "chore: sync submodule pointers after context file sync and cleanup"
```

### 4b. Push all submodules then superproject

```bash
git submodule foreach '
  branch=$(git symbolic-ref --short HEAD)
  if [ "$(git log origin/$branch..$branch --oneline 2>/dev/null | wc -l)" -gt 0 ]; then
    git push origin $branch
  fi
'
git push origin main
```

## Expected End State

- `git status` shows only `m MET4` (3 unstaged dev files — intentional)
- `git submodule status` shows no `+` prefix (all pointers current)
- All 31 submodules have context files committed
- `.DS_Store` files untracked in 5 repos
- Personal/research files gitignored in 3 repos
- core-engine refactor committed
- showcase-portfolio assets committed
- profane-standards template committed

## Verification

```bash
git status                    # Should show only MET4 as modified
git submodule status          # No + prefixes
git submodule foreach --quiet 'git status --short | head -3'  # Only MET4 has output
```

## Branches

Two submodules use `master`: `a-mavs-olevm`, `metasystem-master`. All others use `main`. The push loop handles this via `git symbolic-ref`.

## Risk Notes

- Phase 2 loop ONLY stages `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `docs/pitch/` — no accidental captures
- core-engine `git add -A` is safe because all changes there are intentional dev work (verified via `git diff --stat`)
- MET4 is deliberately excluded from pointer update — its pointer is already correct, just has dirty working tree
- No seed.yaml files are touched
