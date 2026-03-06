# ORGANVM System Exploration Plan
**Status**: Planning Phase | **Created**: 2026-02-24  
**Goal**: Identify high-impact work that would make the biggest difference toward the ORGANVM system running end-to-end

## Executive Summary
The user has requested a comprehensive exploration of the eight-organ ORGANVM system to understand:
1. What high-impact work connects to or builds upon ORGAN-VII (Kerygma - POSSE distribution pipeline)
2. What would make the biggest difference toward end-to-end system execution
3. What comprises the "most impactful next sprint"

**Key Investigation Areas**:
- Meta-organvm governance state and registry-v2.json (single source of truth for ~97 repos)
- ORGAN-IV orchestration tooling: registry.json and event system
- ORGAN-V (Logos) state and public-process essay site
- Cross-organ event flow and notify-kerygma.yml wiring
- seed.yaml audit: declared event subscriptions vs actual implementations
- Omega criteria files defining system completion state

## Task Breakdown

### Phase 1: File Discovery ✅ COMPLETED
**Objective**: Locate key registry, configuration, and seed files

**Completed**:
- Located `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`
- Located `/Users/4jp/Workspace/organvm-iv-taxis/orchestration-start-here/registry.json`
- Found 100+ seed.yaml files across all organs
- Identified seed.yaml files in ORGAN-VII:
  - `/Users/4jp/Workspace/organvm-vii-kerygma/.github/seed.yaml`
  - `/Users/4jp/Workspace/organvm-vii-kerygma/social-automation/seed.yaml`
  - `/Users/4jp/Workspace/organvm-vii-kerygma/distribution-strategy/seed.yaml`

**Issues**:
- No Omega*.md files found; need alternative search pattern

---

### Phase 2: Core Registry Analysis (TODO - READ-ONLY)
**Objective**: Understand the complete system topology and inter-organ dependencies

#### Task 2.1: Analyze registry-v2.json
- **File**: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`
- **Purpose**: Single source of truth for ~97 repos; understand which repos exist, their organ memberships, and their edges
- **Key Questions**:
  - Which repos feed into ORGAN-VII (Kerygma)?
  - Which repos does ORGAN-VII subscribe to?
  - What is the complete dependency graph?
  - Are there repos in LOCAL or CANDIDATE state that could be promoted?
  - What promotion state distribution exists (LOCAL/CANDIDATE/PUBLIC_PROCESS/GRADUATED/ARCHIVED)?
- **Expected Output**: Complete repo inventory with status and edge mapping

#### Task 2.2: Analyze ORGAN-IV registry.json
- **File**: `/Users/4jp/Workspace/organvm-iv-taxis/orchestration-start-here/registry.json`
- **Purpose**: Understand ORGAN-IV orchestration system and how it provides template variables to ORGAN-VII
- **Key Questions**:
  - What variables are available for template interpolation?
  - How does the event system work? (repository_dispatch trigger mechanism)
  - What repos does ORGAN-IV orchestrate?
  - Are there missing event subscriptions or configurations?
- **Expected Output**: ORGAN-IV orchestration model and available template variables

#### Task 2.3: Locate and Analyze Omega Criteria
- **Current Status**: No Omega*.md files found in initial glob search
- **Alternative Searches**:
  - Search for "Omega" or "omega" in governance files
  - Check meta-organvm/organvm-corpvs-testamentvm/ for any criteria documentation
  - Look in `governance-rules.json` or similar validation files
  - Check ORGAN-IV for completion criteria
- **Key Questions**:
  - What are the 17 completion criteria referenced in CLAUDE.md (8/17 met)?
  - What represents "system fully running end-to-end"?
  - What work items would move from 8/17 to 17/17?

---

### Phase 3: ORGAN-VII (Kerygma) Deep Dive (TODO - READ-ONLY)
**Objective**: Understand current ORGAN-VII wiring, dependencies, and event subscriptions

#### Task 3.1: Audit ORGAN-VII seed.yaml Files
**Files to Examine**:
- `/Users/4jp/Workspace/organvm-vii-kerygma/.github/seed.yaml`
- `/Users/4jp/Workspace/organvm-vii-kerygma/social-automation/seed.yaml`
- `/Users/4jp/Workspace/organvm-vii-kerygma/distribution-strategy/seed.yaml`
- `/Users/4jp/Workspace/organvm-vii-kerygma/announcement-templates/seed.yaml`

**Key Questions**:
- What event subscriptions are declared?
- What are the "produces" and "consumes" edges?
- Are subscriptions wired in actual .github/workflows files?
- Are there missing subscriptions compared to registry-v2.json declarations?
- What is the promotion state of each submodule? (Are any in LOCAL/CANDIDATE?)

**Expected Output**: Comprehensive audit of ORGAN-VII event wiring vs declared subscriptions

#### Task 3.2: Analyze ORGAN-VII Workflows
**File Location**: `/Users/4jp/Workspace/organvm-vii-kerygma/.github/.github/workflows/`

**Key Workflows**:
- `dispatch-receiver.yml` - How does ORGAN-IV trigger the pipeline?
- `rss-auto-dispatch.yml` - How does RSS polling work? From which feed?
- `notify-kerygma.yml` - Cross-organ notification handler implementation
- `ci-pipeline.yml` - Test coverage and validation

**Key Questions**:
- Is `notify-kerygma.yml` properly receiving cross-organ events?
- Are RSS polling credentials and feed URL configured?
- What is the failure/retry logic?
- Are there manual intervention steps or fully automated flow?

**Expected Output**: Workflow execution model and gap analysis

---

### Phase 4: ORGAN-V (Logos) & Event Source Analysis (TODO - READ-ONLY)
**Objective**: Understand the public-process essay site and how it feeds ORGAN-VII

#### Task 4.1: Examine ORGAN-V Structure
- **Location**: `/Users/4jp/Workspace/organvm-v-logos/`
- **Key Questions**:
  - What repo is the public-process essay site?
  - What is the Atom feed URL configured in ORGAN-VII?
  - Is the feed URL correct and accessible?
  - What format are essays in (Markdown, HTML, etc.)?
  - How frequently are essays published?

**Expected Output**: ORGAN-V event source configuration

#### Task 4.2: Event Flow Analysis
- **Path**: ORGAN-V public-process Atom feed → RSS poller (ORGAN-VII) → Template engine → POSSE dispatch
- **Key Questions**:
  - Is the poller running on schedule (every 6h per cron)?
  - Are there rate limits or backpressure handling?
  - What happens when ORGAN-V publishes faster than ORGAN-VII can dispatch?
  - Are there log files showing successful essay captures?

**Expected Output**: End-to-end event flow verification

---

### Phase 5: Cross-Organ Event Wiring Analysis (TODO - READ-ONLY)
**Objective**: Map the complete event flow between all organs

#### Task 5.1: Cross-Organ Dependencies
- **From registry-v2.json**: Extract all edges involving ORGAN-VII
- **Query Pattern**:
  - Which repos in ORGAN-II (Poiesis - generative art) produce events ORGAN-VII should consume?
  - Which repos in ORGAN-III (Ergon - products) produce release announcements?
  - Does ORGAN-IV emit orchestration events?
  - Does ORGAN-V emit essay publication events?
  - Which repos does ORGAN-VII produce to? (Analytics to ORGAN-IV? Feedback?)

**Expected Output**: Complete dependency graph showing event sources and sinks

#### Task 5.2: notify-kerygma.yml Deep Dive
- **File**: `/Users/4jp/Workspace/organvm-vii-kerygma/.github/.github/workflows/notify-kerygma.yml`
- **Purpose**: Understand cross-organ notification mechanism
- **Key Questions**:
  - What events trigger this workflow?
  - How does it route notifications to different organs?
  - What platform notifications are sent (Mastodon, Discord, Bluesky, Ghost)?
  - Are there any failures or missed notifications?

**Expected Output**: Cross-organ event routing model

---

### Phase 6: Impact Analysis & Synthesis (TODO - ANALYSIS)
**Objective**: Synthesize findings into actionable high-impact recommendations

#### Task 6.1: Gap Analysis
- **Input**: Results from Phases 2-5
- **Questions to Answer**:
  - What event subscriptions are declared but not implemented?
  - What repos are in LOCAL/CANDIDATE state that should be GRADUATED?
  - What orchestration variables are unused or missing?
  - What Omega criteria are blocking end-to-end execution?
  - Are there circular dependencies or missing wiring?

#### Task 6.2: Prioritization Matrix
- **Dimensions**: 
  - Impact: Would this change enable end-to-end execution?
  - Effort: How much work to implement?
  - Risk: Could this break existing functionality?
  - Dependencies: What must be done first?

#### Task 6.3: Recommended Sprint (Output)
- **Deliverable**: Rank-ordered list of high-impact work items
- **Format**:
  - High-Impact Item #1: [Description] | Effort: [estimate] | Enables: [which Omega criteria]
  - High-Impact Item #2: ...
  - ...
- **Criteria for "High-Impact"**:
  - Moves Omega completion from 8/17 to X/17
  - Enables previously-blocked end-to-end workflows
  - Fixes critical gaps in event wiring
  - Graduates repos from LOCAL/CANDIDATE to GRADUATED state

---

## Key Concepts Reference

**ORGANVM Eight-Organ Model**:
- ORGAN-I: Foundational theory, recursive engines, symbolic computing
- ORGAN-II: Generative art, performance systems, creative coding
- ORGAN-III: Commercial products, SaaS tools, developer utilities
- **ORGAN-IV: Orchestration, governance, AI agents, skills** ← Central orchestrator
- **ORGAN-V: Public discourse, essays, editorial, analytics** ← Content source
- ORGAN-VI: Community, reading groups, salons, learning
- **ORGAN-VII: POSSE distribution, social automation, announcements** ← Our focus
- META: Cross-organ engine, schemas, dashboard, governance corpus

**Promotion State Machine**:
```
LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED
                    (no back-edges allowed)
```

**Event-Driven Architecture**:
```
Event (RSS poll / GitHub dispatch)
  → Template Engine (kerygma_templates)
    → Quality Check (kerygma_templates.quality_checker)
      → POSSE Dispatch (kerygma_social.posse)
        → Analytics Recording (kerygma_strategy.analytics)
```

**Configuration Cascade**:
`YAML file → environment variables (KERYGMA_*) → effective config`

---

## Execution Notes (READ-ONLY Mode)

**Current Phase**: Plan mode - no file modifications or execution
**Allowed Operations**: 
- ✅ Read files (Bash cat, Read tool, Glob for discovery)
- ✅ Search content (Grep tool)
- ❌ Edit, create, or delete files (except this plan document)
- ❌ Execute pipeline commands or trigger workflows
- ✅ Create/update plan document at `/Users/4jp/.claude/plans/lucky-snuggling-mango-agent-a2bd39a09f728dade.md`

**File Locations for Analysis**:
- Registry files: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`
- Orchestration: `/Users/4jp/Workspace/organvm-iv-taxis/orchestration-start-here/registry.json`
- Seed files: Located via previous glob search (100+ files across all organs)
- ORGAN-VII workflows: `/Users/4jp/Workspace/organvm-vii-kerygma/.github/.github/workflows/`
- ORGAN-VII packages: social-automation, announcement-templates, distribution-strategy submodules

---

## Success Criteria

**Analysis Complete When**:
1. ✅ Registry-v2.json fully parsed: repo inventory and edge map established
2. ✅ ORGAN-IV orchestration understood: template variables and event system mapped
3. ✅ ORGAN-VII wiring audited: declared subscriptions vs implementation gaps identified
4. ✅ ORGAN-V event source verified: public-process feed accessible and polled correctly
5. ✅ Cross-organ flow mapped: complete event path from source to POSSE dispatch
6. ✅ Omega criteria identified: understanding what represents "end-to-end execution"
7. ✅ Gap analysis completed: prioritized list of high-impact work items
8. ✅ Recommendation delivered: "Most impactful next sprint" tasks rank-ordered

**Definition of "End-to-End Execution"**:
- All 8 organs producing events
- ORGAN-IV properly orchestrating
- ORGAN-VII consuming events from ORGAN-II, ORGAN-III, ORGAN-V
- Templates rendering correctly with interpolated variables
- POSSE dispatch succeeding to Mastodon, Discord, Bluesky, Ghost
- Analytics collecting delivery metrics
- Feedback flowing back to source organs
- System running on schedule without manual intervention

---

## Next Immediate Actions

1. **Read registry-v2.json** → understand complete repo topology
2. **Read ORGAN-IV registry.json** → understand orchestration model
3. **Audit ORGAN-VII seed.yaml files** → identify event subscription gaps
4. **Examine ORGAN-VII workflows** → verify actual wiring matches declarations
5. **Verify ORGAN-V event source** → confirm public-process feed is accessible
6. **Synthesize findings** → generate high-impact sprint recommendations

---

**End of Plan**
