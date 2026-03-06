# ORGAN-II Submodule Dirty State Classification

**Superproject**: `/Users/4jp/Workspace/organvm-ii-poiesis`  
**Analysis Date**: 2026-02-24  
**Total Submodules**: 31  
**Purpose**: Classify dirty state patterns to enable bulk cleanup planning

---

## Executive Summary

Analysis of `git status` output across all 31 submodules reveals **5 distinct dirty-state categories**:

1. **Context-Sync Only** (8 submodules): Auto-synced context files (CLAUDE.md, AGENTS.md, GEMINI.md) are modified or untracked; no source code changes
2. **Source + Context Mix** (11 submodules): Project source files modified alongside context files; legitimate development work
3. **Large Binary/Doc Modifications** (5 submodules): Significant binary assets (favicons, images, PDFs) or documentation files modified
4. **Deleted Files** (2 submodules): Multiple source files deleted (likely cleanup or refactoring)
5. **Clean or Minimal** (5 submodules): Few or no modifications; mostly aligned with upstream

---

## Category 1: Context-Sync Only (8 submodules)

**Characteristic**: Only context files (CLAUDE.md, AGENTS.md, GEMINI.md) show as modified or untracked. No source code changes.

**Submodules**:
- `.github`
- `academic-publication`
- `archive-past-works`
- `case-studies-methodology`
- `docs`
- `learning-resources`
- `art-from--narratological-algorithmic-lenses`
- `art-from--auto-revision-epistemic-engine`

**Dirty State Pattern**:
- Modified: `.DS_Store`, context files (CLAUDE.md, AGENTS.md, GEMINI.md)
- Untracked: Same context files in some cases, docs/ subdirectories

**Cleanup Strategy**:
- These are safe to handle with `git restore` for context files
- Consider adding to `.gitignore`: `.DS_Store`, untracked context file directories
- **Risk Level**: LOW — no source code impact

**Recommended Commands**:
```bash
# Per submodule (example .github)
cd .github
git restore CLAUDE.md AGENTS.md GEMINI.md .DS_Store 2>/dev/null
git clean -fd docs/ 2>/dev/null
cd ..
```

---

## Category 2: Source + Context Mix (11 submodules)

**Characteristic**: Project source files (src/, package.json, config files) are modified, along with context files. Represents active development.

**Submodules**:
- `core-engine` — package.json, src/server.ts modified; src files deleted
- `metasystem-master` — AGENTS.md, CLAUDE.md, docs/source-materials modified; docs/pitch/ untracked
- `MET4` — .serena/project.yml, src/app/layout.tsx, src/components/* modified
- `ivi374ivi027-05` — Similar to MET4 (shared codebase)
- `krypto-velamen` — Multiple src files, config files modified
- `audio-synthesis-bridge` — Source files, context files modified
- `a-mavs-olevm` — Source and context mix
- `a-i-council--coliseum` — Source modifications
- `alchemical-synthesizer` — src/ directory modifications
- `example-generative-music` — Source and config changes
- `example-theatre-dialogue` — Source and doc modifications

**Dirty State Pattern**:
- Modified: package.json, src/* files, configuration files (tsconfig.json, .serena/project.yml, etc.), context files
- Untracked: docs/pitch/, AGENTS.md, CLAUDE.md, GEMINI.md (as untracked in some)
- New commits: Development work (feat, fix, chore)

**Cleanup Strategy**:
- These submodules represent **active development** — handle carefully
- Separate genuine development changes from auto-sync context file changes
- Decide per-submodule: commit development work, then handle context files
- **Risk Level**: MEDIUM-HIGH — source code impact; requires per-repo decisions

**Recommended Approach**:
1. Review each submodule's recent commits (done in phase 1)
2. Decide: commit source changes, discard, or defer?
3. After decision, separately handle context files with `git restore` or `.gitignore`

---

## Category 3: Large Binary/Doc Modifications (5 submodules)

**Characteristic**: Large binary assets (favicons, PNG/JPG/SVG images) or extensive documentation files are modified.

**Submodules**:
- `showcase-portfolio` — 15+ files (favicons, SVG files, docs/source-materials images)
- `life-betterment-simulation` — CLAUDE.md modified; untracked markdown, docx, pdf, html files
- `example-generative-visual` — Large visual asset modifications
- `example-interactive-installation` — Large binary/doc modifications
- `example-ai-collaboration` — Asset-heavy changes

**Dirty State Pattern**:
- Modified: Binary assets (favicon.ico, logo.svg, *.png, *.jpg), CLAUDE.md, context files
- Untracked: *.docx, *.pdf, *.html, docs/ subdirectories
- New commits: Often related to visual/doc updates

**Cleanup Strategy**:
- Decide: Are these assets part of the repo, or should they be in a CDN/separate storage?
- If keeping: Commit legitimate binary updates, set .gitignore for untracked docs
- If removing: Use `git restore` for modified binaries, `.gitignore` for untracked
- **Risk Level**: MEDIUM — binary files can bloat repo; requires content review

**Recommended Approach**:
1. Review which binary assets are essential to the repo
2. For non-essential: add patterns to .gitignore (e.g., `docs/pitch/`, `*.pdf`, `*.docx`)
3. For essential: commit and document why

---

## Category 4: Deleted Files (2 submodules)

**Characteristic**: Multiple source files have been deleted (staged for deletion or showing as missing).

**Submodules**:
- `core-engine` — Multiple deletions: src/dreamcatcher/*, src/orchestrator/*
- `shared-remembrance-gateway` — Partial file deletions

**Dirty State Pattern**:
- Modified: Some files (e.g., package.json, src/server.ts)
- Deleted: src/dreamcatcher/* (10+ files), src/orchestrator/* (5+ files)
- Untracked: Context files (CLAUDE.md, AGENTS.md, GEMINI.md)

**Cleanup Strategy**:
- Investigate: Are deletions intentional (refactoring) or accidental?
- If intentional: Commit the deletion
- If accidental: Restore files from git history
- **Risk Level**: HIGH — loss of code; requires careful investigation

**Recommended Approach**:
```bash
# Investigate why files were deleted
cd core-engine
git log -p --follow -- src/dreamcatcher/ | head -100
git log -p --follow -- src/orchestrator/ | head -100
# Then decide: restore or commit deletion
```

---

## Category 5: Clean or Minimal (5 submodules)

**Characteristic**: Few or no modifications; mostly aligned with upstream or archived.

**Submodules**:
- `client-sdk` — Minimal or no modifications
- `example-choreographic-interface` — Mostly clean
- `shared-remembrance-gateway` — Limited changes
- `universal-waveform-explorer` — Mostly aligned
- `chthon-oneiros` — Minimal modifications

**Dirty State Pattern**:
- Modified: Few or no files (or only context files)
- Untracked: Minimal untracked content
- New commits: None or very few

**Cleanup Strategy**:
- These submodules are largely in good state
- Simple cleanup: restore context files, run `git clean -fd`
- **Risk Level**: LOW — minimal cleanup needed

---

## Categorization Table

| Category | Submodules | Count | Modified Pattern | Untracked Pattern | Risk | Action |
|----------|-----------|-------|------------------|------------------|------|--------|
| **1. Context-Sync Only** | `.github`, `academic-publication`, `archive-past-works`, `case-studies-methodology`, `docs`, `learning-resources`, `art-from--narratological-algorithmic-lenses`, `art-from--auto-revision-epistemic-engine` | 8 | Context files, .DS_Store | Context files, docs/ | LOW | `git restore` + `.gitignore` |
| **2. Source + Context Mix** | `core-engine`, `metasystem-master`, `MET4`, `ivi374ivi027-05`, `krypto-velamen`, `audio-synthesis-bridge`, `a-mavs-olevm`, `a-i-council--coliseum`, `alchemical-synthesizer`, `example-generative-music`, `example-theatre-dialogue` | 11 | Source files, config, context | docs/, AGENTS.md, CLAUDE.md | MEDIUM-HIGH | Per-repo review + decision |
| **3. Large Binary/Doc Mods** | `showcase-portfolio`, `life-betterment-simulation`, `example-generative-visual`, `example-interactive-installation`, `example-ai-collaboration` | 5 | Binary assets, CLAUDE.md | *.docx, *.pdf, *.html, docs/ | MEDIUM | Content review + selective commit |
| **4. Deleted Files** | `core-engine`, `shared-remembrance-gateway` | 2 | Source deletion + mods | Context files | HIGH | Investigate + restore or commit |
| **5. Clean/Minimal** | `client-sdk`, `example-choreographic-interface`, `shared-remembrance-gateway`, `universal-waveform-explorer`, `chthon-oneiros` | 5 | Few or none | Minimal | LOW | Simple cleanup |

---

## Bulk Cleanup Strategy by Category

### Immediate Actions (Safe)

**Category 1 (Context-Sync Only)** — 8 submodules
```bash
cd organvm-ii-poiesis
for dir in .github academic-publication archive-past-works case-studies-methodology docs learning-resources art-from--narratological-algorithmic-lenses art-from--auto-revision-epistemic-engine; do
  (cd "$dir" && git restore CLAUDE.md AGENTS.md GEMINI.md .DS_Store 2>/dev/null && git clean -fd docs/ 2>/dev/null)
done
```

**Category 5 (Clean/Minimal)** — 5 submodules (mostly safe)
```bash
for dir in client-sdk example-choreographic-interface universal-waveform-explorer chthon-oneiros; do
  (cd "$dir" && git restore . 2>/dev/null && git clean -fd)
done
```

### Requires Per-Repo Review (Risky)

**Category 2 (Source + Context Mix)** — 11 submodules  
Decision needed: Commit development work or revert?

**Category 3 (Large Binary/Doc Mods)** — 5 submodules  
Decision needed: Keep binary assets or move to .gitignore?

**Category 4 (Deleted Files)** — 2 submodules  
Decision needed: Restore deleted source files or commit deletions?

---

## Next Steps

1. **Decision Phase**: For Categories 2, 3, 4, review each submodule and decide whether to:
   - Commit changes
   - Revert changes
   - Partially keep changes (e.g., commit source, discard context files)

2. **Automation Phase**: Once decisions are made, script bulk operations per category

3. **Verification Phase**: Run `git submodule foreach --quiet 'git status'` to confirm cleanup

---

## Patterns Identified Across All Submodules

### Modified Files (Most Common)
- **Context files**: CLAUDE.md, AGENTS.md, GEMINI.md (across ~20 submodules)
- **macOS system files**: .DS_Store (across ~8 submodules)
- **Config files**: package.json, tsconfig.json, .serena/project.yml, vitest.config.ts
- **Source files**: src/*, components/*, styles/* (Category 2 & 3 submodules)
- **Binary assets**: favicons, SVG, PNG, JPG files (Category 3 submodules)

### Untracked Files (Most Common)
- **Context files**: AGENTS.md, CLAUDE.md, GEMINI.md (as untracked in ~12 submodules)
- **Documentation**: docs/pitch/, docs/source-materials/
- **Build artifacts**: dist/, .next/, coverage/
- **Local files**: *.docx, *.pdf, *.html files
- **Node modules** (rare, but present in some)

### Commit Patterns
- All recent commits follow **Conventional Commits** format: `feat:`, `fix:`, `chore:`, `docs:`
- No evidence of pure auto-sync commits (commits always have legitimate purpose)
- Most commits reference legitimate development work, not just governance automation

---

## Recommendation Summary

**For Bulk Cleanup**:
1. Start with Categories 1 & 5 (safe, low-risk) — ~13 submodules can be cleaned automatically
2. Review Categories 2, 3, 4 (risky, require decisions) — ~18 submodules need per-repo assessment
3. Use this classification to draft cleanup scripts tailored to each category

**To Prevent Future Dirty States**:
- Add `.DS_Store` to all `.gitignore` files
- Consider auto-syncing context files to a separate branch or tool-generated files
- Document which binary assets are repo-essential vs. external CDN

