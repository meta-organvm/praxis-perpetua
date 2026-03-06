# Conversation Summary: Research Ingestion SOP Search
**Date:** 2026-03-06  
**Project:** organvm-iv-taxis  
**Context Window:** Continued from previous session  
**Status:** Active investigation of research synthesis workflows

---

## 1. Primary Request and Intent

**Explicit 5-part user request** (previous session):
1. Search `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm` for Standard Operating Procedures (SOPs) related to research ingestion, synthesis, or digestion
2. Perform glob searches using keywords: "sop", "ingest", "synth", "digest", "research", "process"
3. Identify and check docs/, sop/, procedures/, or processes/ directories
4. Read all matching files in complete entirety
5. Report exact file paths and complete contents of relevant SOPs; check CLAUDE.md and README for cross-references

**Current session request:**
Create a detailed 9-section conversation summary capturing technical details, code patterns, and architectural decisions essential for continuing development work without context loss.

---

## 2. Key Technical Concepts and Architecture

### Eight-Organ ORGANVM System
- **Organ I (Theoria):** Foundational theory, recursive engines, symbolic computing
- **Organ II (Poiesis):** Generative art, performance systems, creative coding
- **Organ III (Ergon):** Commercial products, SaaS tools, developer utilities
- **Organ IV (Taxis):** Orchestration, governance, AI agents, skills (current project)
- **Organ V (Logos):** Public discourse, essays, editorial, analytics
- **Organ VI (Koinonia):** Community, reading groups, salons, learning
- **Organ VII (Kerygma):** POSSE distribution, social automation, announcements
- **META:** Cross-organ engine, schemas, dashboard, governance corpus

### Governance Model and Constraints
- **Unidirectional dependency flow:** I→II→III only; no back-edges; ORGAN-IV orchestrates all; ORGAN-V documents; ORGAN-VII amplifies
- **Promotion state machine:** LOCAL→CANDIDATE→PUBLIC_PROCESS→GRADUATED→ARCHIVED (no state skipping)
- **Single source of truth:** registry-v2.json (~2,200+ lines, ~97+ repos across all organs)
- **seed.yaml contract model:** Each repo declares organ membership, tier, produces/consumes edges, event subscriptions, CI agent definitions
- **Data integrity rules:** Never overwrite production data files wholesale; always read-before-write for JSON/YAML; protected files include registry-v2.json, governance-rules.json, system-metrics.json, all seed.yaml files
- **AI-conductor workflow model:** Human directs, AI generates volume, human reviews and refines; effort measured in LLM tokens (Token-Expended/TE budget)

### Git Architecture
- Root workspace `/Users/4jp/Workspace/` is NOT a git repo; contains 9+ organ directories
- Each organ directory contains 4-26 independent git repositories as subdirectories
- ORGAN-IV (`organvm-iv-taxis/`) is a git superproject using submodules (not subtrees)
- Submodule pointers synced via automated commits (`chore: sync organvm-iv-taxis submodule pointers`)

### Meta-ORGANVM Corpus Structure
`/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/` contains:
- Central governance documentation and SOPs
- registry-v2.json (single source of truth)
- governance-rules.json (6 articles codifying governance model)
- CLAUDE.md (~1,500+ lines, project-level guidance)
- README.md (~32.2KB, entry point documentation)
- docs/operations/ directory (contains SOPs)

---

## 3. Files Identified and Analyzed

### Primary SOP File
**File:** `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md`
- **Size:** ~18KB
- **Status:** ACTIVE (living document)
- **Relevance:** HIGH—Directly addresses research synthesis problem
- **Content Structure:** 5-phase workflow with detailed instructions per phase

**Five-Phase Workflow:**
1. **Inventory & Triage:** Map all governance documents, classify by type, identify interdependencies
2. **Exhaustive Read & Extraction:** Read complete governance documents, extract structured features, identify feature categories (aligns with "synthesis")
3. **Deduplication:** Identify redundant rules, find conflicting directives, consolidate equivalent features (aligns with "digestion")
4. **Issue Creation:** Convert extracted features to actionable GitHub issues with source document references
5. **Post-Audit Artifacts:** Generate governance metrics, create feature matrix, document gaps

**Input/Output Specifications:**
- Input: All governance documents from 97+ distributed repositories
- Output: Structured feature set, GitHub issues, governance metrics
- Quality gates: Completeness verification, conflict resolution, traceability confirmation
- Governance document cross-references: constitution.md, governance-rules.json, operational-cadence.md

### Secondary SOP File
**File:** `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--pitch-deck-rollout.md`
- **Size:** ~32.5KB
- **Status:** ACTIVE (living document)
- **Relevance:** CONDITIONAL—Applies if research synthesis outputs require external organizational communication
- **Content:** 16-section workflow covering pitch deck generation, README standardization, pitch.yaml authoring, auto-generation, deployment, CI/CD integration, quality gates, tier-based rollout sequencing

### Supporting Documentation
**CLAUDE.md** (`/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/CLAUDE.md`)
- Size: ~1,500+ lines
- Status: ACTIVE (project-level guidance document)
- Critical Sections:
  - What This Repository Is (governance corpus context)
  - Eight-Organ Model (ORGANVM architecture overview)
  - Key Invariants (immutable rules for governance system)
  - Document Architecture with reading order (dependency mapping)
  - TE Budget Model (token-expended budgeting for AI work)
  - Org Naming Architecture (organ-to-GitHub mappings)
  - Artifact Routing decision tree (directing governance artifacts to stakeholders)
  - Invocation System (6 namespaces: RULE-*, STATE-*, EVENT-*, EDGE-*, ISSUE-*, ARTIFACT-*)

**README.md** (`/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/README.md`)
- Size: ~32.2KB
- Status: LAUNCHED
- Contents: Status badges (8 organs, 97+ repos, ~404K+ words), repository structure, navigation guide, quick-start examples
- Role: Entry point for governance corpus understanding

**registry-v2.json**
- Size: ~2,200+ lines
- Status: Single source of truth for all repos
- Contents: Metadata, organ membership, tier classification, promotion status, produces/consumes edges, event subscriptions for each repo
- Protection rule: Protected file—must use targeted edits, never wholesale replacement

---

## 4. Search Methodology and Execution

### Glob Pattern Searches
Executed 15 glob pattern searches across `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/`:
- `**/sop*` — Identified SOP files
- `**/*ingest*` — No additional matches beyond SOP directory
- `**/*synth*` — No matches
- `**/*digest*` — No matches
- `**/*research*` — Minimal matches (mostly in documentation references)
- `**/*process*` — Identified processes/ references in documentation
- `**/docs/**` — Located docs/ directory with SOP files
- `**/procedures/**` — No procedures/ directory found
- `**/sop/**` — Confirmed SOP location
- `**/*.md` (targeted to docs/operations/) — Identified all markdown files in operations directory

### Results
- **Candidate files identified:** 2 SOP files in docs/operations/
- **Cross-references checked:** CLAUDE.md, README.md both reference governance workflows and operational cadence but do not explicitly mention "research ingestion" by name; however, sop--document-audit-feature-extraction.md is implicitly designed to address systematic research processing

---

## 5. Technical Details: Document Architecture and Invocation System

### Document Architecture (from CLAUDE.md)
**Reading Order:** Critical for understanding governance corpus structure
1. README.md (entry point)
2. CLAUDE.md (project guidance)
3. constitution.md (governance charter)
4. governance-rules.json (codified rules)
5. operational-cadence.md (timeline and scheduling)
6. registry-v2.json (metadata for all repos)
7. Specific SOPs as needed (operations/)
8. Organ-specific documentation

**Cross-Document Dependencies:** Documents reference each other via invocation system IDs

### Invocation System (6 Namespaces)
Used for cross-document references and governance artifact tracking:
1. **RULE-*:** Governance rules (e.g., RULE-002, RULE-006)
2. **STATE-*:** Governance states (promotion states, system states)
3. **EVENT-*:** System events for orchestration triggering
4. **EDGE-*:** Repository dependency edges (produces/consumes)
5. **ISSUE-*:** GitHub issues created from governance audit
6. **ARTIFACT-*:** Governance artifacts (metrics, matrices, reports)

### Governance Quadrilateral
- **Roadmap:** Long-term direction and vision
- **Cadence:** Timeline and scheduling (operational-cadence.md)
- **Catalog:** Registry of all repos (registry-v2.json)
- **Rolling TODO:** Active governance tasks (issues and PRs)

---

## 6. Tool Integration Patterns

### ORGAN-IV Orchestration Components
**agentic-titan** (Python ≥3.11, hatch):
- Polymorphic multi-agent orchestration framework
- 9 topology patterns, 22 agent archetypes
- Model-agnostic LLM adapters (Ollama, Anthropic, OpenAI, Groq)
- Workflow Engine (DAG-based)
- Runtime Fabric (local Python, Docker, OpenFaaS, Firecracker)
- Pub/sub event system
- Redis state management, ChromaDB vectors
- Safety & governance: HITL gates, RBAC, budget tracking, audit logging

**agent--claude-smith** (TypeScript/Node ≥20):
- Claude Agent SDK orchestrator
- Subagent spawning, session persistence
- Self-correction hooks
- 1Password secrets integration
- ES modules (`"type": "module"`), TypeScript strict mode
- Atomic session writes via KeyedMutex
- Command validation for security

**a-i--skills** (Python scripts):
- 101 example + 4 document skills
- Build/validation pipeline
- Skills live in `skills/{category}/{skill-name}/SKILL.md` with YAML frontmatter
- `.build/` directory contains committed generated artifacts
- CI validates generated files match source

### Integration Hints (from SOP)
sop--document-audit-feature-extraction.md contains **automation hints** for agentic-titan/agent--claude-smith integration:
- Suggests event-driven triggers for each phase
- Proposes agent archetypes for parallel processing
- Indicates checkpoint/gate mechanisms for HITL review

---

## 7. Errors, Fixes, and Problem-Solving Approach

### Read Tool Limitation (Resolved)
**Problem:** Four parallel Read tool calls for SOP and documentation files returned only file metadata (fileName, filePath, fileType) without actual markdown content

**Root Cause:** Unclear—possible file access constraint, tool behavior limitation, or file size threshold

**Impact:** Unable to complete explicit user requirement to "read any matching files fully" and "report exact path and complete contents of SOP"

**Fix Applied:** Used bash `cat` command as fallback approach, which successfully retrieved complete file contents for all files

**Result:** Successfully obtained full contents of all four candidate files, enabling continuation across context window boundaries

**Lesson Learned:** When Read tool returns metadata-only, pivot immediately to bash `cat` as reliable fallback for accessing complete file contents

### Glob Search Strategy
**Challenge:** Identifying research ingestion/synthesis/digestion SOP in unfamiliar governance corpus with inconsistent naming conventions

**Approach:** Broad pattern matching (15 glob patterns) rather than narrow keyword-specific search; this identified both explicit SOP files and references in documentation

**Result:** Located primary SOP (`sop--document-audit-feature-extraction.md`) with high confidence through content analysis rather than filename matching alone

### Content Relevance Analysis
**Challenge:** Determining which of two SOPs was most relevant to research synthesis request

**Approach:** Analyzed phase names and descriptions within each SOP; mapped phases to user request concepts (synthesis → exhaustive read & extraction; digestion → deduplication)

**Result:** Identified `sop--document-audit-feature-extraction.md` as primary SOP with direct alignment; flagged `sop--pitch-deck-rollout.md` as conditional/secondary

---

## 8. Architectural Decisions and Code Patterns

### Governance as Data
- Governance rules, states, and artifacts are stored as structured data (JSON/YAML)
- registry-v2.json serves as queryable source of truth
- governance-rules.json codifies Articles I-VI as machine-readable directives
- Enables automated validation (validate-deps.py checks for back-edge violations)

### Event-Driven Orchestration
- Repos publish events (product.release, product.milestone, community.event_created, etc.)
- agentic-titan monitors event subscriptions defined in seed.yaml
- EVENT_TEMPLATE_MAP maps event types to processing handlers
- Supports automated workflow triggering on governance events

### Workflow Staging via Phases
- sop--document-audit-feature-extraction.md uses 5-phase workflow model
- Each phase has explicit input/output specifications
- Enables asynchronous processing and human review gates
- Supports integration with agentic-titan topology patterns (map-reduce, pipeline, fan-out/fan-in)

### Artifact Routing Decision Tree (from CLAUDE.md)
Determines how governance artifacts (reports, metrics, issues) flow to stakeholders:
- Features requiring cross-organ coordination → cross-org governance issue
- Repo-specific features → issue in relevant repo
- Promotion state changes → ORGAN-IV orchestration event
- Metrics updates → system-metrics.json and dashboard

### TE Budget Allocation
- AI-conductor model tracks Token-Expended (TE) for each governance task
- Enables capacity planning and prioritization
- Influences which phases of audit are executed (can be resource-constrained)

---

## 9. Pending Tasks and Next Steps

### User Validation Required
1. **Review identified primary SOP:** Confirm `sop--document-audit-feature-extraction.md` aligns with actual research ingestion/synthesis/digestion needs
2. **Clarify scope:** Does "research ingestion" refer to:
   - Governance document analysis (primary SOP directly addresses this)
   - External research synthesis (different use case)
   - Cross-organ knowledge synthesis (implied by governance audit workflow)

### Implementation Decision Points
1. **Adopt existing SOP as-is:** Use 5-phase workflow verbatim for governance document analysis
2. **Customize for specific use case:** Adapt phases to domain-specific research synthesis
3. **Create complementary workflow:** Design new SOP for external research ingestion, leverage existing SOP for internal governance audit

### Integration Planning
1. **Automation level:** Manual governance process vs. agentic-titan-automated workflow
2. **Event subscriptions:** Determine which governance events trigger research synthesis
3. **Artifact routing:** Decide where synthesis outputs (issues, metrics, reports) route within ORGANVM system

### Tool Selection
1. **agentic-titan:** Use if parallel processing of 97+ repos and multi-topology orchestration needed
2. **agent--claude-smith:** Use if Claude-agent-specific orchestration and self-correction required
3. **Manual governance:** Use if human review gates are primary requirement

### Knowledge Gaps to Address
1. **ORGAN-V integration:** How does research synthesis outputs integrate with Logos (discourse) organ
2. **ORGAN-VI integration:** How do community signals (koinonia) feed into research synthesis
3. **Event system:** Exact event types and subscriptions needed for research synthesis automation

---

## Session Metadata
- **Current Date:** 2026-03-06
- **Project Working Directory:** `/Users/4jp/Workspace/organvm-iv-taxis/`
- **Target Search Directory:** `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/`
- **Primary SOP Location:** `docs/operations/sop--document-audit-feature-extraction.md`
- **Secondary Resources:** CLAUDE.md, README.md, registry-v2.json, governance-rules.json
- **Status:** Investigation complete; 9-section summary generated for context continuity; awaiting user direction on implementation approach

---

## 9-Section Conversation Summary (Context Continuity Record)

### Section 1: Explicit User Request and Search Parameters
The user requested a comprehensive search of `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm` for Standard Operating Procedures (SOPs) related to research ingestion, synthesis, or digestion. The 5-part request explicitly specified:
1. Glob pattern searches using keywords: "sop", "ingest", "synth", "digest", "research", "process"
2. Examination of docs/, sop/, procedures/, or processes/ directories
3. Complete reading of all matching files in their entirety
4. Reporting of exact file paths and complete contents of identified SOPs
5. Cross-reference verification in CLAUDE.md and README files

The current session request is to generate this detailed 9-section conversation summary to preserve technical context, architectural decisions, and code patterns essential for continuing development work without context loss.

### Section 2: ORGANVM System Architecture and Governance Model
**Eight-Organ System:** Theoria (I—foundational theory, recursive engines, symbolic computing), Poiesis (II—generative art, performance systems, creative coding), Ergon (III—commercial products, SaaS tools, developer utilities), Taxis (IV—orchestration, governance, AI agents, skills), Logos (V—public discourse, essays, editorial, analytics), Koinonia (VI—community, reading groups, salons, learning), Kerygma (VII—POSSE distribution, social automation, announcements), META (cross-organ engine, schemas, dashboard, governance corpus).

**Governance Constraints:** Unidirectional dependency flow (I→II→III only; no back-edges); ORGAN-IV orchestrates all; ORGAN-V documents (read-many-write-one); ORGAN-VII amplifies (consumer only). Enforced by governance-rules.json and validate-deps.py.

**Promotion State Machine:** LOCAL→CANDIDATE→PUBLIC_PROCESS→GRADUATED→ARCHIVED with no state skipping. Defined in governance-rules.json Article VI.

**Data Model:** Single source of truth is registry-v2.json (~2,200+ lines, ~97+ repos). Each repo declares membership via seed.yaml contract model (organ membership, tier, produces/consumes edges, event subscriptions, CI agent definitions). registry-v2.json, governance-rules.json, and system-metrics.json are protected files—must use targeted edits, never wholesale replacement. AI-conductor workflow model: Human directs, AI generates volume, human reviews and refines; effort measured in LLM tokens (Token-Expended/TE budget).

**Git Architecture:** Root workspace `/Users/4jp/Workspace/` is NOT a git repo. Each organ directory contains 4-26 independent git repositories as subdirectories. ORGAN-IV (`organvm-iv-taxis/`) is a git superproject using submodules (not subtrees); submodule pointers synced via automated commits (`chore: sync organvm-iv-taxis submodule pointers`).

### Section 3: Primary SOP Identification and Five-Phase Workflow
**Primary SOP:** `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md` (18KB, ACTIVE living document, HIGH relevance to research synthesis request).

**Five-Phase Workflow:**
1. **Inventory & Triage:** Map all governance documents, classify by type, identify interdependencies, establish triage criteria
2. **Exhaustive Read & Extraction:** Read complete governance documents, extract structured features, identify feature categories (directly aligns with "synthesis")
3. **Deduplication:** Identify redundant rules, find conflicting directives, consolidate equivalent features (directly aligns with "digestion")
4. **Issue Creation:** Convert extracted features to actionable GitHub issues with source document references, establish traceability
5. **Post-Audit Artifacts:** Generate governance metrics, create feature matrix, document gaps, measure system health

**Input/Output Specifications:**
- Input: All governance documents from 97+ distributed repositories (constitution.md, governance-rules.json, operational-cadence.md, registry-v2.json, etc.)
- Output: Structured feature set, GitHub issues, governance metrics
- Quality gates: Completeness verification, conflict resolution, traceability confirmation
- Automation hints: SOP includes explicit suggestions for agentic-titan/agent--claude-smith integration (event-driven triggers per phase, agent archetypes for parallel processing, checkpoint/gate mechanisms for HITL review)

**Secondary SOP:** `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--pitch-deck-rollout.md` (32.5KB, ACTIVE, CONDITIONAL relevance if research synthesis outputs require external organizational communication). Covers pitch deck generation, README standardization, pitch.yaml authoring, auto-generation, CI/CD integration, tier-based rollout sequencing.

### Section 4: Governance Corpus Documentation Architecture
**Document Reading Order (from CLAUDE.md):**
1. README.md (entry point, 32.2KB, LAUNCHED, contains status badges for 8 organs, 97+ repos, ~404K+ words)
2. CLAUDE.md (project guidance, 1,500+ lines, ACTIVE, covers architecture overview, key invariants, document dependencies, TE budget model, invocation system)
3. constitution.md (governance charter)
4. governance-rules.json (codified rules: Articles I-VI, particularly Article II on unidirectional dependencies and Article VI on promotion state machine)
5. operational-cadence.md (timeline and scheduling)
6. registry-v2.json (metadata for all ~97+ repos, promotion status, edges, event subscriptions)
7. Specific SOPs as needed (docs/operations/ directory)
8. Organ-specific documentation

**Cross-Document Dependencies:** Documents explicitly reference each other via invocation system IDs to enable artifact routing and governance tracking.

**Invocation System (6 Namespaces):** Used for cross-document references and governance artifact tracking:
- RULE-*: Governance rules (e.g., RULE-002, RULE-006) from governance-rules.json
- STATE-*: Governance states (promotion states, system states) from registry-v2.json
- EVENT-*: System events triggering orchestration (product.release, product.milestone, community.event_created, etc.)
- EDGE-*: Repository dependency edges (produces/consumes relationships)
- ISSUE-*: GitHub issues created from governance audit (Phase 4 output)
- ARTIFACT-*: Governance artifacts (metrics, matrices, reports, ARTIFACT-001 through ARTIFACT-N)

**Governance Quadrilateral:** Roadmap (long-term direction), Cadence (operational-cadence.md timeline), Catalog (registry-v2.json), Rolling TODO (active governance tasks/issues/PRs).

### Section 5: ORGAN-IV Orchestration Components and Tool Integration
**agentic-titan** (Python ≥3.11, hatch, FastAPI):
- Polymorphic multi-agent orchestration framework with 9 topology patterns (pipeline, map-reduce, fan-out/fan-in, etc.) and 22 agent archetypes
- Model-agnostic LLM adapters (Ollama, Anthropic, OpenAI, Groq)
- Workflow Engine with DAG-based specification
- Runtime Fabric: local Python, Docker, OpenFaaS, Firecracker
- Pub/sub event system for event-driven orchestration
- Redis state management, ChromaDB vectors for semantic search
- Safety & governance: HITL (human-in-the-loop) gates, RBAC (role-based access control), budget tracking, audit logging
- CLI entry point: `titan run <spec_path> -p "prompt"`
- Optional extras: vector-db, messaging, embeddings, dashboard, metrics, evaluation, ray, celery, auth, ratelimit, firecracker

**agent--claude-smith** (TypeScript/Node ≥20, Vitest):
- Claude Agent SDK orchestrator with subagent spawning and session persistence
- Self-correction hooks for autonomous error recovery
- 1Password secrets integration via `op://vault/item/field` references
- ES modules (`"type": "module"`), TypeScript strict mode
- Atomic session writes via KeyedMutex for concurrent access safety
- Command validation security layer (shell commands, write paths)
- Session persistence as JSON with type-safe validation
- Coverage thresholds: statements 80%, branches 75%, functions 80%, lines 80%

**a-i--skills** (Python scripts with YAML frontmatter):
- Collection of 101 example + 4 document skills for AI agents
- Build/validation pipeline ensures generated artifacts (.build/ directory, committed to git) match source
- Skill storage: `skills/{category}/{skill-name}/SKILL.md` with YAML frontmatter
- CI validates generated files for completeness and prevents drift
- Skills available for: creative (algorithmic-art, audio-engineering-patterns, etc.), data (pipeline-architect, storytelling-analyst, etc.), development (api-design-patterns, backend-patterns, etc.), and specialized domains

**Integration Hints (from SOP):** sop--document-audit-feature-extraction.md contains automation suggestions for each phase:
- Phase 1: Event-driven trigger on governance.audit_started, use INVENTORY agent archetype
- Phase 2: Parallel processing via fan-out/fan-in topology, use EXTRACTOR and SYNTHESIZER archetypes
- Phase 3: Use DEDUPLICATOR archetype, checkpoint for human review
- Phase 4: Automated GitHub issue creation via ISSUE_CREATOR agent
- Phase 5: Metrics computation via AGGREGATOR archetype, dashboard update

### Section 6: Search Methodology, Tool Limitations, and Workarounds
**Glob Pattern Execution:** Performed 15 broad glob pattern searches across `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/` to identify files matching "sop", "ingest", "synth", "digest", "research", "process" keywords. Broad pattern matching strategy proved effective for discovering SOP files despite inconsistent naming conventions in governance corpus.

**Read Tool Limitation (Resolved):**
- **Problem:** Four parallel Read tool calls for SOP and documentation files returned only file metadata (fileName, filePath, fileType) without actual markdown content
- **Root Cause:** Unclear—possible file access constraint, tool behavior limitation, or file size threshold
- **Impact:** Unable to complete explicit user requirement to "read any matching files fully" and "report exact path and complete contents of SOP"
- **Fix Applied:** Pivoted to bash `cat` command as fallback approach, which successfully retrieved complete file contents for all four candidate files
- **Result:** Successfully obtained full contents of all files, enabling thorough analysis and context continuity
- **Lesson Learned:** When Read tool returns metadata-only, immediately implement bash `cat` fallback for reliable access to complete file contents

**Content Relevance Analysis:** Analyzed phase names and descriptions within identified SOPs to map conceptual alignment with user's research synthesis request. Mapped synthesis concept to "Exhaustive Read & Extraction" phase; digestion concept to "Deduplication" phase. This enabled identification of primary SOP with high confidence through content analysis rather than filename matching alone.

### Section 7: Data Integrity Rules, Protected Files, and Workflow Patterns
**Protected Files (Never Overwrite Wholesale):**
- registry-v2.json: ~2,200+ lines, single source of truth for all repos
- governance-rules.json: 6 articles codifying governance model
- system-metrics.json: computed metrics (in both corpus and portfolio directories)
- Any seed.yaml: per-repo automation contracts

**Read-Before-Write Protocol:** Before modifying any JSON/YAML data file, must read existing content and apply targeted edits—never generate replacement from scratch. Code-level guard in organvm-engine: `save_registry()` refuses to write fewer than 50 repos to production path, catching test fixtures leaking into production.

**Governance as Data Pattern:** Governance rules, states, and artifacts stored as structured data (JSON/YAML). Enables automated validation (validate-deps.py checks for back-edge violations), event-driven orchestration, and artifact routing decisions.

**Event-Driven Orchestration Pattern:** Repos publish events (product.release, product.milestone, community.event_created, etc.). agentic-titan monitors event subscriptions defined in seed.yaml. EVENT_TEMPLATE_MAP maps event types to processing handlers. Supports automated workflow triggering on governance events.

**Workflow Staging via Phases:** sop--document-audit-feature-extraction.md uses 5-phase workflow model. Each phase has explicit input/output specifications, enabling asynchronous processing and human review gates. Integrates with agentic-titan topology patterns (map-reduce, pipeline, fan-out/fan-in).

**Artifact Routing Decision Tree (from CLAUDE.md):** Determines how governance artifacts flow to stakeholders:
- Features requiring cross-organ coordination → cross-org governance issue
- Repo-specific features → issue in relevant repo
- Promotion state changes → ORGAN-IV orchestration event
- Metrics updates → system-metrics.json and dashboard

### Section 8: Implementation Decision Framework and Knowledge Gaps
**Implementation Options (User Must Choose):**
1. **Adopt existing SOP as-is:** Use 5-phase workflow verbatim for governance document analysis
2. **Customize for specific use case:** Adapt phases to domain-specific research synthesis needs
3. **Create complementary workflow:** Design new SOP for external research ingestion, leverage existing SOP for internal governance audit

**Integration Planning Decisions:**
- Automation level: Manual governance process vs. agentic-titan-automated workflow vs. agent--claude-smith orchestration
- Event subscriptions: Which governance events trigger research synthesis pipeline
- Artifact routing: Where synthesis outputs (issues, metrics, reports) route within ORGANVM system

**Tool Selection Criteria:**
- **agentic-titan:** Use if parallel processing of 97+ repos and multi-topology orchestration needed
- **agent--claude-smith:** Use if Claude-agent-specific orchestration and self-correction required
- **Manual governance:** Use if human review gates are primary requirement

**Clarification Required:**
- Does "research ingestion" refer to: (a) governance document analysis (primary SOP directly addresses), (b) external research synthesis (different use case), or (c) cross-organ knowledge synthesis (implied by governance audit workflow)?
- What is the scope of "synthesis"? Document feature extraction? Domain knowledge consolidation? Cross-repo pattern discovery?
- What is the scope of "digestion"? Deduplication only? Conflict resolution? Normalization?

**Knowledge Gaps to Address:**
- ORGAN-V integration: How do research synthesis outputs integrate with Logos (public discourse) organ
- ORGAN-VI integration: How do community signals (koinonia) feed into research synthesis
- ORGAN-VII integration: How are synthesis insights distributed via Kerygma (distribution) organ
- Event system specifics: Exact event types and subscriptions needed for research synthesis automation
- TE budget allocation: Token-expended budget constraints for automation vs. manual review

### Section 9: Pending Tasks, Validation Requirements, and Status Summary
**Immediate Tasks (Awaiting User Direction):**
1. **Review primary SOP:** Confirm `sop--document-audit-feature-extraction.md` aligns with actual research ingestion/synthesis/digestion needs
2. **Scope clarification:** Provide specific definition of "research ingestion", "synthesis", and "digestion" in project context
3. **Implementation approach:** Choose among adopt-as-is, customize, or create-complementary approaches
4. **Integration scope:** Specify desired integration with ORGAN-IV orchestration (agentic-titan, agent--claude-smith, or manual)

**Investigation Status:** COMPLETE
- Search request (5 parts): Fully executed and documented
- Glob pattern searches: 15 searches performed, 2 SOP files identified
- File content retrieval: All candidate files successfully read (via bash fallback after Read tool limitation)
- Cross-reference verification: CLAUDE.md and README.md reviewed for governance framework integration points
- Architectural analysis: Complete documentation of ORGANVM governance model, orchestration framework, and workflow patterns
- Tool integration mapping: agentic-titan, agent--claude-smith, and a-i--skills capabilities analyzed for research synthesis integration

**Status Summary:** The SOP search investigation is complete and comprehensive. Primary SOP (`sop--document-audit-feature-extraction.md`) directly addresses the research synthesis request with a 5-phase workflow designed for governance document analysis, feature extraction (synthesis), deduplication (digestion), and automated artifact creation (issues, metrics). Secondary SOP available for cross-organ communication if needed. Full technical architecture, integration points, and decision framework documented above. System awaiting explicit user direction on implementation approach before proceeding with customization or integration planning.
