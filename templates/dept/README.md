# Department-Mapped SLP Library

Generative templates for populating a product's `docs/` directory. Each file contains all generation prompts for one department's artifacts.

## Architecture

**Layer 1 — System SOPs** (`praxis-perpetua/standards/`): Define _what_ each department needs and _when_.
**Layer 2 — Generative Templates** (this directory): Fill-in-the-blank scaffolds that reference Layer 1 SOPs.

Templates are **generative prompts**, not static forms. They auto-pull data from `seed.yaml`, `registry-v2.json`, `package.json`/`pyproject.toml`, and `src/` structure, then ask only what cannot be inferred.

## Department Index

| File | Dept | Persona | Artifacts | Phase Range |
|------|------|---------|-----------|-------------|
| `eng.md` | ENG | styx-engineering | E1-E5 | foundation–hardening |
| `leg.md` | LEG | styx-legal | L1-L7 | genesis–graduation |
| `prd.md` | PRD | styx-product | P1-P5 | genesis–graduation |
| `ops.md` | OPS | styx-ops | O1-O6 | foundation–graduation |
| `gro.md` | GRO | styx-growth | G1-G6 | hardening–graduation |
| `fin.md` | FIN | styx-finance | F1-F6 | genesis–graduation |
| `cxs.md` | CXS | styx-cx | C1-C5 | hardening–graduation |
| `b2b.md` | B2B | styx-sales | B1-B6 | hardening–graduation |
| `cross.md` | ALL | (varies) | X1-X8 | any |

## Data Sources (auto-pulled by all templates)

| Source | Provides |
|--------|----------|
| `seed.yaml` | Organ, tier, status, produces/consumes edges |
| `package.json` / `pyproject.toml` | Name, version, description, dependencies |
| `registry-v2.json` | Revenue model, revenue status, promotion state |
| `src/` directory | Modules, services, API routes |
| `CLAUDE.md` | Tech stack, CLI commands |
| `.github/workflows/` | CI config, deploy targets |
| `docs/` existing files | Skip already-written artifacts |

## Usage

### Single department
Give an AI agent one department file plus the product's repo path. The agent reads auto-pull sources, asks the declared questions, and generates all artifacts for that department.

### Full orchestration
Give an AI agent `orchestrator.md` plus the product's repo path. It determines lifecycle phase, activates relevant departments, deduplicates questions, and generates the full `docs/` tree.

### Phase gating
Templates declare which lifecycle phase each artifact activates at. An agent generating docs for a `CANDIDATE`-status product (foundation phase) will skip graduation-phase artifacts.

## Governing SOPs

Every template references one or more governing SOPs from `praxis-perpetua/standards/`:

| SOP | Departments |
|-----|-------------|
| `SOP--architecture-decision-records.md` | ENG, CROSS |
| `SOP--legal-compliance-matrix.md` | LEG |
| `SOP--business-organism-design.md` | FIN, GRO, B2B, OPS |
| `SOP--product-deployment-and-revenue-activation.md` | OPS, FIN, CXS |
| `SOP--repo-onboarding-and-habitat-creation.md` | ENG |
| `SOP--completeness-verification.md` | ENG |
| `SOP--market-gap-analysis.md` | PRD, B2B |
| `SOP--stranger-test-protocol.md` | PRD |
| `SOP--planning-and-roadmapping.md` | PRD, CROSS |
| `SOP--essay-publishing-and-distribution.md` | GRO |
| `SOP--security-and-accessibility-audit.md` | B2B |
| `SOP--pitch-deck-rollout.md` | B2B, CROSS |
| `SOP--cicd-resilience-and-recovery.md` | OPS |
| `SOP--readme-and-documentation.md` | CXS |
| `SOP--session-self-critique.md` | CROSS |
| `SOP--strategic-foresight-and-futures.md` | PRD, CXS |
| `SOP--promotion-and-state-transitions.md` | CROSS |
| `METADOC--research-standards.md` | CROSS |
