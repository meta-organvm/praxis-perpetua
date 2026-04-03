# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## What This Is

The **Studium Generale ORGANVM (SGO)** — ORGANVM's internal university, research engine, process governance corpus, and publication house. Named after the medieval *studium generale*: not a building but a right — the authority to teach, examine, and confer recognition anywhere.

Contains 57+ research documents (8 thematic sub-collections + individual papers), 67 SOPs/standards, an 11-chapter dissertation (SGO-2026-D-002), session review logs, derived principles, governance YAMLs, defense rubrics, specifications, and a content pipeline for the Object Lessons publication. No code, no build system, no runtime — CI validates markdown structure only.

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
governance/          SGO constitutional documents (charter.yaml, defense-protocol.yaml,
                     faculty-registry.yaml, senate-config.yaml)
strategy/            Defense rubrics (universal + per-faculty), external feedback tracker
research/            Research corpus (57+ docs) — see Research Corpus below
standards/           Governing METADOCs and SOPs (67 documents)
commissions/         Research commission inquiry log (inquiry-log.yaml)
specifications/      SPEC files and design documents (TLA+ formal models, feature specs)
defenses/            Defense records and transcripts (records/, transcripts/)
publications/        Defended works ready for external release (arxiv/, journal/, distilled/)
content-pipeline/    Object Lessons publication: posts, templates, episode outlines, theory docs
                     (note: content-pipeline/object-lessons/ is a nested git repo)
scripts/             Session extraction tools (extract-claude-sessions.py,
                     extract-gemini-sessions.py, extract-claude-artifacts.py)
sessions/            Dated session logs (YYYY-MM-DD--description.md)
studies/             System studies: audits, findings, hypotheses, triage log
lessons/             Extracted principles and risk profiles
runbooks/            Operational runbooks
ecosystem/           Ecosystem profiles and YAML
testament/           Intellectual genealogy and testament documents
templates/           Reusable review scaffolds
archive/             Superseded standards
```

## Research Corpus

Eight thematic sub-collections plus individual research papers (57+ documents total):

| Sub-collection | Topic |
|----------------|-------|
| `dissertation-institutional-authority/` | SGO-2026-D-002: Recursive Institutional Governance via Multi-Model Evaluative Consensus (11 chapters) |
| `alchemical-system-lifecycle/` | The lifecycle of knowledge-producing systems |
| `everything-change+change-everything/` | Theory of systemic transformation |
| `infrastructure-as-art/` | Institutional infrastructure as creative practice |
| `radical-authenticity/` | Authenticity frameworks in systemic work |
| `solo-auteur-to-studio/` | Scaling from individual to institutional production |
| `system-as-genre/` | Systems as aesthetic and generic form |
| `trash-and-church/` | Cultural dialectics: disposable and sacred |

Individual papers cover: meta-laws of reality, multi-agent architecture, institutional governance, creative leadership frameworks, ontological topology of ORGANVM, formal methods, the Styx pipeline, AI conductor methodology, and more.

## SGO Governance Infrastructure

| File | Purpose |
|------|---------|
| `governance/charter.yaml` | Foundational charter: mission, scope, academic tiers (ICC thresholds) |
| `governance/defense-protocol.yaml` | Defense process: submission → review → panel → certification |
| `governance/faculty-registry.yaml` | Faculty roles, competency domains, IRA panel composition |
| `governance/senate-config.yaml` | Senate quorum rules, voting procedures, promotion authority |
| `commissions/inquiry-log.yaml` | Active and closed research commissions across all organs |

Academic tiers: Paper (ICC > 0.61), Thesis (ICC > 0.70), Dissertation (ICC > 0.75 + Provost).

## Content Pipeline

`content-pipeline/` houses the **Object Lessons** publication infrastructure:
- `object-lessons/` — nested git repo (the Object Lessons website/content repo)
- `posts/` — published and in-progress posts
- `episode-outlines/` — structured outlines per episode
- `theory/` — theoretical underpinnings
- `templates/` — post and episode templates
- `audits/` — content audits and reviews
- `amp-lab/` — experimental content experiments

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
- **Produces** → `organvm-v-logos`: publications
- **Produces** → `organvm-vii-kerygma`: research-distribution
- **Produces** → `organvm-vi-koinonia`: educational-material
- **Produces** → `4444j99/application-pipeline`: portfolio-evidence
- **Produces** → `external`: arxiv-preprints
- **Produces** → `META-ORGANVM`: governance-declarations
- **Consumes** ← `meta-organvm/organvm-corpvs-testamentvm`: reference
- **Consumes** ← `organvm-i-theoria/auto-revision-epistemic-engine`: ira-evaluation-machinery
- **Consumes** ← `organvm-i-theoria/recursive-engine--generative-entity`: symbolic-computing-framework
- **Consumes** ← `all-organs`: research-commissions

### Siblings in Meta
`.github`, `organvm-corpvs-testamentvm`, `alchemia-ingestvm`, `schema-definitions`, `organvm-engine`, `system-dashboard`, `organvm-mcp-server`, `stakeholder-portal`, `materia-collider`, `organvm-ontologia`, `vigiles-aeternae--agon-cosmogonicum`, `cvrsvs-honorvm`

### Governance
- *Standard ORGANVM governance applies*

*Last synced: 2026-04-02T17:06:50Z*

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
| system | any | atomic-clock | The Atomic Clock |
| system | any | execution-sequence | Execution Sequence |
| system | any | multi-agent-dispatch | Multi-Agent Dispatch |
| system | any | session-handoff-avalanche | Session Handoff Avalanche |
| system | any | system-loops | System Loops |
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
| system | any | network-testament-protocol | SOP: Network Testament Protocol (The Mirror Protocol) |
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
| system | any | the-descent-protocol | the-descent-protocol |
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
| unknown | any | SOP-TRIADIC-REVIEW-PROTOCOL | Triadic Review Protocol (TRP) |

Linked skills: cicd-resilience-and-recovery, continuous-learning-agent, cross-agent-handoff, evaluation-to-growth, genesis-dna, multi-agent-workforce-planner, promotion-and-state-transitions, quality-gate-baseline-calibration, repo-onboarding-and-habitat-creation, session-self-critique, structural-integrity-audit


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


## System Density (auto-generated)

AMMOI: 56% | Edges: 41 | Tensions: 0 | Clusters: 0 | Adv: 11 | Events(24h): 26946
Structure: 8 organs / 128 repos / 1654 components (depth 17) | Inference: 0% | Organs: META-ORGANVM:64%, ORGAN-I:55%, ORGAN-II:47%, ORGAN-III:55% +4 more
Last pulse: 2026-04-02T17:06:50 | Δ24h: -0.0% | Δ7d: n/a


## Dialect Identity (Trivium)

**Dialect:** SELF_WITNESSING | **Classical Parallel:** The Eighth Art | **Translation Role:** The Witness — proves all translations compose without loss

Strongest translations: I (formal), IV (structural), V (analogical)

Scan: `organvm trivium scan META <OTHER>` | Matrix: `organvm trivium matrix` | Synthesize: `organvm trivium synthesize`


## Logos Documentation Layer

**Status:** MISSING | **Symmetry:** 0.0 (VACUUM)

Nature demands a documentation counterpart. This formation maintains its narrative record in `docs/logos/`.

### The Tetradic Counterpart
- **[Telos (Idealized Form)](../docs/logos/telos.md)** — The dream and theoretical grounding.
- **[Pragma (Concrete State)](../docs/logos/pragma.md)** — The honest account of what exists.
- **[Praxis (Remediation Plan)](../docs/logos/praxis.md)** — The attack vectors for evolution.
- **[Receptio (Reception)](../docs/logos/receptio.md)** — The account of the constructed polis.

### Alchemical I/O
- **[Source & Transmutation](../docs/logos/alchemical-io.md)** — Narrative of inputs, process, and returns.



*Compliance: Formation is currently void.*

<!-- ORGANVM:AUTO:END -->

## Active Handoff Protocol

If `.conductor/active-handoff.md` exists, **READ IT FIRST** before doing any work.
It contains constraints, locked files, conventions, and completed work from the
originating agent. You MUST honor all constraints listed there.

If the handoff says "CROSS-VERIFICATION REQUIRED", your self-assessment will
NOT be trusted. A different agent will verify your output against these constraints.
