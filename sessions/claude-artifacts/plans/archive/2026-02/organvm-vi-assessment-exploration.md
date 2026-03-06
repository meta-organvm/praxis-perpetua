# ORGAN-VI Assessment Exploration Plan

## Goal
Comprehensively assess ORGAN-VI (organvm-vi-koinonia) state and identify the most impactful next development step.

## User's Four Explicit Exploration Areas

### 1. Promotion Criteria from meta-organvm
**Objective**: Understand the state machine progression from CANDIDATE → PUBLIC_PROCESS → GRADUATED

**Files to examine**:
- `/Users/4jp/Workspace/meta-organvm/governance-rules.json` - promotion criteria rules
- `/Users/4jp/Workspace/meta-organvm/validate-deps.py` - validation/dependency checking logic
- `/Users/4jp/Workspace/meta-organvm/` - omega criteria definitions
- `registry-v2.json` - promotion status tracking

**Key questions**:
- What are the explicit criteria for CANDIDATE → PUBLIC_PROCESS transition?
- What does GRADUATED require beyond PUBLIC_PROCESS?
- What omega criteria exist and how are they measured?

### 2. adaptive-personal-syllabus Gap Analysis
**Objective**: Determine why this repo is LOCAL status when others are CANDIDATE

**Files to examine**:
- `/Users/4jp/Workspace/organvm-vi-koinonia/adaptive-personal-syllabus/seed.yaml` - status declaration
- `/Users/4jp/Workspace/organvm-vi-koinonia/adaptive-personal-syllabus/` - repo structure and implementation completeness
- Comparison with other 4 repos that achieved CANDIDATE

**Key questions**:
- What specific gap(s) prevent CANDIDATE status?
- Is it missing CI/CD, tests, documentation, or functionality?
- What would be the minimal viable change for CANDIDATE promotion?

### 3. CI/CD State Audit
**Objective**: Verify GitHub Actions workflows exist and run for all 6 ORGAN-VI submodules

**Files to examine**:
- Each submodule's `.github/workflows/` directory
- Main superproject `.github/workflows/`
- `.gitmodules` to confirm all 6 repos

**Expected**:
- Workflow files for: salon-archive, reading-group-curriculum, adaptive-personal-syllabus, community-hub, koinonia-db, .github
- Confirmation that workflows are actively running

**Key questions**:
- Do all 6 have CI workflows?
- Are they passing?
- What's the test coverage status?

### 4. Cross-Organ Integration Readiness
**Objective**: Confirm ORGAN-VI is ready for ORGAN-IV orchestration consumption

**Files to examine**:
- `meta-organvm/organvm-corpvs-testamentvm/registry-v2.json` - ORGAN-VI entries and dependencies
- `meta-organvm/governance-rules.json` - inter-organ dependency rules
- ORGAN-VI `.github/` - integration declarations
- Each submodule's `seed.yaml` - produces/consumes edges

**Key questions**:
- Is ORGAN-VI properly registered in registry-v2.json?
- Are produces/consumes edges correctly declared?
- What events does ORGAN-VI subscribe to from ORGAN-IV?
- What is ORGAN-VI producing for downstream consumption?

## Execution Approach

### Phase 1: Foundation (meta-organvm governance)
1. Read governance-rules.json to understand promotion criteria
2. Examine validate-deps.py logic
3. Review registry-v2.json structure for ORGAN-VI entries

### Phase 2: ORGAN-VI State
1. Map all 6 submodule structures
2. Audit CI/CD workflows for each
3. Check seed.yaml files for status declarations

### Phase 3: Gap Analysis
1. Focus deep-dive on adaptive-personal-syllabus
2. Compare its state against CANDIDATE requirements
3. List specific blockers

### Phase 4: Integration Readiness
1. Verify registry entries are complete
2. Check produces/consumes declarations
3. Assess readiness for ORGAN-IV orchestration

## Deliverable
Comprehensive assessment report ordered by impact:
- **Critical blocker** (prevents any progress)
- **High impact** (required for next milestone)
- **Medium impact** (should address soon)
- **Low impact** (nice-to-have improvements)

## Current Blockers
- All initial exploration tool calls failed due to cascading sibling errors
- Plan mode is active (READ-ONLY); cannot execute changes

## Status
**PENDING** - Ready to execute once user confirms proceeding with exploration work (may require exiting plan mode)
