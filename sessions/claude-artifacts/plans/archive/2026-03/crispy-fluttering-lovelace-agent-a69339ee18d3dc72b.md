# ORGANVM-V Superproject Infrastructure Exploration

**Date**: 2026-02-27  
**Project**: organvm-v-logos (ORGAN-V: Public Discourse/Logos layer)  
**Status**: IN PROGRESS  
**Exploration Depth**: Complete infrastructure audit

## Objective
Perform a comprehensive exploration of the ORGANVM-V superproject to understand:
1. Superproject git structure and submodule commit status
2. GitHub Actions workflows (superproject root + all submodules)
3. Automation scripts (Makefiles, Justfiles, Taskfiles, shell scripts, cron jobs)
4. seed.yaml files and governance metadata
5. Configuration files governing automation behavior

## Known Structure (from .gitmodules)

**6 Submodules identified:**
- `.github` (infrastructure)
- `analytics-engine` (scaffold - no source code yet)
- `editorial-standards` (active - YAML/Markdown assets)
- `essay-pipeline` (active - Python validator/indexer)
- `public-process` (active - Jekyll static site flagship)
- `reading-observatory` (scaffold - no source code yet)

## Data Flow Architecture (from CLAUDE.md)
```
editorial-standards/schemas/ + public-process/_posts/
        ↓
   essay-pipeline (validator.py + indexer.py)
        ↓
   public-process/data/ (essays-index.json, cross-references.json, publication-calendar.json)
```

## Tasks Completed
✓ Read /Users/4jp/Workspace/organvm-v-logos/.gitmodules
✓ Read /Users/4jp/Workspace/organvm-v-logos/CLAUDE.md (project-level)
✓ Read /Users/4jp/Workspace/CLAUDE.md (workspace-level)
✓ Identified error: Bash tool does not accept `timeout_ms` parameter

## Tasks Remaining
- [ ] Retrieve git submodule status (correct Bash syntax)
- [ ] Search for GitHub Actions workflows in .github/workflows/ directories
- [ ] Locate all seed.yaml files across 6 submodules
- [ ] Find Makefiles, Justfiles, Taskfiles in superproject root and submodules
- [ ] Search for shell scripts and automation scripts
- [ ] Document configuration files (CI, cron, schedulers)
- [ ] Create comprehensive automation infrastructure report

## Search Strategy
1. Use Bash for: `git submodule status` (no timeout_ms parameter)
2. Use Glob for parallel pattern matching:
   - `**/.github/workflows/*.yml` (GitHub Actions)
   - `**/seed.yaml` (governance metadata)
   - `**/Makefile` (make scripts)
   - `**/Justfile` (just task runner)
   - `**/Taskfile` (taskfile runner)
   - `**/*.sh` (shell scripts - selective to avoid noise)
   - `**/.github/*.md` (community health files)
3. Use Read to examine key files discovered
4. Cross-reference with CLAUDE.md build commands

## Key Files to Examine
- Root: `.github/workflows/`, `Makefile`, setup scripts
- essay-pipeline: `src/validator.py`, `src/indexer.py`, `tests/`
- public-process: `_config.yml`, `Gemfile`, Jekyll configuration
- editorial-standards: `schemas/frontmatter-schema.yaml`, templates
- `.github/` submodule: community health files, org profile

## Findings Log
- **Submodule Count**: 6 (confirmed from .gitmodules)
- **Active Submodules**: 3 (essay-pipeline, editorial-standards, public-process)
- **Scaffold Submodules**: 2 (analytics-engine, reading-observatory)
- **Infrastructure**: 1 (.github)
- **Git URL Pattern**: `git@github.com:organvm-v-logos/{submodule-name}.git`

## Next Immediate Action
Run parallel Glob searches for:
1. Workflow files across all submodules
2. seed.yaml governance files
3. Automation scripts (Makefiles, shell scripts, etc.)
4. Configuration files (CI/CD, cron, schedulers)

Use Bash to get `git submodule status` for commit tracking.
