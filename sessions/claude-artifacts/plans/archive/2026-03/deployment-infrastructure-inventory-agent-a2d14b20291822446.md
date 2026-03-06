# Deployment Infrastructure Inventory Search Plan

**Date**: 2026-02-28  
**Task**: Search all ORGANVM organs for deployment infrastructure files  
**Status**: PENDING (plan mode - no execution yet)

## Objective

Create a comprehensive inventory of deployment infrastructure files across all 8 ORGANVM organ directories, identifying which repos have deployment configuration and what platforms they target.

## Search Scope

**Organs to search**:
- organvm-i-theoria/
- organvm-ii-poiesis/
- organvm-iii-ergon/
- organvm-iv-taxis/
- organvm-v-logos/
- organvm-vi-koinonia/
- organvm-vii-kerygma/
- meta-organvm/

**Deployment file types** (10 patterns):
1. render.yaml, render.json
2. Dockerfile
3. docker-compose.yml, docker-compose.yaml
4. vercel.json
5. fly.toml
6. railway.json, railway.toml
7. DEPLOY.md, DEPLOY.txt
8. Procfile
9. .env, .env.example, .env.production
10. Chart.yaml (Helm), main.tf (Terraform)

**Exclusions**:
- node_modules/ directories
- .git/ directories
- life-my--midst--in (already deployed)
- commerce--meta (governance only)
- .github (infrastructure metadata only)

## Previous Attempt Analysis

**Error**: Initial parallel Glob search failed with timeout
- First call: `**/render.yaml` timed out after 20 seconds
- Cascade failure: Remaining 10 calls failed as sibling errors

**Root cause**: Workspace is too large (~100+ repos) for wildcard search across entire `/Users/4jp/Workspace/` hierarchy with 11 parallel Glob patterns

## Revised Strategy (Sequential, Organ-by-Organ)

### Phase 1: Organ-Level Searches (Sequential)
Instead of one massive parallel search, search each organ individually:

```bash
# For each organ directory, search for deployment files
# Use smaller, more targeted glob patterns:
- organvm-i-theoria: */render.yaml, */Dockerfile, */docker-compose.yml, */vercel.json, etc.
- organvm-ii-poiesis: */render.yaml, */Dockerfile, ...
- organvm-iii-ergon: */render.yaml, */Dockerfile, ... (handle submodules carefully)
- organvm-iv-taxis: */render.yaml, */Dockerfile, ...
- ... (rest of organs)
```

### Phase 2: Aggregate Results
Collect all findings into a structured inventory:
- Repo name
- Organ membership
- Deployment files present
- Deployment platform(s) inferred
- Tech stack (Node, Python, static, etc.)

### Phase 3: Generate Report
Output a markdown table summarizing:
- Which repos have deployment infrastructure
- What deployment targets are covered
- Gaps or missing configurations

## Expected Output Format

```markdown
# Deployment Infrastructure Inventory

## Summary
- Total repos with deployment config: X
- Repos without deployment config: Y
- Most common deployment platform: Z

## Detailed Inventory

| Repo | Organ | Platform(s) | Files | Tech Stack |
|------|-------|-------------|-------|-----------|
| repo-name | ORGAN-I | Render | render.yaml | Python |
| repo-name | ORGAN-III | Docker | Dockerfile, docker-compose.yml | Node.js |
| ... | ... | ... | ... | ... |

## Repos Without Deployment Config
- (list of repos that need deployment infrastructure)

## Notes
- Deployment file locations
- Platform-specific observations
```

## Risk Mitigation

**Timeout Risk**:
- ✓ Reduce scope per search (organ-by-organ instead of workspace-wide)
- ✓ Use sequential Glob calls instead of 11 parallel
- ✓ Consider fallback to bash `find` if Glob continues to timeout

**Submodule Complexity**:
- ✓ Remember ORGAN-III has 27 submodules + 1 standalone (peer-audited--behavioral-blockchain)
- ✓ Handle `.gitmodules` references correctly
- ✓ Account for repos not yet registered as submodules

**False Positives**:
- ✓ Filter out .env.example files that are templates, not active config
- ✓ Distinguish between sample DEPLOY.md docs vs actual deployment guides

## Execution Checklist (When Ready)

- [ ] Verify all 8 organ directories exist and are accessible
- [ ] Run Phase 1 searches (8 sequential Glob calls, one per organ)
- [ ] Aggregate results from all organs
- [ ] Generate formatted inventory table
- [ ] Document repos without deployment infrastructure
- [ ] Output final report to markdown file

## Notes

- This plan assumes execution will proceed only after user approval
- Searches will be read-only (no file modifications)
- Results will be compiled into a single summary document
- Special attention needed for ORGAN-III submodules and standalone repos
