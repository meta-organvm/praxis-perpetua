# METADOC: SOP Ecosystem — Taxonomy, Inventory & Coverage

## 1. Ontological Foundation

This document is the **hub of hubs** for all governed process artifacts in the ORGANVM system. It defines the taxonomy of document types, establishes canonical locations, maps every SOP into functional clusters, traces upstream/downstream dependencies between procedures, and identifies coverage gaps.

The SOP ecosystem exists to answer one question: **"For any operational task in the ORGANVM system, does a governed procedure exist?"** If yes, this document tells you where to find it. If no, this document tells you it's missing and what would fill the gap.

**Scope:** All SOPs, METADOCs, standards, templates, lessons, and operational guides across both `praxis-perpetua` (process governance) and `organvm-corpvs-testamentvm` (system-state governance).

---

## 2. Document Taxonomy

Six document categories, each with a canonical home and clear purpose.

| Category | Prefix/Convention | Canonical Home | Purpose |
|----------|-------------------|----------------|---------|
| **METADOC** | `METADOC--*.md` | `praxis-perpetua/standards/` | Governing frameworks — foundational mandates that define methodology and spawn SOPs |
| **SOP** | `SOP--*.md` | `praxis-perpetua/standards/` | Reusable methodological procedures — step-by-step protocols for repeatable operations |
| **Template** | descriptive name | `praxis-perpetua/templates/` | Reusable scaffolds — fill-in-the-blank structures for consistent execution |
| **Lesson** | descriptive name | `praxis-perpetua/lessons/` | Derived principles — accumulated wisdom from practice, updated continuously |
| **Operational Guide** | descriptive name | `corpus/docs/operations/` | System-specific how-tos — tied to scripts, data files, and specific toolchain |
| **Standard** | numbered `NN-*.md` | `corpus/docs/standards/` | Cross-repo standards — enforced requirements for all repositories |

| **SOP-Skill** | `{name}.md` in `.sops/` | `{repo}/.sops/` or `{organ}/.sops/` | Scoped procedural directives — auto-discovered, no naming prefix required |

### Routing Rule

> **If the document describes a reusable methodology (how to do a type of thing), it belongs in praxis-perpetua. If it describes how to operate a specific system artifact (how to run this script, how to update this file), it belongs in the corpus. If it describes a procedure scoped to one repo or organ, it belongs in that repo's or organ's `.sops/` directory.**

### Migration Policy

Documents with `SOP--` prefix in the corpus that are reusable methodological procedures (not system-specific how-tos) should migrate to praxis-perpetua. Corpus originals receive a one-line header noting the canonical location, preserved as reference copies.

---

## 3. Complete Inventory

### 3.1 praxis-perpetua/standards/ (METADOCs & SOPs)

| # | File | Type | Cluster | Status |
|---|------|------|---------|--------|
| 1 | `METADOC--research-standards.md` | METADOC | Research | Active |
| 2 | `METADOC--sop-ecosystem.md` | METADOC | Hub | Active |
| 3 | `SOP--source-evaluation-and-bibliography.md` | SOP | Research | Active |
| 4 | `SOP--typological-hermeneutic-analysis.md` | SOP | Research | Active |
| 5 | `SOP--strategic-foresight-and-futures.md` | SOP | Research | Active |
| 6 | `SOP--autopoietic-systems-diagnostics.md` | SOP | Research | Active |
| 7 | `SOP--market-gap-analysis.md` | SOP | Research | Active |
| 8 | `SOP--research-to-implementation-pipeline.md` | SOP | Research | Active |
| 9 | `SOP--structural-integrity-audit.md` | SOP | Quality | Active |
| 10 | `SOP--document-audit-feature-extraction.md` | SOP | Quality | Active |
| 11 | `SOP--security-and-accessibility-audit.md` | SOP | Quality | Active |
| 12 | `SOP--stranger-test-protocol.md` | SOP | Quality | Migrated from corpus |
| 13 | `SOP--promotion-and-state-transitions.md` | SOP | Governance | Active |
| 14 | `SOP--repo-onboarding-and-habitat-creation.md` | SOP | Governance | Active |
| 15 | `SOP--cross-agent-handoff.md` | SOP | Governance | Active |
| 16 | `SOP--product-deployment-and-revenue-activation.md` | SOP | Operations | Active |
| 17 | `SOP--essay-publishing-and-distribution.md` | SOP | Operations | Active |
| 18 | `SOP--pitch-deck-rollout.md` | SOP | Operations | Migrated from corpus |
| 19 | `SOP--cicd-resilience-and-recovery.md` | SOP | Operations | Migrated from corpus |
| 20 | `SOP--session-self-critique.md` | SOP | Operations | Active |
| 21 | `SOP--planning-and-roadmapping.md` | SOP | Planning | Active |
| 22 | `SOP--ontological-renaming.md` | SOP | Governance | Active |
| 23 | `SOP--agent-seeding-and-workforce-planning.md` | SOP | Operations | Active |
| 24 | `SOP--readme-and-documentation.md` | SOP | Quality | Active |
| 25 | `SOP--business-organism-design.md` | SOP | Planning | Active |
| 26 | `SOP--completeness-verification.md` | SOP | Quality | Active |
| 27 | `SOP--project-board-taxonomy.md` | SOP | Planning | Active |
| 28 | `SOP--recursive-study-feedback.md` | SOP | Research | Active |
| 29 | `APPENDIX--research-standards-bibliography.md` | Appendix | Research | Active |

### 3.2 praxis-perpetua/templates/

| # | File | Purpose |
|---|------|---------|
| 1 | `session-review.md` | Post-session review scaffold |
| 2 | `content-audit.md` | Content quality assessment |
| 3 | `decision-log.md` | ACCEPT/REJECT/EXPAND decision tracking |
| 4 | `handoff-triage.md` | Cross-agent handoff checklist |
| 5 | `transcript-style-guide.md` | Session transcript rendering conventions |
| 6 | `source-evaluation-scorecard.md` | CRAAP + 5 Cs source evaluation |

### 3.3 praxis-perpetua/lessons/

| # | File | Purpose |
|---|------|---------|
| 1 | `derived-principles.md` | Living document of accumulated wisdom |
| 2 | `agent-behavioral-risks.md` | Per-agent risk profiles and mitigations |
| 3 | `structural-patterns.md` | Recurring structural patterns across sessions |

### 3.4 organvm-corpvs-testamentvm/docs/operations/ (Operational Guides)

| # | File | Type | Note |
|---|------|------|------|
| 1 | `key-workflows.md` | Guide | 7 procedures tied to corpus scripts. See praxis SOPs for formalized versions of sections 2, 3, 6. |
| 2 | `operational-cadence.md` | Guide | Living playbook with time-bound content |
| 3 | `minimum-viable-operations.md` | Guide | System-specific operator guide |
| 4 | `emergency-procedures.md` | Guide | Triage tied to specific infrastructure |
| 5 | `autonomous-setup-guide.md` | Guide | One-time setup guide |
| 6 | `sop--pitch-deck-rollout.md` | Reference | Canonical version migrated to praxis-perpetua |
| 7 | `sop--cicd-resilience.md` | Reference | Canonical version migrated to praxis-perpetua |
| 8 | `stranger-test-protocol.md` | Reference | Canonical version migrated to praxis-perpetua |
| 9 | `concordance.md` | Reference | Invocation symbol lookup table |
| 10 | `concordance-quickref.md` | Reference | Quick-reference concordance |
| 11 | `accessibility-audit-2026-03.md` | Audit | Point-in-time assessment |
| 12 | `security-audit-2026-03.md` | Audit | Point-in-time assessment |

### 3.5 organvm-corpvs-testamentvm/docs/standards/

| # | File | Type |
|---|------|------|
| 1 | `10-repository-standards.md` | Standard |
| 2 | `11-specification-driven-development.md` | Standard |
| 3 | `12-habitat-governance-lifecycle.md` | Standard |

### 3.6 External SOPs (organ-specific, live with their artifact)

SOPs that describe how to operate a specific system artifact belong with that artifact (per the routing rule in §2). They are tracked here for inventory completeness but are not migrated to praxis-perpetua.

| # | File | Organ | Repo | Purpose |
|---|------|-------|------|---------|
| 1 | `sop-doctoral-dissertation.md` | ORGAN-V | `organvm-v-logos/public-process` | Doctoral dissertation research and writing workflow |
| 2 | `sop--diagnostic-inter-rater-agreement.md` | PERSONAL | `4444J99/application-pipeline` | Diagnostic inter-rater agreement procedure for applications |

---

## 4. SOP Cluster Map

SOPs are organized into four functional clusters plus supporting artifacts. Each cluster has a hub document (METADOC or primary SOP) that provides context for its members.

```
METADOC--sop-ecosystem.md (this document — hub of hubs)
    |
    +-- CLUSTER 1: Research Methodology
    |   +-- METADOC--research-standards.md (cluster hub)
    |   +-- SOP--source-evaluation-and-bibliography.md
    |   +-- SOP--typological-hermeneutic-analysis.md
    |   +-- SOP--strategic-foresight-and-futures.md
    |   +-- SOP--autopoietic-systems-diagnostics.md
    |   +-- SOP--market-gap-analysis.md
    |   +-- SOP--research-to-implementation-pipeline.md
    |   +-- SOP--recursive-study-feedback.md
    |
    +-- CLUSTER 2: Quality & Integrity
    |   +-- SOP--structural-integrity-audit.md
    |   +-- SOP--document-audit-feature-extraction.md
    |   +-- SOP--security-and-accessibility-audit.md
    |   +-- SOP--stranger-test-protocol.md
    |   +-- SOP--readme-and-documentation.md
    |   +-- SOP--completeness-verification.md
    |
    +-- CLUSTER 3: Governance & Lifecycle
    |   +-- SOP--promotion-and-state-transitions.md
    |   +-- SOP--repo-onboarding-and-habitat-creation.md
    |   +-- SOP--cross-agent-handoff.md
    |   +-- SOP--ontological-renaming.md
    |
    +-- CLUSTER 4: Operations & Delivery
    |   +-- SOP--product-deployment-and-revenue-activation.md
    |   +-- SOP--essay-publishing-and-distribution.md
    |   +-- SOP--pitch-deck-rollout.md
    |   +-- SOP--cicd-resilience-and-recovery.md
    |   +-- SOP--session-self-critique.md
    |   +-- SOP--agent-seeding-and-workforce-planning.md
    |
    +-- CLUSTER 5: Planning & Design
    |   +-- SOP--planning-and-roadmapping.md
    |   +-- SOP--business-organism-design.md
    |   +-- SOP--project-board-taxonomy.md
    |
    +-- SUPPORTING
        +-- APPENDIX--research-standards-bibliography.md
        +-- templates/ (6 files)
        +-- lessons/ (3 files)
```

**Total governed artifacts:** 2 METADOCs + 25 SOPs + 1 appendix + 6 templates + 3 lessons = **37 artifacts**.

---

## 5. Pipeline Diagram — SOP Dependencies

SOPs are not isolated procedures. They feed into and consume from each other. This diagram traces the primary flows.

```
                    ONBOARDING                    RESEARCH
                       |                             |
    SOP--repo-onboarding  ----+     SOP--source-evaluation
                              |              |
                              v              v
                    SOP--promotion    SOP--typological-hermeneutic
                         |                   |
                         v                   v
               SOP--pitch-deck      SOP--market-gap-analysis
                    rollout                  |
                         |                   v
                         v        SOP--research-to-implementation
              SOP--product-deployment        |
                         |                   v
                         v        SOP--strategic-foresight
              SOP--essay-publishing          |
                         |                   v
                         v        SOP--autopoietic-diagnostics
                   [POSSE/VII]               |
                                             v
                                    SOP--recursive-study-feedback
                                             |
                                             v
                                    [feedback -> source-eval]

    QUALITY (cross-cutting — invoked at milestones)
    +-- SOP--structural-integrity-audit (at promotion, release)
    +-- SOP--document-audit-feature-extraction (quarterly, post-import)
    +-- SOP--security-and-accessibility-audit (quarterly, post-deploy)
    +-- SOP--stranger-test-protocol (at PUBLIC_PROCESS promotion)

    GOVERNANCE (cross-cutting — invoked at boundaries)
    +-- SOP--cross-agent-handoff (at agent session boundaries)
    +-- SOP--session-self-critique (at every session end)
    +-- SOP--cicd-resilience-and-recovery (at CI failure)
```

### Key Upstream/Downstream Relationships

| SOP | Upstream (feeds into this) | Downstream (this feeds into) |
|-----|---------------------------|------------------------------|
| repo-onboarding | (entry point) | promotion, pitch-deck |
| promotion | repo-onboarding, structural-integrity | pitch-deck, product-deployment |
| product-deployment | promotion | essay-publishing |
| essay-publishing | product-deployment, research-to-implementation | (POSSE distribution) |
| source-evaluation | (entry point) | typological-hermeneutic, market-gap |
| structural-integrity | (triggered at milestones) | promotion (gate) |
| security-accessibility | (triggered quarterly) | promotion (gate), product-deployment (gate) |
| stranger-test | promotion (at PUBLIC_PROCESS) | (documentation improvements) |
| planning-and-roadmapping | (entry point) | repo-onboarding, agent-seeding |
| ontological-renaming | (entry point) | repo-onboarding |
| agent-seeding | planning-and-roadmapping | cross-agent-handoff, session-self-critique |
| readme-and-documentation | repo-onboarding | stranger-test, structural-integrity |
| business-organism-design | market-gap-analysis, planning-and-roadmapping | product-deployment |
| project-board-taxonomy | planning-and-roadmapping, business-organism-design, agent-seeding | (board operations) |
| recursive-study-feedback | autopoietic-diagnostics, all study outputs | source-evaluation, typological-hermeneutic, derived-principles |
| completeness-verification | (triggered at milestones) | promotion (gate) |

---

## 6. Coverage Matrix — Organs x Operational Domains

This matrix maps which SOPs provide coverage for each organ across key operational domains. Coverage ratings: FULL (dedicated SOP covers this), PARTIAL (SOP applies but not organ-specific), GAP (no SOP coverage).

| Domain | I Theoria | II Poiesis | III Ergon | IV Taxis | V Logos | VI Koinonia | VII Kerygma | META |
|--------|-----------|------------|-----------|----------|---------|-------------|-------------|------|
| **Research** | FULL | FULL | FULL | PARTIAL | PARTIAL | PARTIAL | — | FULL |
| **Repo Onboarding** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Promotion** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Deployment** | PARTIAL | PARTIAL | FULL | PARTIAL | PARTIAL | — | — | PARTIAL |
| **Publishing** | — | — | PARTIAL | — | FULL | — | FULL | — |
| **Quality Audit** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Security Audit** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Pitch Deck** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **CI/CD Recovery** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Agent Handoff** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Session Review** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Planning** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Documentation** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Naming** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Agent Workforce** | PARTIAL | PARTIAL | FULL | FULL | PARTIAL | PARTIAL | — | FULL |
| **Completeness** | FULL | FULL | FULL | FULL | FULL | FULL | FULL | FULL |
| **Business Design** | — | — | FULL | — | — | — | — | PARTIAL |

### Coverage Notes

- **Research** is PARTIAL for IV-VI because these organs rarely need deep typological or foresight research — their research needs are operational, not academic. The research cluster SOPs apply when needed.
- **Deployment** is organ-specific: ORGAN-III has full coverage via `SOP--product-deployment-and-revenue-activation.md`; other organs deploy via simpler GitHub Pages or static hosting patterns covered by the pitch deck and CI/CD SOPs.
- **Publishing** covers ORGAN-V (essays) and ORGAN-VII (POSSE distribution) specifically via `SOP--essay-publishing-and-distribution.md`.
- **Planning** is universally applicable via `SOP--planning-and-roadmapping.md` — any initiative requiring phased execution.
- **Agent Workforce** is PARTIAL for organs that rarely need multi-agent parallelism (I, II, V, VI) — single-agent sessions suffice for most theoretical and community work.
- **Business Design** applies primarily to ORGAN-III (commercial products) via `SOP--business-organism-design.md`. META has partial coverage for system-wide business modeling.

---

## 7. Gap Register

Identified gaps with severity and resolution status.

| # | Gap | Severity | Status | Resolution |
|---|-----|----------|--------|------------|
| G1 | No SOP for promotion execution | HIGH | RESOLVED | `SOP--promotion-and-state-transitions.md` created |
| G2 | No SOP for new repo creation | HIGH | RESOLVED | `SOP--repo-onboarding-and-habitat-creation.md` created |
| G3 | No SOP for product deployment / revenue | HIGH | RESOLVED | `SOP--product-deployment-and-revenue-activation.md` created |
| G4 | No SOP for essay publishing pipeline | MEDIUM | RESOLVED | `SOP--essay-publishing-and-distribution.md` created |
| G5 | No SOP for repeatable security/a11y audits | MEDIUM | RESOLVED | `SOP--security-and-accessibility-audit.md` created |
| G6 | Pitch deck SOP in corpus, not praxis | LOW | RESOLVED | Migrated to praxis-perpetua |
| G7 | CI/CD resilience SOP in corpus, not praxis | LOW | RESOLVED | Migrated to praxis-perpetua |
| G8 | Stranger test protocol not in SOP format | LOW | RESOLVED | Migrated and normalized to praxis-perpetua |
| G9 | No formal data migration/backup SOP | LOW | OPEN | Future: `SOP--data-migration-and-backup.md` |
| G10 | No SOP for community event facilitation (VI) | LOW | OPEN | Future: organ-specific when community launches |
| G11 | No SOP for planning and roadmapping | HIGH | RESOLVED | `SOP--planning-and-roadmapping.md` created (distill pipeline) |
| G12 | No SOP for ontological naming conventions | MEDIUM | RESOLVED | `SOP--ontological-renaming.md` created (distill pipeline) |
| G13 | No SOP for agent workforce decomposition | HIGH | RESOLVED | `SOP--agent-seeding-and-workforce-planning.md` created (distill pipeline) |
| G14 | No SOP for README/documentation standards | MEDIUM | RESOLVED | `SOP--readme-and-documentation.md` created (distill pipeline) |
| G15 | No SOP for business organism design | MEDIUM | RESOLVED | `SOP--business-organism-design.md` created (distill pipeline) |
| G16 | No SOP for completeness verification | MEDIUM | RESOLVED | `SOP--completeness-verification.md` created (distill pipeline) |

---

## 8. Format Conventions

Every SOP in this ecosystem follows a consistent format:

1. `# SOP: {Title}` heading
2. `## 1. Ontological Purpose` — with cross-ref to governing METADOC
3. `## N. Phase {N}: {Title}` for each procedural phase
4. `### Process` — numbered steps under each phase
5. `### Starter Research Questions` — 4-6 questions per phase
6. `## N. Output Artifacts` — list of deliverables
7. Appendices for templates, tables, and cross-references
8. Version line: `*Version: 1.0.0 | System-Wide Directive | ORGANVM*`

METADOCs follow a freer structure but must include: ontological foundation, cluster/pipeline map, cross-references, and version line.

---

## 9. Maintenance

This METADOC is updated when:
- A new SOP is created (add to inventory + cluster map)
- An SOP is migrated between repos (update inventory + routing)
- A new gap is identified (add to gap register)
- A gap is resolved (update status)
- Coverage matrix changes (organ gains/loses SOP coverage)

---

## 10. Four-Tier Procedural Directive Model

SOPs and skills are structurally the same thing — procedural directives for agents. The four-tier model unifies them under a resolution cascade where more-specific directives override or complement less-specific ones.

| Tier | Scope | Location | Format | Discovery |
|------|-------|----------|--------|-----------|
| **T1: Universal** | Generic, any project | `a-i--skills/skills/{cat}/{name}/SKILL.md` | Skill frontmatter | Skill build system |
| **T2: System** | All ORGANVM organs | `praxis-perpetua/standards/SOP--*.md` | SOP + optional frontmatter | `organvm sop discover` |
| **T3: Organ** | All repos in one organ | `{organ-superproject}/.sops/{name}.md` | SOP with frontmatter | `organvm sop discover` |
| **T4: Repo** | One repository | `{repo}/.sops/{name}.md` | SOP with frontmatter | `organvm sop discover` |

**Resolution cascade** (most-specific wins): T4 > T3 > T2 > T1

### SOP-Skill Bridge Format

SOPs gain optional YAML frontmatter (backward-compatible — existing SOPs work without it):

```yaml
---
sop: true
name: structural-integrity-audit
scope: system                    # system | organ | repo
triggers:
  - context:code-review
  - context:promotion
complements:
  - verification-loop            # links to T1 universal skill
overrides: null                  # name of higher-scope SOP this replaces
---
# SOP: Structural Integrity Audit
...existing content unchanged...
```

### Skill-to-SOP Mappings

| T1 Universal Skill | T2 System SOP | Relationship |
|---------------------|---------------|-------------|
| `verification-loop` | `SOP--structural-integrity-audit` | SOP = ORGANVM-specific version |
| `evaluation-to-growth` | `SOP--session-self-critique` | SOP governs ORGANVM session reviews |
| `deployment-cicd` | `SOP--product-deployment-and-revenue-activation` | SOP adds Stripe/monitoring specifics |
| `security-essentials-pack` | `SOP--security-and-accessibility-audit` | SOP adds quarterly cadence |
| `github-repo-curator` | `SOP--repo-onboarding-and-habitat-creation` | SOP adds registry/seed.yaml |
| `research-synthesis-workflow` | `SOP--research-to-implementation-pipeline` | SOP adds ORGANVM routing |
| `incident-response-commander` | `SOP--cicd-resilience-and-recovery` | SOP adds soak patterns |
| `doc-coauthoring` | `SOP--essay-publishing-and-distribution` | SOP adds POSSE pipeline |
| `ontological-renamer` | `SOP--ontological-renaming` | SOP adds registry/seed.yaml propagation |
| `multi-agent-workforce-planner` | `SOP--agent-seeding-and-workforce-planning` | SOP adds ORGANVM workstream patterns |
| `project-orchestration` | `SOP--planning-and-roadmapping` | SOP adds there-and-back-again methodology |
| `github-repository-standards` | `SOP--readme-and-documentation` | SOP adds portfolio-standard README |
| `systemic-product-analyst` | `SOP--business-organism-design` | SOP adds phased activation model |

### Lifecycle Phase Model

Directives can declare a `phase` to indicate when in the repo lifecycle they become relevant. The phase maps directly to the promotion state machine:

| Phase | Promotion State | When | Core Directives |
|-------|----------------|------|-----------------|
| `genesis` | (pre-LOCAL) | Project creation | github-repository-standards, github-repo-curator, repo-onboarding, ontological-renaming, planning-and-roadmapping, business-organism-design |
| `foundation` | LOCAL | Initial development | testing-patterns, tdd-workflow, security-threat-modeler, coding-standards-enforcer, readme-and-documentation, agent-seeding-and-workforce-planning |
| `hardening` | CANDIDATE | Preparing for public | verification-loop, deployment-cicd, accessibility-patterns, security-implementation-guide, completeness-verification |
| `graduation` | PUBLIC_PROCESS → GRADUATED | Public maturity | stranger-test-protocol, doc-coauthoring, structural-integrity-audit |
| `sustaining` | GRADUATED | Ongoing maintenance | incident-response-commander, evaluation-to-growth, cicd-resilience |
| `any` | (all states) | Always applicable | session-self-critique, cli-module-pattern |

**Backward-compatible:** `phase` defaults to `any` when absent — existing SOPs/skills work unchanged.

Frontmatter extension:

```yaml
---
sop: true
name: registry-update-protocol
scope: repo
phase: foundation          # genesis | foundation | hardening | graduation | sustaining | any
triggers:
  - context:registry-edit
complements: []
overrides: null
---
```

**Phase-aware resolution:** `organvm sop resolve --phase hardening` returns only directives matching that phase (or `any`). Context sync auto-resolves the phase from each repo's `promotion_status` in the registry.

**Genesis DNA:** The `SOP--genesis-dna.md` defines the minimum viable repo structure and linked skills that fire at project creation (phase: genesis). It is the structural genome that all downstream SOPs depend on.

### .sops/ Directories

Files in `.sops/` are self-declaring SOP-skills — any `.md` file in a `.sops/` directory is automatically discovered by `organvm sop discover` regardless of filename prefix. No inventory entry needed.

Seed examples:
- `meta-organvm/.sops/submodule-sync-protocol.md` — T3 organ-level directive for all META repos
- `meta-organvm/.sops/commit-and-release-workflow.md` — T3 commit/push/release protocol
- `meta-organvm/.sops/session-state-management.md` — T3 session state preservation directive
- `meta-organvm/organvm-engine/.sops/cli-module-pattern.md` — T4 repo-level directive for adding CLI commands
- `meta-organvm/organvm-corpvs-testamentvm/.sops/registry-update-protocol.md` — T4 repo-level directive for safe registry editing

### Context Integration

Resolved directives are injected into auto-generated CLAUDE.md sections via `organvm context sync`:

```markdown
## Active Directives

| Scope | Name | Description |
|-------|------|-------------|
| repo | cli-module-pattern | How to add CLI command groups to the engine |
| organ | submodule-sync-protocol | Submodule pointer sync for META repos |
| system | structural-integrity-audit | Quality gate at promotion milestones |

Linked skills: verification-loop, deployment-cicd
```

### CLI Commands

```bash
organvm sop discover [--json] [--organ X]   # Show all SOPs including .sops/ files
organvm sop resolve <name> [--repo X] [--organ X]   # Show active SOP for context
organvm sop init --scope repo|organ [--name <name>]   # Scaffold .sops/ dir + template
```

---

## 11. Dual-Level Output Doctrine

Every SOP execution produces two artifacts:

1. **The Direct Output** — what the SOP was designed to create (audit report, deployment, essay, pipeline result)
2. **The Consulting Clone** — a reproducible, client-facing version of that output (case study, methodology deck, deliverable template, engagement report)

The consulting clone is not an afterthought. It is designed into the action from the start. When executing any SOP, the operator must ask: **"What is the Level 2 output? Who would pay for this?"**

### Mapping

The `consulting-services-manifest.md` (in `organvm-corpvs-testamentvm/docs/strategy/`) maps each SOP to its consulting package, target client profile, and deliverable format. Every new SOP added to the ecosystem must have a corresponding entry in the manifest.

### Examples

| SOP | Direct Output (Level 1) | Consulting Clone (Level 2) |
|-----|------------------------|---------------------------|
| structural-integrity-audit | Internal audit report | "Marrow Report" for pre-due-diligence clients |
| stranger-test-protocol | Navigation audit log | Legibility score + UX recommendations deck |
| product-deployment-and-revenue-activation | Deployed product | Case study + deployment runbook for "almost finished" products |
| session-self-critique | Session review scaffold | AI-governance methodology documentation |

### Revenue Pathway

This doctrine operationalizes principle E2 (Dual-Level Production) from `praxis-perpetua/lessons/derived-principles.md`. The revenue pathway for every SOP execution is `consulting-service` — the methodology itself is the product.

---

*Version: 2.1.0 | System-Wide Directive | ORGANVM*
