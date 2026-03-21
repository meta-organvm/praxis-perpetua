# Governance Trilemma Declaration

**Date:** 2026-03-21
**Status:** ENACTED
**Source:** Implementation Manifest P0-01 (SYN-02 SS5.5 Recommendation 1; TRP-SYN-02 POV-3)
**Theoretical Basis:** SYN-02 — The Governance Trilemma: Consistency, Completeness, and Measurability in Automated Software Governance
**Scope:** System-wide — all organs, all governance artifacts, all automated checks

---

## The Trilemma

Any automated governance system must choose at most two of three properties:

1. **Consistency** — governance rules produce the same verdict for the same input, regardless of evaluator or context
2. **Completeness** — every property relevant to quality is assessed; no blind spots exist
3. **Measurability** — governance verdicts are derived from observable, quantifiable indicators that can be automated

No system achieves all three simultaneously. The choice is structural, not a failure of implementation.

---

## ORGANVM's Position: Consistent + Measurable

ORGANVM explicitly chooses **Consistency and Measurability**, accepting **Incompleteness** as the structural cost.

### Why This Position

- **Consistency** is non-negotiable for a single-practitioner system. If governance rules produce different verdicts depending on which AI agent executes them, or which session runs the check, the system becomes ungovernable. A solo operator cannot arbitrate inconsistent automated judgments at scale.
- **Measurability** is non-negotiable for an AI-conductor model. The human directs; automation generates volume. If governance cannot be automated through observable indicators, the human becomes the bottleneck — defeating the entire amplification premise.
- **Incompleteness** is therefore the accepted cost. The governance system does not assess everything that matters. It assesses everything it can assess consistently and measurably, and it explicitly declares what it cannot assess.

### What This Means in Practice

The governance system will always have blind spots. Properties that require judgment, context, or semantic understanding are outside the automated governance boundary. This is not a deficiency to be fixed — it is a structural reality to be managed.

---

## What IS Governed (Syntactic Properties)

These properties are consistently decidable and measurably automatable. The governance system enforces them exhaustively.

| Property | Enforcement | Validator |
|----------|-------------|-----------|
| File existence (README, seed.yaml, CHANGELOG) | CI + `organvm governance audit` | `validate_readme_mandate`, `validate_seed_mandate` |
| Schema validation (seed.yaml, registry-v2.json) | CI + `organvm-validate` | JSON Schema validators in `schema-definitions/` |
| Naming convention compliance (double-hyphen pattern) | CI + naming linter (P0-05) | See `2026-03-21-naming-convention-spec.md` |
| Dependency graph acyclicity (DAG invariant) | CI + `organvm governance check-deps` | `validate_dag_invariant` (AX-1) |
| Promotion state machine integrity | CI + `organvm governance promote` | `validate_promotion_integrity` (RR-5) |
| CI pipeline pass/fail | GitHub Actions | Per-repo workflow files |
| Test existence and execution | CI + pytest/vitest | Per-repo test suites |
| Registry coherence (no duplicates, valid states) | `organvm registry validate` | `validate_registry_coherence` (AX-4) |
| Stale repository detection (90-day TTL) | `organvm governance audit` | `validate_ttl_eviction` (AX-3) |
| Cross-organ edge declaration (epistemic membranes) | `organvm seed graph` | `validate_epistemic_membranes` (AX-2) |
| Event handshake (declared events exist in catalog) | `organvm governance audit` | `validate_event_handshake` (RR-3) |

---

## What is NOT Governed (Semantic Properties)

These properties require human judgment and cannot be reduced to consistent, measurable checks. Per Rice's theorem (RP-02), no automated system can decide non-trivial semantic properties of programs in general. The governance system does not pretend to assess these.

| Property | Why It Cannot Be Automated | Who Assesses It |
|----------|---------------------------|-----------------|
| Code quality (beyond lint/format) | Requires understanding intent, context, and trade-offs | Human review, IRA panel |
| Architectural fitness | Whether the architecture serves its purpose is a judgment call | IRA panel, Provost |
| Readiness for promotion (beyond checklist) | "Ready" is a construct that exceeds its operationalization (P0-03) | IRA panel defense |
| Innovation value | Whether work contributes novel insight has no decidable metric | Human judgment |
| Ethical alignment | Value judgments resist formalization | Provost, Constitutional review |
| Documentation adequacy (beyond existence) | A README can exist and be useless; quality is semantic | Stranger test, peer review |
| Naming appropriateness (beyond pattern) | A name can match the regex and still mislead | Human review |
| Fitness for organ placement | Whether a repo truly belongs in its organ requires domain understanding | IRA panel (AX-5 is audit-only) |
| Contribution to system mission | Whether work advances the North Star is a strategic judgment | Provost |
| Detection of Goodhart-corrupted metrics | When a metric stops measuring what it claims to measure | IRA panel, metric rotation (P1-02) |

---

## What Bridges the Gap

The gap between what is governed and what matters is not unmanaged. Three mechanisms bridge it:

### 1. The IRA Panel (Inter-Rater Agreement)

The multi-model evaluative consensus panel is the primary bridge. It operates as ORGANVM's Tarskian escape — the meta-level system that can reason about properties the object-level governance cannot assess. The IRA panel:

- Assesses semantic properties during promotion defenses
- Provides structured disagreement as governance signal (not noise)
- Uses psychometric inter-rater agreement (ICC, kappa) to measure whether its own assessments are reliable
- Is structurally necessary because of impossibility results (Godel, Rice, Arrow), not merely a quality assurance convenience

See: `governance/defense-protocol.yaml`, `governance/faculty-registry.yaml`

### 2. Human Review Gates

Every promotion transition includes a human review gate. The AI-conductor model means automation handles throughput, but humans retain judgment at every decision point that involves semantic properties. Specific gates:

- **Promotion defenses** — no repo advances past PUBLIC_PROCESS without human-verified IRA panel assessment
- **Stranger test** — an external perspective assesses documentation adequacy (semantic, not syntactic)
- **Provost review** — the human operator reviews all Dissertation-tier work and strategic decisions
- **Session review protocol** — session self-critique logs capture what automation missed

### 3. The Thesis Review Protocol (TRP)

The TRP provides structured external criticism of SGO academic work. Three independent points of view assess each thesis, identifying blind spots, unstated assumptions, and missed implications. The TRP specifically surfaces properties that the automated governance system cannot assess — making incompleteness visible and actionable.

See: `governance/senate-config.yaml`, SGO defense infrastructure

---

## The Blind-Spot Registry

Per P0-01, ORGANVM maintains an explicit registry of governance blind spots — properties that the governance system does not assess. This registry is not a TODO list of things to automate; many of these properties are structurally undecidable. It is a declaration of known incompleteness.

### Declared Blind Spots

| ID | Blind Spot | Category | Mitigation |
|----|-----------|----------|------------|
| BS-01 | Code quality beyond lint rules | Semantic | IRA panel review during promotion |
| BS-02 | Whether seed.yaml declarations match runtime behavior | Semantic | Runtime analysis as under-approximation (P0-09) |
| BS-03 | Whether test coverage reflects meaningful testing (vs. trivial tests) | Semantic | IRA panel + constitutive value assessment (P1-24) |
| BS-04 | Whether documentation communicates effectively | Semantic | Stranger test protocol |
| BS-05 | Whether architectural decisions serve the organ mission | Semantic | IRA panel with domain-specific rubrics |
| BS-06 | Whether metrics still measure what they claim to measure | Meta-governance | Goodhart monitoring (P1-02), metric rotation |
| BS-07 | Whether governance rules are interpreted consistently by AI agents | Translation drift | Monitoring + rule clarification (P1-21) |
| BS-08 | Whether the governance system itself is well-governed | Self-reference | Vigiles Aeternae (Constitutional Article VII: The Watchers Are Watched) |
| BS-09 | Whether promotion criteria at each level are correctly specified | Construct validity | Factor analysis (P0-04), Guttman scale validation (P1-13) |
| BS-10 | Whether organ placement is correct for borderline repos | Domain judgment | IRA panel with organ-specific inclusion/exclusion criteria (AX-5) |

---

## Obligations

This declaration creates the following obligations:

1. **Every automated governance verdict** must include an explicit scope statement: what was checked, and what was not checked. (Implements P0-07.)
2. **The blind-spot registry** must be maintained as a living document. New blind spots are added as they are discovered; blind spots are never removed, only reclassified if a reliable automated check is developed.
3. **No semantic property** may be added to automated CI checks without review by the IRA panel to confirm that the proposed check is genuinely decidable and does not merely approximate a semantic judgment.
4. **The trilemma position** must be re-evaluated annually or when the system undergoes a major architectural change. The current position (Consistent + Measurable) is appropriate for ORGANVM's current scale and operational model; it is not permanently fixed.

---

## Cross-References

- **SYN-02:** The Governance Trilemma (theoretical foundation)
- **RP-02:** Computability and governance (Rice's theorem, Godel's incompleteness)
- **P0-02:** `2026-03-21-syntactic-semantic-boundary.md` (rule classification)
- **P0-07:** Incompleteness visibility in governance verdicts
- **P0-08:** IRA panel protocol formalization
- **Constitutional Article IV:** Every Power Must Declare Its Failure Mode
- **Constitutional Article V:** No Single Entity Owns Truth
- **Constitutional Article VII:** The Watchers Are Watched

---

*This document is a governance declaration, not a research paper. It records a structural choice and its consequences. The theoretical justification is in SYN-02; the operational implementation follows from P0-02 through P0-09.*
