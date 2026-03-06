# praxis-perpetua

**Process governance corpus for the ORGANVM eight-organ system.**

Praxis (practice informed by theory) + Perpetua (continuous/unending). This repo embodies the daily loop: practice, review, extract lessons, improve practice.

## Role in the System

The planning corpus (`organvm-corpvs-testamentvm`) governs **system state** — registry, rules, metrics, planning. This repo governs **process** — how we work, how we learn, how we review. Different concern, different repo.

**Organ:** META-ORGANVM | **Tier:** standard | **Status:** CANDIDATE

## Directory Structure

```
standards/          Governing standards: METADOCs and SOPs
templates/          Reusable review scaffolds (session reviews, audits, decision logs)
sessions/           Dated session logs (append-only archive)
lessons/            Extracted principles (living documents, updated as patterns emerge)
archive/            Superseded standards (never deleted, moved here)
```

## Standards

| Document | Scope |
|----------|-------|
| `METADOC--research-standards.md` | Architectural typology and research methodology |
| `SOP--session-self-critique.md` | Daily session review process |
| `SOP--cross-agent-handoff.md` | Receiving work from external AI agents |
| `SOP--structural-integrity-audit.md` | Deep codebase audit methodology |
| `SOP--market-gap-analysis.md` | Competitor deconstruction and strategic parrying |
| `SOP--research-to-implementation-pipeline.md` | Research-to-spec transformation pipeline |

## Usage

1. At session end, follow `SOP--session-self-critique.md`
2. Copy `templates/session-review.md` to `sessions/YYYY-MM-DD--description.md`
3. Complete the review phases
4. Update `lessons/derived-principles.md` with any new patterns

## Versioning

Standards are never overwritten. Revisions create new versions (`-v2.md`, `-v3.md`). Superseded versions move to `archive/YYYY-MM/`.

---
*ORGANVM Meta | Process Governance Corpus*
