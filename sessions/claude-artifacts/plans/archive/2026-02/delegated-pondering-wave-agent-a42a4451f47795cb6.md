# Meta-ORGANVM Thorough Exploration & Assessment Plan

**Task**: Thoroughly explore MCP server and system-level documentation in `/Users/4jp/Workspace/meta-organvm/`

**Date**: 2026-02-23  
**Status**: PLAN MODE (read-only, no execution until approved)

---

## Exploration Objectives

### Primary Investigative Questions
1. **MCP Tool Implementation**: Are all 13 declared tools actually implemented, or do some raise `NotImplementedError`?
2. **Context File Consistency**: Are CLAUDE.md, AGENTS.md, GEMINI.md consistent across subprojects?
3. **Registry Quality**: Is registry-v2.json well-structured? Any obvious data quality issues?
4. **Schema Consistency**: Do seed.yaml files follow a consistent schema across subprojects?
5. **Configuration Integrity**: Are there orphaned, contradictory, or deprecated config files?

---

## Three Exploration Areas

### Area 1: organvm-mcp-server/ (Tool Implementation Assessment)

**Scope**: Complete source and test review

**Files to Read**:
- `src/organvm_mcp/server.py` - Entry point, server initialization
- `src/organvm_mcp/types.py` - Type definitions
- `src/organvm_mcp/data/*.py` - All data loader modules
- `src/organvm_mcp/tools/*.py` - All tool implementations (should be 13 total)
- `tests/*.py` - All test files
- `seed.yaml` - Repo automation contract
- `README.md` - Documentation
- `pyproject.toml` - Dependencies, metadata

**Assessment Criteria**:
- [ ] Count actual tool implementations vs. declared tools
- [ ] Flag any `raise NotImplementedError` or stub implementations
- [ ] Identify error handling patterns (try/except, validation, edge cases)
- [ ] Assess data loading patterns (file I/O, parsing, caching)
- [ ] Note any missing test coverage
- [ ] Check for type hint completeness

**Estimated Reads**: 15-20 files

---

### Area 2: organvm-corpvs-testamentvm/ (Registry & Governance)

**Scope**: Governance and registry structure review (NOT full 404K-word corpus)

**Files to Read**:
- `CLAUDE.md` (if exists) - Project-specific guidance
- `registry-v2.json` - First 100 lines + last 50 lines only
- `governance-rules.json` - Governance rules
- `scripts/` directory - List and skim validation/automation tooling
- `seed.yaml` - Repo automation contract

**Assessment Criteria**:
- [ ] Registry structure: How are repos catalogued? Any obvious gaps?
- [ ] Governance rules: What policies are enforced? Clarity of rules?
- [ ] Validation scripts: What schema/data validation exists?
- [ ] Seed.yaml alignment with system conventions

**Estimated Reads**: 5-8 files (partial reads of large files)

---

### Area 3: Cross-Cutting System Configuration & Context

**Scope**: Consistency assessment across all context and config files

**Files to Read**:
- `/Users/4jp/Workspace/meta-organvm/CLAUDE.md` - Workspace guidance
- `/Users/4jp/Workspace/meta-organvm/AGENTS.md` - AI agent instructions
- `/Users/4jp/Workspace/meta-organvm/GEMINI.md` - Gemini-specific instructions
- `/Users/4jp/Workspace/meta-organvm/.github/organ-aesthetic.yaml` - Visual identity
- `/Users/4jp/Workspace/meta-organvm/alchemia-ingestvm/taste.yaml` - Aesthetic cascade
- `seed.yaml` from 3+ subprojects:
  - `organvm-engine/seed.yaml`
  - `schema-definitions/seed.yaml`
  - `system-dashboard/seed.yaml`

**Assessment Criteria**:
- [ ] Are context files (CLAUDE.md, AGENTS.md, GEMINI.md) logically organized?
- [ ] Do they reference each other appropriately?
- [ ] Is organ-aesthetic.yaml complete? (Palette, typography, tone, layout patterns)
- [ ] Does taste.yaml cascade properly? (Aesthetic inheritance chain)
- [ ] Do seed.yaml files use consistent schema and field names?
- [ ] Are promotes/consumes/subscriptions edges coherent?
- [ ] Any orphaned or deprecated configurations?

**Estimated Reads**: 8-10 files

---

## Execution Phases

### Phase 1: File Discovery & Structure Mapping
- [ ] Re-examine directory structure of meta-organvm
- [ ] Confirm file existence for all planned reads
- [ ] Identify any additional context files not listed above

### Phase 2: MCP Server Deep Dive
- [ ] Read organvm-mcp-server source files systematically
- [ ] Count and document all tool implementations
- [ ] Flag implementation status (complete, partial, stub)
- [ ] Assess error handling and data patterns

### Phase 3: Registry & Governance Review
- [ ] Read registry-v2.json structure (head/tail)
- [ ] Read governance-rules.json and assess clarity
- [ ] Skim scripts/ for validation and automation logic
- [ ] Check seed.yaml format

### Phase 4: Cross-Cutting Configuration Audit
- [ ] Read all context files (CLAUDE.md, AGENTS.md, GEMINI.md)
- [ ] Read aesthetic and taste configurations
- [ ] Read seed.yaml from 3+ subprojects
- [ ] Compare schema consistency

### Phase 5: Synthesis & Reporting
- [ ] Generate comprehensive findings report
- [ ] List all tool implementation statuses
- [ ] Document configuration issues (if any)
- [ ] Provide recommendations

---

## Deliverables

Upon completion, provide:
1. **MCP Tool Inventory**: Count, names, status (working/stub/error-prone)
2. **Registry Assessment**: Structure analysis, data quality observations
3. **Configuration Audit Report**: Consistency findings, orphaned files
4. **Recommendations**: Any structural improvements or missing documentation

---

## Notes

- **Read-Only Mode**: No file edits or modifications during exploration
- **Large File Handling**: registry-v2.json and corpus files will be read partially only
- **Parallel Efficiency**: Multiple file reads will be executed in parallel where possible
- **Path Convention**: All file paths are absolute, starting from `/Users/4jp/Workspace/meta-organvm/`

