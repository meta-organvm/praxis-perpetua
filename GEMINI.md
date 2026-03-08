<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** META-ORGANVM (Meta) | **Tier:** standard | **Status:** CANDIDATE
**Org:** `meta-organvm` | **Repo:** `praxis-perpetua`

### Edges
- **Consumes** ← `meta-organvm/organvm-corpvs-testamentvm`: reference

### Siblings in Meta
`.github`, `organvm-corpvs-testamentvm`, `alchemia-ingestvm`, `schema-definitions`, `organvm-engine`, `system-dashboard`, `organvm-mcp-server`

### Governance
- *Standard ORGANVM governance applies*

*Last synced: 2026-03-08T13:07:06Z*

## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`

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
| system | any | research-standards | METADOC: Architectural Typology & Research Standards |
| system | any | sop-ecosystem | METADOC: SOP Ecosystem — Taxonomy, Inventory & Coverage |
| system | any | autopoietic-systems-diagnostics | SOP: Autopoietic Systems Diagnostics (The Mirror of Eternity) |
| system | any | cicd-resilience-and-recovery | SOP: CI/CD Pipeline Resilience & Recovery |
| system | hardening | completeness-verification | completeness-verification |
| system | any | cross-agent-handoff | SOP: Cross-Agent Session Handoff |
| system | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction |
| system | any | essay-publishing-and-distribution | SOP: Essay Publishing & Distribution |
| system | any | market-gap-analysis | SOP: Full-Breath Market-Gap Analysis & Defensive Parrying |
| system | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |
| system | hardening | product-deployment-and-revenue-activation | product-deployment-and-revenue-activation |
| system | any | promotion-and-state-transitions | SOP: Promotion & State Transitions |
| system | any | repo-onboarding-and-habitat-creation | SOP: Repo Onboarding & Habitat Creation |
| system | any | research-to-implementation-pipeline | SOP: Research-to-Implementation Pipeline (The Gold Path) |
| system | any | security-and-accessibility-audit | SOP: Security & Accessibility Audit |
| system | any | session-self-critique | session-self-critique |
| system | any | source-evaluation-and-bibliography | SOP: Source Evaluation & Annotated Bibliography (The Refinery) |
| system | any | stranger-test-protocol | SOP: Stranger Test Protocol |
| system | any | strategic-foresight-and-futures | SOP: Strategic Foresight & Futures (The Telescope) |
| system | hardening | structural-integrity-audit | structural-integrity-audit |
| system | any | typological-hermeneutic-analysis | SOP: Typological & Hermeneutic Analysis (The Archaeology) |
| unknown | any | SOP-001-vector-pipeline-activation | SOP-001: Vector Pipeline Activation |
| unknown | any | cicd-resilience | SOP: CI/CD Pipeline Resilience & Recovery |
| unknown | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction v2.0 |
| unknown | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |

Linked skills: cross-agent-handoff, deployment-cicd, evaluation-to-growth, session-self-critique, structural-integrity-audit, verification-loop


**Prompting (Google)**: context 1M tokens (Gemini 1.5 Pro), format: markdown, thinking: thinking mode (thinkingConfig)


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

Cross-organ links: 416 | Top tags: `python`, `bash`, `pytest`, `mcp`, `go`

Run: `organvm atoms pipeline --write && organvm atoms fanout --write`

<!-- ORGANVM:AUTO:END -->
