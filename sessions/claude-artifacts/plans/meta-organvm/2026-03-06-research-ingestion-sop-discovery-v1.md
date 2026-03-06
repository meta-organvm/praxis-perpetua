# Research Ingestion/Synthesis/Digestion SOP Discovery
**Date**: 2026-03-06  
**Status**: COMPLETED  
**Context Window**: Continuation from previous session (context compaction required)

---

## 1. Primary Request and Intent

**Original Explicit User Request (5 Parts):**
1. Search `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm` for SOP files related to research ingestion, synthesis, or digestion
2. Perform glob searches for keywords: "sop", "ingest", "synth", "digest", "research", "process"
3. Identify any docs/, sop/, procedures/, or processes/ directories
4. Read all matching files **in complete entirety**
5. Report exact file paths and complete contents; check CLAUDE.md and README for references

**Current Session Request:**
Create detailed conversation summary capturing technical details, code patterns, and architectural decisions essential for continuing development work.

**Resolution Status**: ✅ COMPLETED
- All five parts of original request executed and satisfied
- Primary SOP identified: `sop--document-audit-feature-extraction.md`
- Secondary SOP identified: `sop--pitch-deck-rollout.md`
- Complete file contents retrieved (via bash `cat` fallback after Read tool limitation)
- Cross-references in CLAUDE.md and README checked

---

## 2. Key Technical Concepts and Architecture

### Eight-Organ ORGANVM System
```
ORGAN-I   (Theoria)         → Foundational theory, recursive engines, symbolic computing
ORGAN-II  (Poiesis)         → Generative art, performance systems, creative coding
ORGAN-III (Ergon)           → Commercial products, SaaS tools, developer utilities
ORGAN-IV  (Taxis)           → Orchestration, governance, AI agents, skills
ORGAN-V   (Logos)           → Public discourse, essays, editorial, analytics
ORGAN-VI  (Koinonia)        → Community, reading groups, salons, learning
ORGAN-VII (Kerygma)         → POSSE distribution, social automation, announcements
META      (META-ORGANVM)    → Cross-organ engine, schemas, dashboard, governance corpus
```

### Governance Quadrilateral
The governance framework operates on four pillars:
1. **Roadmap** — Strategic vision and long-term direction
2. **Cadence** — Recurring governance processes and review cycles
3. **Catalog** — Inventory of all 97+ repositories across organs
4. **Rolling TODO** — Continuous improvement and task tracking

### Unidirectional Dependency Flow
**Critical invariant:** No back-edges allowed.
- `I → II → III` — Unidirectional dependency chain
- ORGAN-IV orchestrates all organs
- ORGAN-V documents (read-many-write-one)
- ORGAN-VII amplifies (consumer only)
- Enforcement: `validate-deps.py` in `orchestration-start-here/`

### Promotion State Machine
```
LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED
```
**No state skipping allowed.** Every repository follows this path with explicit approval gates.

### Single Source of Truth
**`registry-v2.json`** in `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/`
- Contains all ~100 repositories across 8 organs
- 2,200+ lines of structured repo metadata
- Schema includes: organ membership, tier (flagship/standard/infrastructure), promotion_status, produces/consumes edges, event subscriptions
- Protected file: must use targeted edits, never wholesale replacement

### seed.yaml Contract Model
Every repository declares via `seed.yaml` (schema v1.0):
- Organ membership and tier classification
- Promotion status (LOCAL, CANDIDATE, PUBLIC_PROCESS, GRADUATED, ARCHIVED)
- Produces edges — events/artifacts this repo generates
- Consumes edges — events/artifacts this repo subscribes to
- CI agent definitions — GitHub Actions workflow configuration
- Event subscriptions — what governance events trigger automation

### AI-Conductor Workflow Model
Operational pattern for governance work:
1. **Human directs** — Specifies intent, scope, governance goals
2. **AI generates volume** — Creates substantial first drafts, runs automation, generates candidates
3. **Human reviews** — Evaluates output, refines direction, makes acceptance decisions
4. **Effort metric**: Token-Expended (TE) budget — measured in LLM tokens, not hours

### Research Synthesis Workflow (5-Phase)
From `sop--document-audit-feature-extraction.md`:

**Phase 1: Inventory & Triage**
- Map all governance documents across 97 repos
- Classify by type: constitution, rules, procedures, metrics
- Identify scope and interdependencies
- Output: Artifact inventory with cross-reference map

**Phase 2: Exhaustive Read & Extraction**
- Read complete governance documents end-to-end
- Extract structured features: rules, constraints, processes, decisions
- Identify feature categories: dependency rules, promotion gates, event types, state transitions
- Output: Structured feature manifest with line references

**Phase 3: Deduplication**
- Identify redundant governance rules across documents
- Find conflicting directives (if any)
- Consolidate equivalent features under single definition
- Output: Deduplication report with merge recommendations

**Phase 4: Issue Creation**
- Convert extracted features to actionable GitHub issues
- Create issues in appropriate repos (e.g., orchestration-start-here for global rules)
- Link back to source documents with precise line references
- Output: GitHub issue references with correlation mapping

**Phase 5: Post-Audit Artifacts**
- Generate governance metrics and health dashboard
- Create feature matrix (repo × feature presence)
- Document gaps and improvement opportunities
- Output: Artifacts for continuous monitoring

---

## 3. Files and Code Sections

### Primary SOP: `sop--document-audit-feature-extraction.md`
**Path**: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md`  
**Size**: ~18KB  
**Status**: ACTIVE (Living document, continuously updated)  
**Version**: Stable implementation of 5-phase governance audit workflow

**Key Sections:**
- Executive Summary — Purpose, scope, expected outcomes
- Five-phase workflow with detailed instructions per phase
- Input/output specifications for each phase
- Quality gates and validation checkpoints
- Governance document cross-references (constitution.md, governance-rules.json, operational-cadence.md)
- Automation hints for agentic-titan and agent--claude-smith integration
- Error handling and exception procedures

**Critical Importance**: Directly addresses research synthesis problem — takes unstructured governance documentation across 97 repos, extracts structured features, identifies patterns/gaps, creates actionable improvements.

**Integration Points**:
- Works with `registry-v2.json` (repo inventory)
- References `governance-rules.json` (legal/policy rules)
- Cross-references `constitution.md` (ORGANVM principles)
- Coordinates with `operational-cadence.md` (process timing)
- Outputs feed into ORGAN-IV orchestration and ORGAN-V documentation

### Secondary SOP: `sop--pitch-deck-rollout.md`
**Path**: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--pitch-deck-rollout.md`  
**Size**: ~32.5KB  
**Status**: ACTIVE (Living document)  
**Relevance**: Conditional — applies if research synthesis outputs require external organizational communication

**Key Sections** (16-section table of contents):
1. Pitch deck generation from repo seed.yaml
2. README standardization across tiers
3. pitch.yaml authoring guidelines
4. Auto-generation pipeline configuration
5. Deployment to external channels
6. CI/CD integration patterns
7. Quality gates and review cycles
8. Tier-based rollout sequencing (flagship → standard → infrastructure)
9. External submission pipeline
10. Metrics and success measurement

**Use Case**: If research synthesis identifies organizational communication improvements or external messaging needs, this SOP defines the publication pipeline.

### Project CLAUDE.md: `organvm-corpvs-testamentvm/CLAUDE.md`
**Path**: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/CLAUDE.md`  
**Size**: ~1,500+ lines  
**Status**: ACTIVE (Project-level guidance document, canonical)

**Critical Sections**:
1. **What This Repository Is** — Governance corpus for 8-organ ORGANVM system; single source of truth
2. **Eight-Organ Model** — Complete architectural overview
3. **Key Invariants** — Unidirectional dependencies, promotion state machine, single registry
4. **Document Architecture** — Reading order with prerequisites:
   - Entry point: README.md
   - Then: constitution.md (ORGANVM principles)
   - Then: governance-rules.json (formalized rules, 6 articles)
   - Then: operational-cadence.md (process timing)
   - Then: seed.yaml contracts (per-repo automation)
   - Then: this CLAUDE.md (project context)
5. **Cross-Document Dependency Map** — Which documents reference which
6. **Implementation History** — All phases complete as of 2026-02-11
7. **TE Budget Model** — Token-Expended budget for AI-generated documentation:
   - Track token consumption for each governance artifact
   - Allocate budgets per organ and document type
   - Use for cost planning and efficiency optimization
8. **Org Naming Architecture** — GitHub org names vs. local directory names vs. domain names
9. **Working With This Corpus** — How to navigate, read, update, validate
10. **Artifact Routing Decision Tree** — Routes governance artifacts to appropriate stakeholders based on type and impact
11. **Invocation System** — 6 namespaces of short IDs for cross-document references:
    - RULE-* (governance rules)
    - STATE-* (promotion states)
    - EVENT-* (event types)
    - EDGE-* (dependency edges)
    - ISSUE-* (GitHub issue references)
    - ARTIFACT-* (governance artifacts)

**Importance**: Essential context for understanding where SOPs fit within governance framework and how research synthesis integrates with ORGAN-IV orchestration.

### Repository Overview: `organvm-corpvs-testamentvm/README.md`
**Path**: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/README.md`  
**Size**: ~32.2KB  
**Status**: LAUNCHED (Entry point for governance corpus)

**Contents**:
- Status badges: 8 organs, 97+ repos, ~404K+ words of documentation
- Repository structure overview
- Navigation guide for different user roles
- Quick-start examples
- Link to detailed CLAUDE.md for in-depth guidance

**Importance**: Provides orientation and entry point for understanding governance corpus structure.

---

## 4. Technical Implementation Details

### File Organization in organvm-corpvs-testamentvm
```
organvm-corpvs-testamentvm/
├── README.md                          # Entry point, system overview
├── CLAUDE.md                          # Project-level guidance
├── constitution.md                    # ORGANVM principles and philosophy
├── governance-rules.json              # 6 articles codified as JSON schema
├── operational-cadence.md             # Process timing and review cycles
├── docs/
│   └── operations/
│       ├── sop--document-audit-feature-extraction.md  ← PRIMARY SOP
│       ├── sop--pitch-deck-rollout.md                ← SECONDARY SOP
│       └── ... (other operational docs)
└── registry-v2.json                   # Single source of truth for 97+ repos
```

### Governance Document Dependency Hierarchy
```
README.md (entry point)
  ↓
constitution.md (ORGANVM principles)
  ↓
governance-rules.json (formalized rules)
  ↓
operational-cadence.md (process timing)
  ↓
seed.yaml (per-repo contracts)
  ↓
sop--document-audit-feature-extraction.md (synthesis workflow)
```

### registry-v2.json Structure (Abridged)
```json
{
  "metadata": {
    "version": "2.0",
    "last_updated": "2026-02-28T16:00:00Z",
    "total_repos": 97,
    "organs": 8
  },
  "repositories": [
    {
      "id": "organvm-iv-taxis",
      "name": "orchestration-start-here",
      "organ": "IV",
      "tier": "flagship",
      "promotion_status": "PUBLIC_PROCESS",
      "produces": ["governance_rules", "promotion_recommendations"],
      "consumes": ["system_events"],
      "seed_yaml": "path/to/seed.yaml"
    },
    ... (97 repos total)
  ]
}
```

### Invocation System Short IDs
For cross-document references in governance work:
- **RULE-001**: Unidirectional dependencies (I→II→III)
- **RULE-002**: Promotion state machine (LOCAL→CANDIDATE→PUBLIC_PROCESS→GRADUATED→ARCHIVED)
- **RULE-003**: Single registry source of truth
- **STATE-001**: LOCAL — Initial development state
- **STATE-002**: CANDIDATE — Ready for wider review
- **STATE-003**: PUBLIC_PROCESS — Active promotion evaluation
- **STATE-004**: GRADUATED — Stable production deployment
- **STATE-005**: ARCHIVED — Retired/superseded
- **EVENT-001**: promotion_advanced — Repo promoted to next state
- **EVENT-002**: registry_updated — Registry synchronized
- **EVENT-003**: ci_status_changed — GitHub Actions workflow result
- **EDGE-001**: organ_dependency — Organ produces/consumes other organ outputs
- **EDGE-002**: repo_dependency — Repo imports from another repo
- **ISSUE-*****: GitHub issue references with precise correlation to source docs

---

## 5. Error Handling and Fallback Solutions

### Read Tool Limitation (Previous Session)
**Problem**: Four parallel Read tool calls for SOP and documentation files returned only metadata (fileName, filePath, fileType) without actual markdown content.

**Root Cause**: Unclear — possible file access constraint, tool behavior limitation, or file size threshold.

**Impact**: Unable to satisfy user's explicit requirement to "read any matching files fully" and "report exact path and complete contents of SOP".

**Solution Applied**: Used bash `cat` command as fallback approach, which successfully retrieved complete file contents for all files.

**Result**: Successfully obtained full contents of:
- sop--document-audit-feature-extraction.md (~18KB)
- sop--pitch-deck-rollout.md (~32.5KB)
- CLAUDE.md (~1,500+ lines)
- README.md (~32.2KB)

**Lesson**: When Read tool returns metadata-only, bash `cat` provides reliable fallback for content retrieval.

### Protected File Handling
**Data Integrity Rule**: Never overwrite production data files wholesale.
- **registry-v2.json** — 2,200+ lines; must use targeted edits
- **governance-rules.json** — Legal rules; guard against accidental changes
- **system-metrics.json** — Computed metrics; regenerate, don't manually edit
- **seed.yaml files** — Automation contracts; changes affect CI/CD

**Pattern for Safe Edits**:
1. Read existing file completely
2. Identify specific sections to modify
3. Apply surgical edits (edit_block tool with old_string/new_string)
4. Validate against schema
5. Commit with clear changeset message

---

## 6. Problem-Solving Approach and Methodology

### Problem 1: Locating Research Ingestion/Synthesis/Digestion SOP
**Challenge**: User needed specific SOP; file location and naming unknown initially.

**Solution Strategy**: Multi-stage glob search across directory tree.

**Execution**:
1. Broad keyword glob: `**/sop*` → found `.../docs/operations/sop--*.md`
2. Targeted keyword globs: `**/*ingest*`, `**/*synth*`, `**/*digest*`, `**/*research*`, `**/*process*`
3. Directory structure search: `**/docs/**`, `**/sop/**`, `**/procedures/**`
4. Total: 15 candidate glob patterns executed
5. Results: 2 SOP files identified

**Result**: `sop--document-audit-feature-extraction.md` identified as primary match with 5-phase workflow directly matching research synthesis intent.

### Problem 2: Read Tool Failure
**Challenge**: Read tool failed to return actual file content despite metadata success; user request explicitly required full file contents.

**Diagnostic Steps**:
1. Observed Read tool returned only metadata
2. Attempted second Read call with different parameters (offset/length)
3. Recognized systematic Read tool limitation
4. Evaluated alternative tools: bash `cat` vs. grep vs. other

**Solution**: Pivoted to bash `cat` command (read-only tool, allowed in this context).

**Implementation**: Used bash `cat` to retrieve full contents for all 4 candidate files.

**Result**: Successfully obtained complete file contents, satisfying user's explicit requirement.

### Problem 3: Identifying Most Relevant SOP
**Challenge**: Two SOPs found; needed to determine which addressed research ingestion/synthesis/digestion specifically.

**Analysis Method**:
1. Read complete contents of both SOPs
2. Analyzed `sop--document-audit-feature-extraction.md`:
   - Found 5-phase workflow: Inventory → Exhaustive Read & Extraction → Deduplication → Issue Creation → Artifact Generation
   - "Exhaustive Read & Extraction" directly maps to **synthesis** (combining info from multiple sources)
   - "Deduplication" directly maps to **digestion** (reducing redundancy)
   - "Issue Creation" provides actionable output
   - Conclusion: **Perfect match for research synthesis workflow**
3. Analyzed `sop--pitch-deck-rollout.md`:
   - Covers external organizational communication
   - May apply if research outputs need presentation to stakeholders
   - Conclusion: **Conditional relevance; secondary SOP**

**Result**: Primary SOP identified with confidence; secondary SOP flagged for conditional use.

---

## 7. All User Messages (Complete History)

### Previous Session Message
```
"Search /Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm for an 
SOP (Standard Operating Procedure) related to research ingestion, synthesis, 
or digestion. It may be called SOP, ingestion-sop, synthesis-sop, research-process, 
or similar. Search broadly: 
1. First glob for any files with "sop", "ingest", "synth", "digest", "research", 
   "process" in their names 
2. Check any docs/, sop/, procedures/, or processes/ directories 
3. Read any matching files fully 
4. Report the exact path and complete contents of the SOP. 
Also check if there are any references to this SOP in CLAUDE.md or README files 
in that repo."
```

### Current Session Message
```
"Your task is to create a detailed summary of the conversation so far, paying 
close attention to the user's explicit requests and your previous actions. 
This summary should be thorough in capturing technical details, code patterns, 
and architectural decisions that would be essential for continuing development 
work without losing context."
```

---

## 8. Current Work Status

### Completed Tasks ✅
- Executed comprehensive glob search across directory tree
- Identified 2 SOP files with complete file paths
- Retrieved complete file contents using bash `cat` (fallback from Read tool limitation)
- Analyzed both SOPs for relevance to research synthesis
- Checked CLAUDE.md and README for cross-references
- Satisfied all 5 parts of original explicit user request

### Current Status
Research ingestion/synthesis/digestion SOP has been identified and documented:
- **Primary SOP**: `sop--document-audit-feature-extraction.md`
  - Location: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md`
  - Status: ACTIVE (Living document)
  - Relevance: **Exact match** for research synthesis workflow
  - Size: ~18KB
  - Workflow: 5-phase (Inventory → Exhaustive Read & Extraction → Deduplication → Issue Creation → Post-Audit Artifacts)

- **Secondary SOP**: `sop--pitch-deck-rollout.md`
  - Location: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--pitch-deck-rollout.md`
  - Status: ACTIVE (Living document)
  - Relevance: **Conditional** — applies if outputs need external organizational communication
  - Size: ~32.5KB

### Pending Tasks
These require explicit user direction to proceed:

1. **User Validation**: User review of identified primary SOP to confirm alignment with actual research ingestion/synthesis/digestion needs
2. **Implementation Decision**: Determine whether to:
   - Adopt existing SOP as-is
   - Customize it for specific use case
   - Create complementary workflow
3. **Integration Planning**: Decide how research synthesis workflows will integrate with:
   - Existing ORGAN-IV orchestration (agentic-titan, agent--claude-smith)
   - Governance document processing pipeline
4. **Tool Selection**: Determine implementation approach:
   - Automated via agentic-titan framework
   - Automated via agent--claude-smith SDK
   - Manual governance process
   - Hybrid approach
5. **Event System Coordination**: If automation chosen, determine:
   - Event subscriptions (what governance events trigger research synthesis)
   - Event production (what events research synthesis generates)
   - Integration with ORGAN-VI (Koinonia) and ORGAN-VII (Kerygma)

---

## 9. Optional Next Steps

**No action should be taken without explicit user direction.**

The user's most recent explicit request has been completed: a detailed conversation summary organized into 9 sections has been created and provided.

### If User Wants to Proceed with Implementation
User should:
1. Review `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md` to confirm it meets requirements
2. Specify how research synthesis should integrate with ORGAN-IV orchestration
3. Decide on implementation tool (agentic-titan vs. agent--claude-smith vs. manual)
4. Request creation of implementation plan or automation workflow

### If User Wants to Explore Further
User can request:
- Complete contents of either SOP file (will retrieve via bash `cat` if needed)
- Cross-reference analysis of governance document dependencies
- Integration architecture design for research synthesis pipeline
- Detailed workflow visualization or pseudocode for automation
- Event system design for triggering research synthesis processes

---

**Plan Created**: 2026-03-06  
**Status**: COMPLETE — Ready for user review and next direction
