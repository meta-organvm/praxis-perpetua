# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## What This Is

The **Studium Generale ORGANVM (SGO)** — ORGANVM's internal university, research engine, process governance corpus, and publication house. Named after the medieval *studium generale*: not a building but a right — the authority to teach, examine, and confer recognition anywhere.

Contains 47+ research documents, 64 SOPs/standards, an 11-chapter dissertation (SGO-2026-D-002), session review logs, derived principles, governance YAMLs, and defense rubrics. No code, no build system, no runtime — CI validates markdown structure only.

**Organ:** META-ORGANVM | **Tier:** standard | **Status:** GRADUATED

### SGO Identity

- **Cross-organ authority:** Any organ can commission research; the SGO evaluates and certifies
- **Evaluation machinery:** Shares IRA (multi-model evaluative consensus) with `auto-revision-epistemic-engine`
- **Publication channel:** Defended works flow through ORGAN-V (Logos)
- **Dual organism:** The SGO produces knowledge; the IRA certifies it. Immune system + nervous system.
- **Academic tiers:** Paper (ICC > 0.61), Thesis (ICC > 0.70), Dissertation (ICC > 0.75 + Provost)

## Key Rules

- **Session logs are append-only.** Never overwrite a dated session file in `sessions/`. Create a new dated file instead.
- **Derived principles are a living document.** Update `lessons/derived-principles.md` when new patterns emerge. Do not duplicate existing entries — refine them.
- **Standards follow ORGANVM versioning.** Never overwrite a standard in `standards/`. Create a new version (`-v2.md`, `-v3.md`) and move the old one to `archive/YYYY-MM/`.
- **Templates are reusable scaffolds.** Files in `templates/` are not instances — they are copied to `sessions/` or used as checklists during reviews.

## Directory Layout

```
governance/    SGO constitutional documents (charter, defense protocol, senate, faculty registry)
strategy/      Defense rubrics (universal + per-faculty), external feedback tracker
research/      Research corpus (47+ docs) + dissertation-institutional-authority/ (11 chapters)
standards/     Governing METADOCs and SOPs (64 documents)
commissions/   Research commission inquiry log
templates/     Reusable review scaffolds
sessions/      Dated session logs (YYYY-MM-DD--description.md)
lessons/       Extracted principles and risk profiles
archive/       Superseded standards
```

## Working Here

- No `pytest`, no `ruff`, no build commands. CI validates markdown structure only.
- Cross-references to other repos use relative paths from the workspace root (e.g., `meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`).
- The founding session log (`sessions/2026-03-06--gemini-styx-research.md`) documents the beta run that motivated this repo's creation.

## Relationship to Other Subprojects

- **organvm-corpvs-testamentvm**: System-state governance (registry, metrics, planning). This repo: process + academic governance (how we work + how we evaluate knowledge).
- **organvm-engine**: Provides CLI and automation. This repo: provides the human-readable standards that the engine enforces.
- **auto-revision-epistemic-engine** (ORGAN-I): The IRA evaluation machinery — shared infrastructure for SGO defenses.
- **organvm-v-logos**: Publication channel — defended works flow through Logos for distribution.
- **application-pipeline** (4444J99): SGO-2026-D-001 (Pipeline dissertation) lives there; certification records feed portfolio evidence.

### Provenance

Originally created 2026-03-06 as a process governance corpus. Evolved into the Studium Generale ORGANVM on 2026-03-19 when governance YAMLs were migrated from `organvm-i-theoria/studium-generale/` (now archived). The research corpus, dissertations, and standards were already here — the SGO formalized what was already happening.

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** META-ORGANVM (Meta) | **Tier:** standard | **Status:** GRADUATED
**Org:** `meta-organvm` | **Repo:** `praxis-perpetua`

### Edges
- **Consumes** ← `meta-organvm/organvm-corpvs-testamentvm`: reference

### Siblings in Meta
`.github`, `organvm-corpvs-testamentvm`, `alchemia-ingestvm`, `schema-definitions`, `organvm-engine`, `system-dashboard`, `organvm-mcp-server`, `stakeholder-portal`, `materia-collider`, `organvm-ontologia`

### Governance
- *Standard ORGANVM governance applies*

*Last synced: 2026-03-20T00:59:57Z*

## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`
4. Run `organvm prompts distill --dry-run` to detect uncovered operational patterns

Transcripts are on-demand (never committed):
- `organvm session transcript <id>` — conversation summary
- `organvm session transcript <id> --unabridged` — full audit trail
- `organvm session prompts <id>` — human prompts only


## Active Directives

| Scope | Phase | Name | Description |
|-------|-------|------|-------------|
| organ | any | commit-and-release-workflow | Commit & Release Workflow |
| organ | any | session-state-management | session-state-management |
| organ | any | submodule-sync-protocol | submodule-sync-protocol |
| system | any | prompting-standards | Prompting Standards |
| system | any | research-standards-bibliography | APPENDIX: Research Standards Bibliography |
| system | any | phase-closing-and-forward-plan | METADOC: Phase-Closing Commemoration & Forward Attack Plan |
| system | any | research-standards | METADOC: Architectural Typology & Research Standards |
| system | any | sop-ecosystem | METADOC: SOP Ecosystem — Taxonomy, Inventory & Coverage |
| system | any | autonomous-content-syndication | SOP: Autonomous Content Syndication (The Broadcast Protocol) |
| system | any | autopoietic-systems-diagnostics | SOP: Autopoietic Systems Diagnostics (The Mirror of Eternity) |
| system | any | background-task-resilience | background-task-resilience |
| system | any | cicd-resilience-and-recovery | SOP: CI/CD Pipeline Resilience & Recovery |
| system | any | community-event-facilitation | SOP: Community Event Facilitation (The Dialectic Crucible) |
| system | any | context-window-conservation | context-window-conservation |
| system | any | conversation-to-content-pipeline | SOP — Conversation-to-Content Pipeline |
| system | any | cross-agent-handoff | SOP: Cross-Agent Session Handoff |
| system | any | cross-channel-publishing-metrics | SOP: Cross-Channel Publishing Metrics (The Echo Protocol) |
| system | any | data-migration-and-backup | SOP: Data Migration and Backup Protocol (The Memory Vault) |
| system | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction |
| system | any | dynamic-lens-assembly | SOP: Dynamic Lens Assembly |
| system | any | essay-publishing-and-distribution | SOP: Essay Publishing & Distribution |
| system | any | formal-methods-applied-protocols | SOP: Formal Methods Applied Protocols |
| system | any | formal-methods-master-taxonomy | SOP: Formal Methods Master Taxonomy (The Blueprint of Proof) |
| system | any | formal-methods-tla-pluscal | SOP: Formal Methods — TLA+ and PlusCal Verification (The Blueprint Verifier) |
| system | any | generative-art-deployment | SOP: Generative Art Deployment (The Gallery Protocol) |
| system | any | market-gap-analysis | SOP: Full-Breath Market-Gap Analysis & Defensive Parrying |
| system | any | mcp-server-fleet-management | SOP: MCP Server Fleet Management (The Server Protocol) |
| system | any | multi-agent-swarm-orchestration | SOP: Multi-Agent Swarm Orchestration (The Polymorphic Swarm) |
| system | any | open-source-licensing-and-ip | SOP: Open Source Licensing and IP (The Commons Protocol) |
| system | any | performance-interface-design | SOP: Performance Interface Design (The Stage Protocol) |
| system | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |
| system | any | polymorphic-agent-testing | SOP: Polymorphic Agent Testing (The Adversarial Protocol) |
| system | any | promotion-and-state-transitions | SOP: Promotion & State Transitions |
| system | any | recursive-study-feedback | SOP: Recursive Study & Feedback Loop (The Ouroboros) |
| system | any | repo-onboarding-and-habitat-creation | SOP: Repo Onboarding & Habitat Creation |
| system | any | research-to-implementation-pipeline | SOP: Research-to-Implementation Pipeline (The Gold Path) |
| system | any | security-and-accessibility-audit | SOP: Security & Accessibility Audit |
| system | any | session-self-critique | session-self-critique |
| system | any | smart-contract-audit-and-legal-wrap | SOP: Smart Contract Audit and Legal Wrap (The Ledger Protocol) |
| system | any | source-evaluation-and-bibliography | SOP: Source Evaluation & Annotated Bibliography (The Refinery) |
| system | any | stranger-test-protocol | SOP: Stranger Test Protocol |
| system | any | strategic-foresight-and-futures | SOP: Strategic Foresight & Futures (The Telescope) |
| system | any | styx-pipeline-traversal | SOP: Styx Pipeline Traversal (The 7-Organ Transmutation) |
| system | any | system-dashboard-telemetry | SOP: System Dashboard Telemetry (The Panopticon Protocol) |
| system | any | the-membrane-protocol | the-membrane-protocol |
| system | any | theoretical-concept-versioning | SOP: Theoretical Concept Versioning (The Epistemic Protocol) |
| system | any | theory-to-concrete-gate | theory-to-concrete-gate |
| system | any | typological-hermeneutic-analysis | SOP: Typological & Hermeneutic Analysis (The Archaeology) |
| unknown | any | SOP-001-vector-pipeline-activation | SOP-001: Vector Pipeline Activation |
| unknown | any | cicd-resilience | SOP: CI/CD Pipeline Resilience & Recovery |
| unknown | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction v2.0 |
| unknown | any | ira-grade-norming | SOP: Diagnostic Inter-Rater Agreement (IRA) Grade Norming |
| unknown | any | ira-grade-norming | ira-grade-norming |
| unknown | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |

Linked skills: continuous-learning-agent, cross-agent-handoff, evaluation-to-growth, genesis-dna, multi-agent-workforce-planner, promotion-and-state-transitions, session-self-critique


**Prompting (Anthropic)**: context 200K tokens, format: XML tags, thinking: extended thinking (budget_tokens)


## Ecosystem Status

- **delivery**: 1/1 live, 0 planned
- **content**: 1/1 live, 0 planned

Run: `organvm ecosystem show praxis-perpetua` | `organvm ecosystem validate --organ META`


## Task Queue (from pipeline)

**13** pending tasks | Last pipeline: unknown

- `c3ba265ed715` organvm-engine/src/organvm_engine/sop/discover.py — Add `phase` field to SOPEntry [express, pytest, python]
- `362f9dd113b3` organvm-engine/src/organvm_engine/sop/resolver.py — Add `phase` filter + `promotion_to_phase() [express, pytest, python]
- `c478b2a12c39` organvm-engine/src/organvm_engine/cli/sop.py — Add `--phase` flag [express, pytest, python]
- `4f10858561c6` organvm-engine/src/organvm_engine/cli/__init__.py — Wire `--phase [express, pytest, python]
- `9ec2a0c60344` organvm-engine/src/organvm_engine/contextmd/sync.py — Auto-resolve phase from promotion_status [express, pytest, python]
- `0b31c511876b` organvm-engine/src/organvm_engine/contextmd/generator.py — Show phase in directives [express, pytest, python]
- `8e56e9d66554` praxis-perpetua/standards/SOP--genesis-dna.md — New: genesis bundle SOP [express, pytest, python]
- `69741e9c9ff1` praxis-perpetua/standards/SOP--structural-integrity-audit.md — Add `phase: hardening [express, pytest, python]
- ... and 5 more

Cross-organ links: 549 | Top tags: `python`, `bash`, `mcp`, `pytest`, `typescript`

Run: `organvm atoms pipeline --write && organvm atoms fanout --write`


## Entity Identity (Ontologia)

**UID:** `ent_repo_01KKKX3RVRNJK755GX7N9CJ3SJ` | **Matched by:** primary_name

Resolve: `organvm ontologia resolve praxis-perpetua` | History: `organvm ontologia history ent_repo_01KKKX3RVRNJK755GX7N9CJ3SJ`


## Live System Variables (Ontologia)

| Variable | Value | Scope | Updated |
|----------|-------|-------|---------|
| `active_repos` | 1 | global | 2026-03-20 |
| `archived_repos` | 0 | global | 2026-03-20 |
| `ci_workflows` | 1 | global | 2026-03-20 |
| `code_files` | 0 | global | 2026-03-20 |
| `dependency_edges` | 0 | global | 2026-03-20 |
| `operational_organs` | 1 | global | 2026-03-20 |
| `published_essays` | 0 | global | 2026-03-20 |
| `repos_with_tests` | 0 | global | 2026-03-20 |
| `sprints_completed` | 0 | global | 2026-03-20 |
| `test_files` | 0 | global | 2026-03-20 |
| `total_organs` | 1 | global | 2026-03-20 |
| `total_repos` | 1 | global | 2026-03-20 |
| `total_words_formatted` | 0 | global | 2026-03-20 |
| `total_words_numeric` | 0 | global | 2026-03-20 |
| `total_words_short` | 0K+ | global | 2026-03-20 |

Metrics: 9 registered | Observations: 5784 recorded
Resolve: `organvm ontologia status` | Refresh: `organvm refresh`


## System Density (auto-generated)

AMMOI: 58% | Edges: 28 | Tensions: 33 | Clusters: 5 | Adv: 3 | Events(24h): 8195
Structure: 8 organs / 113 repos / 1654 components (depth 17) | Inference: 98% | Organs: META-ORGANVM:70%, ORGAN-I:58%, ORGAN-II:48%, ORGAN-III:56% +4 more
Last pulse: 2026-03-20T00:59:49 | Δ24h: n/a | Δ7d: n/a

<!-- ORGANVM:AUTO:END -->
