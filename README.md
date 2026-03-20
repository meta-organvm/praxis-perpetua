# praxis-perpetua

**Studium Generale ORGANVM (SGO) — Internal university, research engine, process governance corpus, and publication house for the ORGANVM eight-organ system.**

Praxis (practice informed by theory) + Perpetua (continuous/unending). Named after the medieval *studium generale* — not a building but a right: the authority to teach, examine, and confer recognition anywhere.

## Role in the System

The planning corpus (`organvm-corpvs-testamentvm`) governs **system state** — registry, rules, metrics, planning. This repo governs **process and knowledge** — how we work, how we learn, how we evaluate, and how we certify original contributions. The SGO shares IRA evaluation machinery with `auto-revision-epistemic-engine` for multi-model evaluative consensus.

**Organ:** META-ORGANVM | **Tier:** standard | **Status:** GRADUATED

## Directory Structure

```
governance/         SGO constitutional documents (charter, defense protocol, faculty registry, senate config)
strategy/           Defense rubrics (universal + per-faculty) and external feedback tracker
research/           Research corpus (47+ docs) and dissertation-institutional-authority/ (11 chapters)
commissions/        Research commission inquiry log (SGO-2026-D-001, SGO-2026-D-002)
standards/          Governing standards: 64 METADOCs and SOPs
templates/          Reusable review scaffolds (session reviews, audits, decision logs)
sessions/           Dated session logs (append-only archive)
lessons/            Extracted principles (living documents, updated as patterns emerge)
archive/            Superseded standards (never deleted, moved here)
```

## SGO Academic Structure

**Faculties:** 8 faculties mapping 1:1 to ORGANVM organs, each with its own rubric dimensions and methodological traditions.

**Academic Tiers:**

| Tier | Name | Panel | ICC Threshold |
|------|------|-------|--------------|
| I | Paper | 4 standing | > 0.61 |
| II | Thesis | 4 standing + 1 guest | > 0.70 |
| III | Dissertation | 4 standing + 2 guests + Provost | > 0.75 |

**Inaugural Dissertations:**
- SGO-2026-D-001: *Precision Over Volume* — MCDA framework for application pipeline management (Faculty of Applied Systems)
- SGO-2026-D-002: *Recursive Institutional Governance* — Multi-model evaluative consensus (Faculty of Governance + Meta-Cognition)

## Standards

| Document | Scope |
|----------|-------|
| `governance/charter.yaml` | SGO constitutional document — identity, authority, principles |
| `governance/defense-protocol.yaml` | 8-stage defense protocol with ICC thresholds |
| `governance/faculty-registry.yaml` | 8 faculties, rubric mappings, guest examiners |
| `governance/senate-config.yaml` | Standing senate (4 models), convocation rules |
| `strategy/defense-rubrics/universal.yaml` | 8 evaluation dimensions with 1-10 scale anchors |
| `METADOC--research-standards.md` | Architectural typology and research methodology |
| `SOP--session-self-critique.md` | Daily session review process |
| `SOP--cross-agent-handoff.md` | Receiving work from external AI agents |

## Usage

1. At session end, follow `SOP--session-self-critique.md`
2. Copy `templates/session-review.md` to `sessions/YYYY-MM-DD--description.md`
3. Complete the review phases
4. Update `lessons/derived-principles.md` with any new patterns

## Versioning

Standards are never overwritten. Revisions create new versions (`-v2.md`, `-v3.md`). Superseded versions move to `archive/YYYY-MM/`.

## Provenance

Created 2026-03-06 as a process governance corpus. Evolved into the Studium Generale ORGANVM on 2026-03-19 when governance YAMLs were migrated from `organvm-i-theoria/studium-generale/` (now archived).

---
*ORGANVM Meta | Studium Generale ORGANVM*
