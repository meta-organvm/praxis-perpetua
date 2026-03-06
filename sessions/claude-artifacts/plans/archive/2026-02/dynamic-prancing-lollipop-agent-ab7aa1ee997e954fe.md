# ORGANVM Workspace Maturity Assessment Plan

## Objective
Comprehensively assess the implementation maturity of the ORGANVM eight-organ system by analyzing code quality, project structure, and feature completeness across ~100 repositories.

## Scope
- **Organs I-V**: Repository code maturity, structure patterns, automation contracts
- **Meta-ORGANVM**: CLI functionality, test coverage, dashboard implementation
- **Output**: Prioritized maturity report guiding next development phases

## Phase 1: Organ Directory Assessment (Organs I-V)

### 1.1 Directory Structure Analysis
For each organ (`organvm-i-theoria`, `organvm-ii-poiesis`, `organvm-iii-ergon`, `organvm-iv-taxis`, `organvm-v-logos`):

1. List all subdirectories (individual repositories)
2. For each repo, check presence of:
   - `src/` or `lib/` directories (indicates code implementation)
   - `tests/` or `test/` directories (indicates test coverage)
   - `seed.yaml` file (indicates ORGANVM integration)
   - `README.md` (indicates documentation)
   - `setup.py` / `pyproject.toml` / `package.json` (indicates packaging)
3. Categorize as:
   - **Fully Implemented**: src + tests + seed.yaml
   - **Partially Implemented**: src + seed.yaml OR src + tests (missing one component)
   - **Skeleton**: seed.yaml only OR just git repo with minimal content
   - **Empty**: No seed.yaml, no src, no tests

### 1.2 Results Aggregation
Create summary table for each organ:
| Repo Name | Code | Tests | Seed.yaml | Category | Status |
|-----------|------|-------|-----------|----------|--------|

**Key Metrics**:
- % Fully Implemented
- % Partially Implemented
- % Skeleton/Empty
- Total repos per organ

### 1.3 Seed.yaml Pattern Analysis
For repos with `seed.yaml`:
- Extract `organ`, `tier`, `produces`, `consumes`, `status` fields
- Identify promotion pipeline progression (LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED)
- Flag any inconsistencies with registry-v2.json

---

## Phase 2: organvm-engine CLI & Feature Assessment

### 2.1 CLI Command Implementation Status
Test each command group:

**Registry Commands**:
- `organvm registry show <repo>` - actual vs stub
- `organvm registry list [--organ] [--status] [--tier] [--public]`
- `organvm registry validate`
- `organvm registry update <repo> <field> <value>`

**Governance Commands**:
- `organvm governance audit [--rules]`
- `organvm governance check-deps`
- `organvm governance promote <repo> <target-state>`
- `organvm governance impact <repo>`

**Seed Commands**:
- `organvm seed discover [--workspace]`
- `organvm seed validate`
- `organvm seed graph`

**Metrics Commands**:
- `organvm metrics calculate [--output]`
- `organvm metrics propagate [--cross-repo] [--dry-run]`
- `organvm metrics refresh [--cross-repo] [--dry-run]`

**Git Commands** (superproject management):
- `organvm git init-superproject --organ {I|II|III|IV|V|VI|VII|META}`
- `organvm git sync-organ --organ X [--message] [--dry-run]`
- `organvm git status [--organ X]`

**Context Commands**:
- `organvm context sync [--dry-run] [--organ X]`

### 2.2 Test Coverage Analysis
Check `organvm-engine/tests/`:
- Which test files exist (test_registry.py, test_governance.py, etc.)
- Which test functions pass/fail
- Coverage gaps vs declared features

### 2.3 Implementation Completeness
For each module in `organvm-engine/src/organvm_engine/`:
- `registry/` - loader, query, validator, updater
- `governance/` - state_machine, dependency_graph, audit, rules, impact
- `seed/` - discover, reader, graph
- `metrics/` - calculator, propagator, timeseries
- `git/` - superproject, status, reproduce
- `contextmd/` - generator, templates, sync

Mark as:
- ✅ Fully Implemented
- 🚧 Partial Implementation
- ⏸️ Stubbed/TODO
- ❌ Missing

---

## Phase 3: system-dashboard Assessment

### 3.1 Route Implementation Status
Check `system-dashboard/src/dashboard/`:
- `/health/` - health check endpoint
- `/registry/` - registry browser
- `/graph/` - dependency graph visualization
- `/soak/` - soak test monitoring
- `/essays/` - essay publication
- `/omega/` - omega scorecard

For each route:
- Does it render HTML or return placeholder?
- What data does it display?
- Are there template files (Jinja2 in `templates/`)?
- What endpoints does it call on organvm-engine?

### 3.2 Dashboard Functionality
- Can it start (`organvm-dashboard` or `uvicorn dashboard.app:app --reload`)?
- Do routes load without errors?
- What data sources does it display (registry, metrics, health)?
- What is placeholder vs real data?

### 3.3 Frontend Implementation
- Check `static/` directory for CSS/JS
- Identify HTMX integration points
- Check for missing dependencies or build steps

---

## Phase 4: Cross-System Integration Check

### 4.1 Dependency Graph Validation
- Verify schema-definitions is consumed by engine/dashboard
- Check alchemia-ingestvm integration with registry
- Verify organvm-mcp-server exposes all 13 tools

### 4.2 Data Flow Verification
- registry-v2.json availability and format
- governance-rules.json enforcement
- seed.yaml discovery completeness
- MCP server accessibility

---

## Deliverables

### Report Structure
1. **Executive Summary**
   - Overall maturity percentage by organ
   - Critical missing implementations
   - Top 5 gaps blocking full system operation

2. **Detailed Tables**
   - Organ I-V repo inventory with maturity categorization
   - organvm-engine command implementation matrix
   - system-dashboard route/feature completion

3. **Gap Analysis**
   - High-priority stubbed features
   - Missing test coverage
   - Seed.yaml adoption rate
   - Dashboard placeholder areas

4. **Recommendations**
   - Phase 1 priorities (highest-impact work)
   - Phase 2 optimization targets
   - Phase 3 stabilization candidates

### Success Criteria
- ✅ Repo count verified (21+32+29+8+7 = 97 repos in Organs I-V)
- ✅ Each repo categorized (Fully/Partial/Skeleton/Empty)
- ✅ All CLI commands tested (working vs stub)
- ✅ Dashboard routes assessed (implemented vs placeholder)
- ✅ Integration gaps identified
- ✅ Actionable priority list generated

---

## Execution Strategy

### Tools to Use
- **Bash** (find, ls): Directory exploration, file presence detection
- **Glob**: Pattern matching for src/, tests/, seed.yaml
- **Grep**: File content search (detecting stub implementations)
- **Read**: Inspect key files (seed.yaml, route definitions, test files)

### Order of Execution
1. Organ I-V assessment (parallelizable - one grep/glob per organ)
2. organvm-engine analysis (read source files, test files)
3. system-dashboard analysis (read app structure, templates)
4. Integration verification (cross-reference findings)
5. Synthesis into report

### Estimated Work
- Phase 1: ~50 file reads/searches (organs)
- Phase 2: ~20 file reads (engine analysis)
- Phase 3: ~10 file reads (dashboard analysis)
- Phase 4: 5-10 cross-references
- **Total**: ~100 read operations across ~1500 files

---

## Notes
- No execution occurs until user approval
- All findings will be READ-ONLY (no modifications)
- Plan prioritizes breadth (coverage) over depth (detailed code review)
- Focus is on "what exists and works" not "ideal implementation"
