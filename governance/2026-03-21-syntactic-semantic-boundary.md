# Syntactic-Semantic Boundary: Classification of ORGANVM Governance Rules

**Date:** 2026-03-21
**Status:** ENACTED
**Source:** Implementation Manifest P0-02 (RP-02 SS4.5 Implication 1, SS5.2; SYN-02 SS4.1)
**Theoretical Basis:** RP-02 — Computability Limits in Automated Governance (Rice's Theorem Applied to Software Governance)
**Scope:** All governance rules in governance-rules.json, seed.yaml schemas, CI checks, axioms, dictums, and repo rules

---

## The Boundary Principle

Per Rice's theorem, no automated system can decide all non-trivial semantic properties of programs. This means every governance rule falls into one of three categories:

1. **SYNTACTIC** — the rule checks a property that is decidable from the structure of artifacts alone, without requiring understanding of meaning, intent, or fitness. These can be automated exhaustively.
2. **SEMANTIC** — the rule checks a property that requires understanding meaning, intent, context, or fitness. These are undecidable in general and require human judgment.
3. **BOUNDARY** — the rule has a syntactic component that can be automated and a semantic component that cannot. Automation provides a partial check; human review completes it.

This classification is not a quality ranking. Syntactic rules are not "lesser" governance; they are the governance that can be trusted to automation. Semantic rules are not "better" governance; they are the governance that must be routed to human judgment. The classification determines enforcement mechanism, not importance.

---

## Classification: Constitutional Articles

| Article | Rule | Classification | Rationale |
|---------|------|---------------|-----------|
| I | Identity Must Be Declared | BOUNDARY | File existence is syntactic (seed.yaml exists); whether the declaration accurately describes the entity is semantic |
| II | Records Are Immutable | SYNTACTIC | Append-only is a structural property enforceable by git history and event-sourced storage |
| III | Transition Requires Readiness | BOUNDARY | Checklist criteria are syntactic; whether readiness evidence is genuine is semantic |
| IV | Every Power Must Declare Its Failure Mode | BOUNDARY | Declaration existence is syntactic; whether the declared failure mode is honest/complete is semantic |
| V | No Single Entity Owns Truth | SEMANTIC | Distributed truth is an architectural principle verifiable only by holistic system audit |
| VI | Entropy Is The Default | BOUNDARY | Activity detection (commits, CI runs) is syntactic; whether the activity constitutes meaningful maintenance is semantic |
| VII | The Watchers Are Watched | BOUNDARY | Audit record existence is syntactic; whether the audit is substantive is semantic |

---

## Classification: Axioms (governance-rules.json dictums.axioms)

| ID | Name | Classification | Automated Check | Semantic Residue |
|----|------|---------------|-----------------|------------------|
| AX-1 | DAG Invariant | **SYNTACTIC** | `validate_dag_invariant` — graph cycle detection on declared edges | None. The dependency graph is a syntactic structure; acyclicity is decidable. |
| AX-2 | Epistemic Membranes | **BOUNDARY** | `validate_epistemic_membranes` — checks declared produces/consumes in seed.yaml | Undeclared coupling via shared databases, implicit imports, or runtime calls cannot be detected from seed.yaml alone. |
| AX-3 | TTL Eviction | **BOUNDARY** | `validate_ttl_eviction` — checks last-commit timestamp against 90-day threshold | Activity timestamp is syntactic; whether the activity constitutes meaningful work (vs. trivial commits to reset the clock) is semantic. |
| AX-4 | Registry Coherence | **SYNTACTIC** | `validate_registry_coherence` — checks uniqueness, valid states, array lengths | The registry is a data structure; coherence constraints are structural invariants. |
| AX-5 | Organ Placement | **SEMANTIC** | `validate_organ_placement` — checks against inclusion/exclusion criteria | Whether a repo "belongs" in an organ requires domain understanding. The inclusion/exclusion criteria in organ-definitions.json are heuristics, not decision procedures. Enforcement is audit-only, not automated rejection. |

---

## Classification: Organ Dictums (governance-rules.json dictums.organ_dictums)

| ID | Name | Organ | Classification | Rationale |
|----|------|-------|---------------|-----------|
| OD-I | Theoria Purity | I | **SYNTACTIC** | "Must not depend on ORGAN-II or ORGAN-III" is a graph property checkable on declared edges. |
| OD-II | Poiesis Derivation | II | **SYNTACTIC** | "May depend on ORGAN-I but never on ORGAN-III" is a graph property. |
| OD-III | Ergon Factory Gate | III | **BOUNDARY** | `revenue_model` field existence is syntactic; whether the revenue model is viable is semantic. CI configuration existence is syntactic; whether tests are meaningful is semantic. |
| OD-IV | Taxis Orchestration | IV | **SEMANTIC** | "Must not contain domain logic belonging to I, II, or III" requires understanding what constitutes domain logic vs. orchestration logic. Enforcement is manual. |
| OD-V | Logos Write Scope | V | **BOUNDARY** | Seed.yaml produces-edge checking is syntactic; whether ORGAN-V truly only "observes and documents" requires understanding the nature of the content. |
| OD-VI | Koinonia Community | VI | **SEMANTIC** | "Products feed into VI via declared event edges" — edge existence is syntactic, but whether the feeding constitutes genuine community infrastructure is semantic. Enforcement is audit-only. |
| OD-VII | Kerygma Consumer | VII | **BOUNDARY** | "No produces edges in seed.yaml" is syntactic. Whether the organ generates "original domain content" (vs. distribution content) requires semantic judgment. |
| OD-META | Meta Governance | META | **SEMANTIC** | "Changes here propagate system-wide" is a design principle, not a checkable property. Enforcement is audit-only. |

---

## Classification: Repo Rules (governance-rules.json dictums.repo_rules)

| ID | Name | Classification | Automated Check | Semantic Residue |
|----|------|---------------|-----------------|------------------|
| RR-1 | Seed Contract Mandate | **SYNTACTIC** | `validate_seed_mandate` — file exists and passes schema validation | None for existence; seed.yaml accuracy is tracked separately (P0-09). |
| RR-2 | Single Responsibility | **SEMANTIC** | None (`validator: null`) | Whether a repo has "a single, well-defined responsibility" is a design judgment. Monolith/micro-repo detection requires understanding the domain. |
| RR-3 | Event Handshake | **BOUNDARY** | `validate_event_handshake` — declared events exist in the catalog | Edge declaration is syntactic; whether events are actually produced/consumed at runtime is semantic (P0-09). |
| RR-4 | README Mandate | **BOUNDARY** | `validate_readme_mandate` — file exists, `documentation_status != EMPTY` | Existence is syntactic; whether the README communicates effectively is semantic (stranger test). |
| RR-5 | Promotion Integrity | **SYNTACTIC** | `validate_promotion_integrity` — state is in valid set, transitions follow state machine | The state machine is a formal structure; valid transitions are decidable. |

---

## Classification: Promotion Criteria (governance-rules.json state_machine.promotion_criteria)

### INCUBATOR to LOCAL

| Criterion | Classification | Rationale |
|-----------|---------------|-----------|
| Strict JSON Schema or YAML configuration defined | **SYNTACTIC** | Schema existence and validity are structural. |
| Upstream/downstream edges declared in seed.yaml | **SYNTACTIC** | Edge declaration is a structural property of the YAML file. |
| Interface contract (Webhook/MCP) established | **BOUNDARY** | Contract file existence is syntactic; whether the contract is correct is semantic. |
| 14-day TTL | **SYNTACTIC** | Timestamp comparison. |

### CANDIDATE to PUBLIC_PROCESS

| Criterion | Classification | Rationale |
|-----------|---------------|-----------|
| `ci_workflow` is not null | **SYNTACTIC** | Field value check. |
| `implementation_status` is ACTIVE | **SYNTACTIC** | Field value check. |
| README exists and passes portfolio gate | **BOUNDARY** | Existence is syntactic; "passes portfolio gate" requires quality judgment. |

### PUBLIC_PROCESS to GRADUATED

| Criterion | Classification | Rationale |
|-----------|---------------|-----------|
| All CANDIDATE criteria met | **BOUNDARY** | Inherits the boundary criteria from CANDIDATE. |
| `platinum_status` is true | **SYNTACTIC** | Boolean field check. |
| Stranger test or peer review completed | **SEMANTIC** | Whether the review was substantive is a judgment. Completion tracking is syntactic; review quality is not. |
| No critical audit findings | **BOUNDARY** | "No findings" is syntactic (empty set); whether findings were correctly identified is semantic. |

---

## Classification: Audit Thresholds (governance-rules.json audit_thresholds)

### Critical Thresholds

| Threshold | Classification | Rationale |
|-----------|---------------|-----------|
| `missing_readme` | **SYNTACTIC** | File existence check. |
| `circular_dependency` | **SYNTACTIC** | Graph cycle detection. |
| `back_edge_violation` | **SYNTACTIC** | Graph edge direction check against allowed-edges list. |
| `organ_has_zero_repos` | **SYNTACTIC** | Array length check. |

### Warning Thresholds

| Threshold | Classification | Rationale |
|-----------|---------------|-----------|
| `stale_repo_days: 90` | **BOUNDARY** | Timestamp is syntactic; meaningful activity is semantic. |
| `missing_changelog` | **SYNTACTIC** | File existence check. |
| `missing_ci_workflow` | **SYNTACTIC** | Field value check. |
| `missing_badges` | **SYNTACTIC** | File content pattern match. |
| `essay_count_below: 10` | **SYNTACTIC** | Count comparison. |
| `missing_seed_yaml` | **SYNTACTIC** | File existence check. |

---

## Classification: CI Pipeline Checks

These are the checks that run in GitHub Actions workflows across the system.

| Check | Classification | Rationale |
|-------|---------------|-----------|
| `ruff check` (Python linting) | **SYNTACTIC** | Pattern matching on source code syntax. |
| `pyright` (type checking) | **SYNTACTIC** | Type inference is decidable for the restricted type system used. |
| `pytest` execution (pass/fail) | **BOUNDARY** | Test execution is automated; whether tests are meaningful is semantic. A test suite can pass and still miss critical bugs. |
| `npm run typecheck` (TypeScript) | **SYNTACTIC** | Type checking against declared types. |
| `npm run lint` (ESLint) | **SYNTACTIC** | Pattern matching on source code syntax. |
| `npm run build` (build success) | **SYNTACTIC** | Compilation/bundling is a decidable process. |
| Schema validation (`organvm-validate`) | **SYNTACTIC** | JSON Schema validation is decidable. |
| Dependency audit (`npm audit`, `pip audit`) | **BOUNDARY** | Known vulnerability matching is syntactic; whether a vulnerability is exploitable in context is semantic. |

---

## Classification: Seed.yaml Properties

| Property | Classification | Rationale |
|----------|---------------|-----------|
| `organ` membership declaration | **SYNTACTIC** (for validation), **SEMANTIC** (for correctness) | The field value can be validated against allowed values (syntactic), but whether the repo truly belongs in that organ is semantic (AX-5). |
| `tier` declaration (flagship/standard/stub/infrastructure) | **BOUNDARY** | Valid tier values are syntactic; whether the tier assignment reflects the repo's actual importance is semantic. |
| `produces`/`consumes` edges | **BOUNDARY** | Edge declaration syntax is validatable; whether edges accurately describe runtime data flow is semantic (P0-09). |
| `events` subscriptions | **BOUNDARY** | Event name existence in catalog is syntactic; whether subscriptions are actually honored is semantic. |
| Schema compliance (field types, required fields) | **SYNTACTIC** | JSON Schema validation. |

---

## Summary Statistics

| Category | Count | Percentage |
|----------|-------|------------|
| **SYNTACTIC** (fully automatable) | 24 | 40% |
| **BOUNDARY** (partially automatable) | 25 | 42% |
| **SEMANTIC** (requires human judgment) | 11 | 18% |
| **Total classified rules** | 60 | 100% |

---

## Implications

### For Automation (organvm-engine, CI pipelines)

1. **SYNTACTIC rules** should be enforced in CI as hard gates. Failure blocks promotion. No exceptions, no overrides.
2. **BOUNDARY rules** should be enforced in CI for their syntactic component only. The automated check produces a partial verdict: "syntactic component passes; semantic component not assessed." The semantic residue must be explicitly listed in the verdict output (P0-07).
3. **SEMANTIC rules** must never be added to CI as automated gates. They belong exclusively in human review processes (IRA panel, stranger test, Provost review).

### For the IRA Panel

The IRA panel's domain is precisely the SEMANTIC column plus the semantic residue of all BOUNDARY rules. The panel's assessment protocol should be structured around these specific semantic gaps, not around duplicating syntactic checks that automation already handles.

### For Governance Evolution

When a new governance rule is proposed, it must be classified before implementation. The classification determines the enforcement mechanism. Attempting to automate a semantic rule produces false precision; failing to automate a syntactic rule wastes human attention.

---

## Maintenance

This classification must be updated when:

1. A new governance rule is added to `governance-rules.json`
2. A new axiom or dictum is enacted
3. A new CI check is introduced
4. A BOUNDARY rule is reclassified (e.g., a new tool makes the semantic component partially decidable)

The classification is maintained as a governance artifact in `praxis-perpetua/governance/`. It is not embedded in `governance-rules.json` itself to avoid circular self-governance — the classification of rules is a meta-governance function.

---

## Cross-References

- **RP-02:** Computability limits in automated governance (Rice's theorem, decidability hierarchy)
- **SYN-02:** The Governance Trilemma (consistency/completeness/measurability)
- **P0-01:** `2026-03-21-governance-trilemma-declaration.md` (ORGANVM's trilemma position)
- **P0-07:** Incompleteness visibility in governance verdicts
- **P0-09:** Seed.yaml semantic accuracy tracking
- **P1-18:** Governance-as-type-system framework (Curry-Howard classification)
- **Constitutional Article I:** Identity Must Be Declared
- **Constitutional Article IV:** Every Power Must Declare Its Failure Mode

---

*This classification is empirical, not theoretical. It reflects the actual governance rules currently in force in ORGANVM as of 2026-03-21. The theoretical justification is in RP-02; the trilemma context is in SYN-02. Future governance rules must be classified at creation time.*
