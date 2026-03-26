---
status: reference-activated
---
# SGO Research Programme -- ORGANVM Implementation Manifest

**Generated:** 2026-03-20
**Source:** 12 papers + 3 TRP reviews across 4 research phases
**Scope:** Every actionable design recommendation extracted from the SGO research programme

---

## Summary Statistics

| Dimension | Count |
|-----------|-------|
| **Total tasks** | 74 |
| **P0 (Foundational)** | 14 |
| **P1 (Important)** | 32 |
| **P2 (Enhancement)** | 28 |
| **GOVERNANCE** | 22 |
| **MEASUREMENT** | 18 |
| **NAMING** | 11 |
| **ARCHITECTURE** | 12 |
| **TOOLING** | 7 |
| **PROCESS** | 4 |
| **Effort S (hours)** | 18 |
| **Effort M (days)** | 31 |
| **Effort L (weeks)** | 19 |
| **Effort XL (months)** | 6 |

---

## P0: Foundational Tasks

These must be done before other work can build on them. They establish the structural preconditions for the entire programme.

### P0-01: Make the Governance Trilemma choice explicit

- **Source:** SYN-02 SS5.5 Recommendation 1; TRP-SYN-02 POV-3
- **Recommendation:** Document ORGANVM's implicit choice of Consistent + Measurable over Complete. Create a machine-readable registry of governance blind spots -- properties that the governance system does not assess -- alongside the registry of properties it does assess.
- **Affected components:** META-ORGANVM governance corpus, ORGAN-IV governance-rules.json
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** None

### P0-02: Classify all governance rules as syntactic or semantic

- **Source:** RP-02 SS4.5 Implication 1, SS5.2; SYN-02 SS4.1
- **Recommendation:** Audit every governance rule in governance-rules.json, seed.yaml schemas, and CI checks. Explicitly classify each as syntactic (automatable, decidable) or semantic (requiring human judgment, undecidable per Rice's theorem). Maintain this classification as a machine-readable annotation.
- **Affected components:** ORGAN-IV governance-rules.json, all seed.yaml schemas, CI pipeline configs
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** None

### P0-03: Define "readiness" construct independently of its operationalization

- **Source:** RP-07 SS7 Implication 1; SYN-02 SS4.4; SYN-04 SS4.1
- **Recommendation:** Break the construct-operationalization circularity. Convene an expert panel to define the full domain of "repository readiness" independently of the metrics that measure it. Document what dimensions the construct encompasses (structural completeness, code quality, operational maturity, fitness for purpose, architectural coherence), what it excludes, and how the dimensions relate.
- **Affected components:** META-ORGANVM, ORGAN-IV orchestration
- **Category:** MEASUREMENT
- **Effort:** M (days)
- **Dependencies:** None

### P0-04: Conduct factor analysis on the omega scorecard

- **Source:** RP-07 SS6.2, SS6.3 Stage 2; SYN-02 SS5.5 Recommendation 2
- **Recommendation:** Perform exploratory factor analysis on all omega scorecard indicators across the repository population. Determine whether the indicators reflect a single latent construct or multiple distinct factors (structural completeness, code quality, operational readiness). If multidimensional, replace the single composite score with a multidimensional quality profile.
- **Affected components:** META-ORGANVM organvm-engine, system-metrics.json
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P0-03

### P0-05: Implement the naming convention validator (double-hyphen linter)

- **Source:** RP-04 SS5.1 Principle 6 (governance proportionality); SYN-03 SS6.4; RP-02 SS4.5 Implication 2
- **Recommendation:** Build an automated naming validator that enforces the double-hyphen convention. Validate: exactly one `--` separator, valid hyphenated words on each side, consistent formatting. Integrate into CI pipelines as a syntactic governance check. Since naming rules are syntactic properties, they can be enforced exhaustively per Rice's theorem.
- **Affected components:** ORGAN-IV CI tooling, all repos
- **Category:** NAMING
- **Effort:** M (days)
- **Dependencies:** None

### P0-06: Build a controlled vocabulary registry for domain terms

- **Source:** RP-04 SS5.1 Principle 4; SYN-03 SS6.4
- **Recommendation:** Create a machine-readable controlled vocabulary mapping canonical terms to their synonyms and specifying which terms are preferred across the system. Seed contracts (seed.yaml) should reference this vocabulary. Validate new names against the controlled vocabulary in CI.
- **Affected components:** META-ORGANVM governance corpus, seed.yaml schema
- **Category:** NAMING
- **Effort:** M (days)
- **Dependencies:** P0-05

### P0-07: Make incompleteness visible in all governance verdicts

- **Source:** RP-02 SS5.5 Principle; SYN-02 SS5.5 Recommendation 1
- **Recommendation:** Every automated governance verdict must include an explicit statement of scope: "This component passes all syntactic checks. The following semantic properties have not been verified and require human review: [list]." Display governance coverage as a dashboard metric alongside pass/fail results.
- **Affected components:** organvm-engine CLI output, dashboard, CI pipeline output
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P0-02

### P0-08: Formalize the IRA panel protocol

- **Source:** RP-02 SS6.3; SYN-02 SS4.5, SS5.3, SS5.5 Recommendation 5
- **Recommendation:** Strengthen the IRA panel as the Tarskian escape. Provide explicit guidance on semantic properties that automated checks cannot assess: fitness for purpose, architectural coherence, contribution to organ mission, ethical alignment, detection of Goodhart-corrupted metrics. Document why the panel is structurally necessary (impossibility results), not merely a quality assurance convenience.
- **Affected components:** ORGAN-IV governance documentation, IRA panel SOP
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P0-02

### P0-09: Implement seed.yaml semantic accuracy tracking

- **Source:** RP-02 SS6.2, SS6.4; SYN-02 SS5.4
- **Recommendation:** Maintain a machine-readable registry of "properties not covered by seed.yaml validation." Track the gap between declared dependencies/events in seed.yaml and actual runtime behavior. Since this gap is a semantic property (Rice's theorem), use runtime analysis as an under-approximation and flag discrepancies for human review.
- **Affected components:** organvm-engine, seed.yaml validation, CI pipeline
- **Category:** GOVERNANCE
- **Effort:** L (weeks)
- **Dependencies:** P0-02

### P0-10: Separate self-maintenance from self-improvement in governance

- **Source:** RP-02 SS5.7; SS6.4
- **Recommendation:** Build two distinct operational modes. Self-maintenance mode runs continuously: monitoring system health, test pass rates, metric ranges, dependency integrity, correcting deviations automatically. Self-improvement mode is triggered by human decision: changes to governance rules, semantic objectives, or architectural structure require human review and approval. Enforce the boundary architecturally.
- **Affected components:** ORGAN-IV orchestration, META-ORGANVM governance
- **Category:** ARCHITECTURE
- **Effort:** L (weeks)
- **Dependencies:** P0-02, P0-08

### P0-11: Establish the hybrid topology principle as architectural law

- **Source:** RP-03 SS6.1-6.4; SYN-02 SS4.2
- **Recommendation:** Codify: inter-organ dependency flow is strictly hierarchical (I->II->III, enforced by validate-deps.py). Intra-organ connectivity is rhizomatic (any repo can depend on any other within an organ). Cross-organ communication via event schemas only. Registry provides legibility-without-hierarchy. Document this as the compression/search principle applied to ORGANVM.
- **Affected components:** ORGAN-IV governance-rules.json, CLAUDE.md files, architectural documentation
- **Category:** ARCHITECTURE
- **Effort:** S (hours)
- **Dependencies:** None

### P0-12: Design governance artifacts as boundary objects

- **Source:** RP-05 SS4.3, SS7.1; SYN-02 SS4.3; SYN-03 SS5.1-5.3
- **Recommendation:** Redesign seed.yaml, CLAUDE.md, and governance-rules.json as boundary objects that explicitly accommodate multiple interpretive communities (human operators, AI assistants, CI/CD pipelines, dashboards). Each artifact should be human-readable (for governance), machine-parseable (for automation), and AI-interpretable (for coding assistants) simultaneously.
- **Affected components:** All seed.yaml files, all CLAUDE.md files, governance-rules.json
- **Category:** ARCHITECTURE
- **Effort:** M (days)
- **Dependencies:** None

### P0-13: Implement temporal staging for governance validation

- **Source:** RP-02 SS5.1, SS6.1; SYN-02 SS4.1, SS5.2
- **Recommendation:** Ensure the governance system always validates the previous state using the current state, never the current state using itself. Each promotion transition must validate using criteria established at the prior state. Enforce that the validator and the validated come from different temporal stages. Document this as the bootstrapping principle.
- **Affected components:** ORGAN-IV promotion state machine, organvm-engine
- **Category:** GOVERNANCE
- **Effort:** S (hours)
- **Dependencies:** None

### P0-14: Implement context-specific governance norms

- **Source:** RP-07 SS5.5, SS7 Implication 4; SYN-02 SS5.5 Recommendation 3; SYN-04 SS5.2
- **Recommendation:** Do not apply uniform thresholds across heterogeneous repositories. At minimum, differentiate by: organ (ORGAN-I Python theory vs. ORGAN-III TypeScript products), programming language, and project type (library vs. CLI vs. web app). Until measurement invariance testing is feasible, use expert-determined context-specific norms.
- **Affected components:** organvm-engine scoring, promotion criteria, governance-rules.json
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P0-03, P0-04

---

## P1: Important Tasks

High-impact tasks with clear value. Should be prioritized after P0 foundations are in place.

### P1-01: Implement IRT-based scoring for governance checks

- **Source:** RP-07 SS5.1-5.4, SS6.3 Stage 3; SYN-02 SS4.4
- **Recommendation:** Fit a 2PL IRT model to pass/fail data for all governance checks. Estimate difficulty (b) and discrimination (a) parameters for each check. Weight checks by information content rather than treating all as equal. Assign checks to promotion levels based on empirical difficulty, not face validity.
- **Affected components:** organvm-engine scoring algorithm, promotion criteria
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P0-04

### P1-02: Implement Goodhart monitoring system

- **Source:** RP-07 SS7 Implication 7; SYN-02 SS5.4, SS5.5 Recommendation 4; SYN-04 SS5.3
- **Recommendation:** Track the correlation between governance metrics and external outcomes (production incidents, peer assessment quality, deployment success) over time. When correlation declines, flag the metric for recalibration. Implement periodic metric rotation to reduce gaming stability. Track IRT discrimination parameters over time: declining discrimination signals Goodhart corruption.
- **Affected components:** organvm-engine, system-metrics.json, dashboard
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P1-01

### P1-03: Report governance scores with confidence intervals

- **Source:** RP-07 SS6.4, SS7 Implication (error quantification); SYN-02 SS4.4
- **Recommendation:** Use CTT formula SEM = sigma_X * sqrt(1 - r_XX) as minimum. Report uncertainty alongside every score. Governance decisions near promotion thresholds should be acknowledged as uncertain. Provide a mechanism for handling borderline cases.
- **Affected components:** organvm-engine score output, dashboard
- **Category:** MEASUREMENT
- **Effort:** M (days)
- **Dependencies:** P0-04

### P1-04: Build a Governance Trilemma Audit instrument

- **Source:** SYN-02 SS6; TRP-SYN-02 POV-1 Expansion 2
- **Recommendation:** Create a formal audit methodology: (a) identify the system's declared trilemma position; (b) test actual behavior against declaration; (c) identify specific mechanisms by which each sacrificed property manifests; (d) assess whether sacrifice produces unmanaged risk. Apply to ORGANVM and document results.
- **Affected components:** ORGAN-IV governance documentation, META-ORGANVM
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P0-01

### P1-05: Create a Practitioner's Decision Matrix for trilemma positions

- **Source:** TRP-SYN-02 POV-3 Amendment; SYN-02 SS6
- **Recommendation:** Build a concrete table mapping governance contexts (early-stage, scaling, regulated, research, open-source, AI-augmented) to recommended trilemma positions with specific guidance on what "sacrificing" each horn looks like in practice.
- **Affected components:** ORGAN-IV governance documentation
- **Category:** GOVERNANCE
- **Effort:** S (hours)
- **Dependencies:** P0-01

### P1-06: Implement OPP-based governance architecture

- **Source:** RP-05 SS7.3; SYN-02 SS4.3
- **Recommendation:** Design explicit obligatory passage points at every critical juncture: before code is committed, before data is modified, before external APIs are called, before outputs are published. Each OPP is an opportunity for translation verification. Document the OPP map for the system.
- **Affected components:** All CI pipelines, git hooks, deployment workflows
- **Category:** ARCHITECTURE
- **Effort:** L (weeks)
- **Dependencies:** P0-02

### P1-07: Build the stigmergic infrastructure layer

- **Source:** RP-03 SS6.4 Heuristic 5; RP-03 SS7.2-7.3
- **Recommendation:** Invest in rich, persistent, searchable stigmergic substrates: knowledge graphs, version control metadata, the registry, dashboards, shared codebases. These enable lateral coordination without hierarchical intermediation. The registry-v2.json and dashboard are the existing foundation; extend them.
- **Affected components:** META-ORGANVM dashboard, registry, knowledge graph
- **Category:** TOOLING
- **Effort:** L (weeks)
- **Dependencies:** P0-11

### P1-08: Implement namespace governance proportional to scale

- **Source:** RP-04 SS5.1 Principle 3, Principle 6; SYN-03 SS6.5
- **Recommendation:** Formalize: who can create top-level names? What are the rules for naming within each namespace? How are violations detected and resolved? Who arbitrates disputes? Document namespace governance as part of ORGAN-IV's charter.
- **Affected components:** ORGAN-IV governance, naming documentation
- **Category:** NAMING
- **Effort:** S (hours)
- **Dependencies:** P0-05, P0-06

### P1-09: Track naming debt and implement naming health metrics

- **Source:** RP-04 SS5.3; SYN-03 SS3.4, SS6.2
- **Recommendation:** Create a mechanism to detect and track naming debt: names that no longer accurately describe what they name. Implement periodic naming audits. Track semantic drift: when implementations evolve but names do not, flag for review. A name stability metric should be part of the governance dashboard.
- **Affected components:** organvm-engine, dashboard, all repos
- **Category:** NAMING
- **Effort:** M (days)
- **Dependencies:** P0-05

### P1-10: Formalize the distinction between designed and emergent hierarchy

- **Source:** RP-03 SS4.4; SYN-02 SS2.2
- **Recommendation:** Monitor all flat/rhizomatic organizational domains for hub-and-spoke emergence (scale-free dynamics). When hubs emerge (certain repos or organs accumulating disproportionate dependencies or attention), make them explicit. Assign formal authority commensurate with informal influence. Track the centrality distribution of the dependency graph over time.
- **Affected components:** organvm-engine dependency analysis, dashboard, governance-rules.json
- **Category:** ARCHITECTURE
- **Effort:** M (days)
- **Dependencies:** P0-11

### P1-11: Build relational quality metrics (not just entity-level)

- **Source:** SYN-04 SS5.1
- **Recommendation:** Supplement entity-level metrics (coverage, complexity, lint score) with network-level metrics: dependency health as network position characterization, test quality as alignment between test structure and production use, documentation adequacy as communicative integration with users. Quality is a relational property, not an intrinsic one.
- **Affected components:** organvm-engine metrics system, system-metrics.json
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P0-04

### P1-12: Record network configuration alongside every assessment score

- **Source:** SYN-04 SS5.2
- **Recommendation:** Every governance score should be accompanied by: which tools (and versions) were used, which checks were applied (and at what thresholds), the repository's dependency network state, the development context. This metadata is constitutive of the score's meaning.
- **Affected components:** organvm-engine assessment output, system-metrics.json schema
- **Category:** MEASUREMENT
- **Effort:** M (days)
- **Dependencies:** P0-14

### P1-13: Implement the Guttman scale validation for the promotion pipeline

- **Source:** RP-07 SS4.1, SS6.3 Stage 1; SYN-02 SS5.2
- **Recommendation:** Conduct scalogram analysis on the promotion pipeline. Compute Guttman's coefficient of reproducibility. Test whether repositories in higher promotion states consistently exhibit properties required at lower states. Identify hard violations, soft violations, and structural violations. A CR below 0.90 indicates the promotion construct is misspecified.
- **Affected components:** organvm-engine analytics, promotion criteria
- **Category:** MEASUREMENT
- **Effort:** M (days)
- **Dependencies:** P0-04

### P1-14: Implement criterion validation for governance scores

- **Source:** RP-07 SS4.4, SS6.3 Stage 5, SS7 Implication 5
- **Recommendation:** Correlate governance scores with external outcomes: production incident rates, peer review assessments, deployment success, time-to-resolution for reported issues. Compute concurrent and predictive validity coefficients. Criterion validation must be ongoing, not one-time.
- **Affected components:** organvm-engine, system-metrics.json, external data integration
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P1-01

### P1-15: Adopt VSM recursive structure for organs

- **Source:** SYN-02 SS4.6, SS5.5 Recommendation 6; TRP-SYN-02 POV-1 Amendment
- **Recommendation:** Align each organ with Beer's five subsystems: System 1 (operations), System 2 (coordination), System 3 (control/resource optimization), System 4 (environmental intelligence), System 5 (identity/policy). ORGAN-IV functions as System 3/4 at the inter-organ level. Map VSM subsystems to trilemma properties: S3 manages measurability, S4 manages completeness boundary, S5 manages consistency.
- **Affected components:** ORGAN-IV architecture, all organ-level CLAUDE.md files
- **Category:** ARCHITECTURE
- **Effort:** L (weeks)
- **Dependencies:** P0-10, P0-11

### P1-16: Design system prompts as enrollment contracts, not command lists

- **Source:** RP-05 SS7.1
- **Recommendation:** Redesign all CLAUDE.md files and system prompts to define a role, establish a relationship, and specify conditions of productive collaboration -- not just list prohibitions. Treat the AI as a mediator to be enrolled, not an intermediary to be constrained.
- **Affected components:** All CLAUDE.md files, AI interaction protocols
- **Category:** PROCESS
- **Effort:** M (days)
- **Dependencies:** P0-12

### P1-17: Implement mediator visibility in AI-generated outputs

- **Source:** RP-05 SS7.2
- **Recommendation:** All AI-generated outputs should include: transparent attribution, indication of confidence/uncertainty, visible traces of the translation process (sources consulted, tools invoked, alternatives considered), and mechanisms for the user to inspect and challenge translations. Do not present the AI as an intermediary when it is a mediator.
- **Affected components:** All AI interaction tooling, commit message templates
- **Category:** PROCESS
- **Effort:** M (days)
- **Dependencies:** None

### P1-18: Build governance-as-type-system framework

- **Source:** RP-02 SS4.4, SS4.5 Implication 5; RP-06 SS7.4 (governance implications)
- **Recommendation:** Use the Curry-Howard framing to classify governance rules by type-theoretic strength. Rules expressible as simple types can be checked decidably. Rules requiring dependent types are undecidable and should be flagged for human review. This classifies rules by the Chomsky hierarchy: regular (finite checks), context-free (recursive structural checks), context-sensitive (context-dependent checks requiring semantic analysis).
- **Affected components:** ORGAN-IV governance framework, governance-rules.json
- **Category:** GOVERNANCE
- **Effort:** L (weeks)
- **Dependencies:** P0-02

### P1-19: Implement over/under-approximation strategy per governance rule

- **Source:** RP-02 SS4.3, SS5.4
- **Recommendation:** For each semantic governance rule, explicitly choose a direction of approximation. Conservative (over-approximate) for safety-critical properties: flag anything that might be a violation. Liberal (under-approximate) for non-critical properties: flag only definite violations. Document the direction and estimated error rate for each rule.
- **Affected components:** CI pipeline checks, governance-rules.json
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P0-02

### P1-20: Implement language-game specification for naming contexts

- **Source:** RP-04 SS5.1 Principle 7
- **Recommendation:** When designing naming conventions, specify the language game: where will this name appear (Git, Jira, changelog, metric label, dashboard, API)? Who will read it? What must they understand from the name alone? Different contexts may require different naming conventions for the same entities.
- **Affected components:** Naming documentation, ORGAN-IV governance
- **Category:** NAMING
- **Effort:** S (hours)
- **Dependencies:** P0-05

### P1-21: Design for translation drift in governance rules

- **Source:** SYN-02 SS4.3, SS5.5 Recommendation 7; RP-05 SS7.1
- **Recommendation:** Accept that governance rules will be interpreted differently by different actants. Monitor for excessive interpretation drift (where human understanding and AI interpretation diverge). Use monitoring as a signal for rule clarification, not rule rigidification. Build feedback loops as translation-maintenance mechanisms.
- **Affected components:** All governance artifacts, AI interaction monitoring
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P0-12

### P1-22: Implement the four-phase design audit

- **Source:** CAPSTONE SS11.6
- **Recommendation:** For each organ and major system, verify coverage across all four formalization phases: (1) Naming -- are terms well-defined? (2) Structuring -- is organizational topology appropriate? (3) Computing -- are formal validations in place? (4) Reflecting -- is self-assessment operational? Identify phase gaps and plan remediation.
- **Affected components:** All organs, META-ORGANVM
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P0-01

### P1-23: Build item analysis for governance checks

- **Source:** RP-07 SS6.3 Stage 1
- **Recommendation:** For each governance check, compute: pass rate across the repository population, point-biserial correlation between check result and total score (excluding that check). Checks with very high/low pass rates contribute little information. Checks with low correlations may measure a different construct. Remove or redesign non-discriminating checks.
- **Affected components:** organvm-engine analytics
- **Category:** MEASUREMENT
- **Effort:** M (days)
- **Dependencies:** P0-04

### P1-24: Design assessment criteria for constitutive value, not just diagnostic value

- **Source:** SYN-04 SS5.4
- **Recommendation:** Choose assessment criteria not only for their ability to distinguish quality levels (diagnostic value) but also for their ability to encourage desirable development practices (constitutive value). A check that has high discrimination but encourages harmful practices (e.g., trivial tests for coverage) is constitutively counterproductive. Optimize both simultaneously.
- **Affected components:** CI pipeline check design, governance-rules.json
- **Category:** MEASUREMENT
- **Effort:** M (days)
- **Dependencies:** P0-03, P1-01

### P1-25: Implement schema contracts as syntactic categories

- **Source:** SYN-01 SS6 (ORGANVM implications); CAPSTONE SS10.2
- **Recommendation:** Treat seed.yaml contracts as a formal syntactic category. Registry operations (validation, promotion, dependency checking) should be functorial: meaning-preserving transformations that respect the compositional structure of the schema. Implement schema validation as type-checking in the Curry-Howard sense.
- **Affected components:** organvm-engine schema validation, seed.yaml
- **Category:** TOOLING
- **Effort:** L (weeks)
- **Dependencies:** P0-09

### P1-26: Implement external case study of the Governance Trilemma

- **Source:** TRP-SYN-02 all POVs (A4)
- **Recommendation:** Apply the Governance Trilemma framework to at least one governance system not designed by the author (e.g., Linux kernel governance, GDPR enforcement, Kubernetes governance). Document findings. This demonstrates portability and addresses the self-referential case study limitation.
- **Affected components:** Research papers (SYN-02 revision)
- **Category:** PROCESS
- **Effort:** M (days)
- **Dependencies:** P0-01

### P1-27: Calibrate formality claims in SYN-02

- **Source:** TRP-SYN-02 A1, A2, A3
- **Recommendation:** Replace language presenting the Governance Trilemma as a formal theorem with language reflecting its current status as a structural argument. Engage seriously with mechanism design (VCG, proper scoring rules) as partial counterexamples to Goodhart-as-impossibility. Add a Formalization Roadmap specifying what a fully formal version would require.
- **Affected components:** SYN-02 paper revision
- **Category:** PROCESS
- **Effort:** M (days)
- **Dependencies:** None

### P1-28: Address the small-N problem for psychometric calibration

- **Source:** TRP-SYN-02 POV-3 Critique 3 (A8)
- **Recommendation:** With 117 repositories, full IRT estimation is marginal. Develop simplified approaches: classical reliability analysis, expert panel calibration, Bayesian methods with informative priors. Treat repeated measurements over time as additional "respondents." Document the statistical power constraints honestly.
- **Affected components:** organvm-engine analytics, methodology documentation
- **Category:** MEASUREMENT
- **Effort:** M (days)
- **Dependencies:** P0-04

### P1-29: Implement panarchy-aware design for phase transitions

- **Source:** RP-03 SS4.5, SS6.4 Heuristic 3
- **Recommendation:** Build organizational structures that can transition between hierarchical and rhizomatic phases. Implement innovation sandboxes, periodic reorganization mechanisms, and explicit "release/reorganization" phases within each organ's lifecycle. Monitor for rigid hierarchies that prevent creative destruction.
- **Affected components:** ORGAN-IV orchestration, organ-level governance
- **Category:** ARCHITECTURE
- **Effort:** L (weeks)
- **Dependencies:** P0-11

---

## P2: Enhancement Tasks

Nice-to-have improvements that deepen the system's theoretical alignment and operational sophistication.

### P2-01: Build adaptive governance assessment

- **Source:** RP-07 SS7 Implication 6
- **Recommendation:** Implement IRT-enabled adaptive testing: evaluate repositories with checks selected based on estimated quality level, concentrating measurement effort on checks most informative for each repository. Skip easy checks for obviously high-quality repos; skip hard checks for clearly low-quality ones.
- **Affected components:** organvm-engine assessment pipeline
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P1-01

### P2-02: Implement measurement invariance testing across organs

- **Source:** RP-07 SS5.5, SS6.3 Stage 4; SYN-02 SS5.5 Recommendation 3
- **Recommendation:** Conduct multi-group CFA and DIF analysis across organs, programming languages, and project types. Identify checks that exhibit DIF. Where invariance fails, implement group-specific scoring or redesign checks.
- **Affected components:** organvm-engine analytics
- **Category:** MEASUREMENT
- **Effort:** XL (months)
- **Dependencies:** P1-01, P0-14

### P2-03: Build a rhizomaticity index for organizational monitoring

- **Source:** RP-03 SS2.4
- **Recommendation:** Implement R(G) = f(C, L, gamma, Gini(centrality), 1/Q) for the dependency graph. Track clustering coefficient, average path length, power-law exponent, centrality inequality, and modularity over time. Alert when the system drifts toward unhealthy hierarchicalization or unproductive flatness.
- **Affected components:** organvm-engine network analysis, dashboard
- **Category:** TOOLING
- **Effort:** L (weeks)
- **Dependencies:** P1-07

### P2-04: Implement sense-preservation checks for aliases

- **Source:** RP-04 SS5.1 Principle 2
- **Recommendation:** When multiple names point to the same referent (customer_id / account_holder_id), validate that the naming system preserves sense distinctions. Warn when aliases collapse conceptual frames that should remain distinct.
- **Affected components:** organvm-engine, naming validation
- **Category:** NAMING
- **Effort:** S (hours)
- **Dependencies:** P0-06

### P2-05: Implement type-token naming discipline

- **Source:** RP-04 SS5.1 Principle 5
- **Recommendation:** Enforce that the naming convention visually distinguishes types from tokens, schemas from records, conventions from their applications. Audit the existing naming for type-token confusion.
- **Affected components:** Naming documentation, linting rules
- **Category:** NAMING
- **Effort:** S (hours)
- **Dependencies:** P0-05

### P2-06: Build the dynamic trilemma navigation model

- **Source:** TRP-SYN-02 POV-1 Expansion 1
- **Recommendation:** Develop a governance lifecycle model mapping expected trajectory of trilemma choices as the system scales. A startup phase might choose Complete+Measurable (accepting inconsistency for rapid iteration), migrating toward Consistent+Measurable at maturity. Identify transition costs and risks.
- **Affected components:** ORGAN-IV governance documentation, strategic planning
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P1-04

### P2-07: Map the inter-organ trilemma coordination problem

- **Source:** TRP-SYN-02 POV-1 Expansion 3
- **Recommendation:** Each organ makes its own local trilemma choice. ORGAN-IV must coordinate these choices. Map how one organ's incompleteness interacts with another organ's inconsistency. Identify the failure modes at inter-organ governance interfaces.
- **Affected components:** ORGAN-IV governance, organ-level documentation
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P1-04

### P2-08: Implement the Willard strategy for restricted self-verification

- **Source:** RP-02 SS7 (Willard strategy discussion)
- **Recommendation:** Investigate restricting governance system expressiveness so it cannot construct self-referential rules. If governance is restricted to enforcing rules about other components but not itself, the Godelian obstacle may be avoided for that restricted domain. An external mechanism fills the gap for self-governance.
- **Affected components:** ORGAN-IV governance architecture
- **Category:** GOVERNANCE
- **Effort:** L (weeks)
- **Dependencies:** P0-10

### P2-09: Implement abstract interpretation for semantic governance approximation

- **Source:** RP-02 SS4.3
- **Recommendation:** For semantic governance rules that cannot be decided exactly, implement abstract interpretation with explicit soundness/completeness tradeoffs. Document whether each approximation is over-approximate (conservative, no false negatives) or under-approximate (liberal, no false positives).
- **Affected components:** CI pipeline analysis tools
- **Category:** TOOLING
- **Effort:** L (weeks)
- **Dependencies:** P1-19

### P2-10: Design strange loop stability analysis

- **Source:** RP-02 SS5.6
- **Recommendation:** Identify all strange loops in the governance architecture (e.g., "governance engine validates all components; governance engine is a component"). Characterize each loop's stability: convergent (each iteration produces smaller deltas) vs. divergent (each iteration amplifies errors). Use temporal staging and external verification to stabilize divergent loops.
- **Affected components:** META-ORGANVM governance, ORGAN-IV
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P0-13

### P2-11: Explore consequential validity monitoring

- **Source:** SYN-04 SS5.3; RP-07 SS7 Implication 7
- **Recommendation:** Build feedback loops tracking downstream effects of assessment decisions. Do repositories that pass checks perform better in production? Do governance decisions produce intended organizational outcomes? Monitor for pathological incentives (Goodhart dynamics).
- **Affected components:** organvm-engine monitoring, dashboard
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P1-02

### P2-12: Implement multi-level interpretation naming

- **Source:** SYN-03 SS6.3
- **Recommendation:** Ensure naming conventions provide shallow interpretability (novice extracts basic info) and deep interpretability (expert extracts structural and semantic info). Test names against multiple expertise levels. The double-hyphen convention already exhibits this; ensure new names do too.
- **Affected components:** Naming guidelines, onboarding documentation
- **Category:** NAMING
- **Effort:** S (hours)
- **Dependencies:** P0-05

### P2-13: Build the ontological commitment registry

- **Source:** RP-04 SS5.1 Principle 1; SYN-03 SS5.4
- **Recommendation:** Maintain a registry of every naming decision that constitutes an ontological commitment. To name a directory "models/" is to assert that "models" is a valid category. Track these commitments and review them periodically for continued validity.
- **Affected components:** META-ORGANVM governance corpus
- **Category:** NAMING
- **Effort:** S (hours)
- **Dependencies:** P0-06

### P2-14: Implement names-as-infrastructure breakdown detection

- **Source:** SYN-03 SS2.2, SS6.4
- **Recommendation:** Naming infrastructure becomes visible upon breakdown. Build automated detection for: reference failures (names pointing to nothing), collisions (same name for different things), semantic drift (name meaning changed but name persists), abstraction mismatches (different systems using different names for the same concept).
- **Affected components:** organvm-engine validation, CI pipeline
- **Category:** NAMING
- **Effort:** M (days)
- **Dependencies:** P0-05, P0-06

### P2-15: Design for ontological pluralism in quality assessment

- **Source:** SYN-04 SS5.5
- **Recommendation:** Accept that "quality" is multiple -- constituted differently in different network configurations. A Python data pipeline, a TypeScript web app, and a Rust systems library are in different networks. Produce quality profiles rather than single scores. Use multi-group CFA with partial invariance.
- **Affected components:** organvm-engine scoring, dashboard visualization
- **Category:** MEASUREMENT
- **Effort:** L (weeks)
- **Dependencies:** P0-14, P2-02

### P2-16: Build a formalization roadmap for the Governance Trilemma

- **Source:** TRP-SYN-02 A3
- **Recommendation:** Specify what a fully formal version of the Governance Trilemma would require: (a) formal definition of "governance system" as mathematical object; (b) formal definitions of completeness, consistency, measurability; (c) conditions for joint unsatisfiability; (d) proof. Publish as research roadmap.
- **Affected components:** Research papers, ORGAN-I theory repos
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P1-27

### P2-17: Build governance rule classification by Chomsky level

- **Source:** RP-06 SS7.4; TRP-RP-06 POV-3 Expansion 4
- **Recommendation:** Classify every governance rule by its position in the Chomsky hierarchy: regular (simple pattern matching), context-free (recursive structural validation), context-sensitive (context-dependent checks), unrestricted (semantic judgment). Map decidability implications: regular/CF are decidable; CS is PSPACE-hard; unrestricted is undecidable.
- **Affected components:** ORGAN-IV governance-rules.json documentation
- **Category:** GOVERNANCE
- **Effort:** M (days)
- **Dependencies:** P0-02, P1-18

### P2-18: Implement alignment-as-translation framework for AI interactions

- **Source:** RP-05 SS5.5; CAPSTONE SS12.5
- **Recommendation:** Reframe AI alignment as ongoing network stabilization (translation) rather than value installation. Classify misalignment types by translation-failure moment: hallucination = mobilization failure, refusal = enrollment failure, value misalignment = problematization failure. Design remediation strategies per failure type.
- **Affected components:** AI interaction protocols, CLAUDE.md files
- **Category:** PROCESS
- **Effort:** M (days)
- **Dependencies:** P1-16

### P2-19: Build the test information function for governance assessment

- **Source:** RP-07 SS5.4
- **Recommendation:** Compute I(theta) = sum of item information functions across all governance checks. Identify regions of the quality continuum where measurement precision is inadequate. Add checks targeted at under-measured regions, especially promotion boundaries.
- **Affected components:** organvm-engine analytics
- **Category:** MEASUREMENT
- **Effort:** M (days)
- **Dependencies:** P1-01

### P2-20: Implement Dunbar-aware team sizing for organs

- **Source:** RP-03 SS4.1, SS6.4 Heuristic 6
- **Recommendation:** Within any organizational unit relying on lateral coordination, keep active participants below the cognitive limit (~150 for unassisted humans, potentially higher with AI mediation). Above this threshold, introduce hierarchical compression or subdivide. Currently single-operator, but design for future scaling.
- **Affected components:** ORGAN-IV scaling documentation
- **Category:** ARCHITECTURE
- **Effort:** S (hours)
- **Dependencies:** None

### P2-21: Implement SEM-based relational quality model

- **Source:** SYN-04 SS5.1
- **Recommendation:** Use structural equation modeling to specify quality not as a single latent variable but as a network of related constructs (maintainability, reliability, usability, security) with relationships explicitly modeled. Test fit against observed data.
- **Affected components:** organvm-engine analytics
- **Category:** MEASUREMENT
- **Effort:** XL (months)
- **Dependencies:** P0-04, P1-01

### P2-22: Scope-narrow the SYN-01 claims per TRP review

- **Source:** TRP-SYN-01 Synthesis Priorities 1-3
- **Recommendation:** Narrow SYN-01 scope claim to "the architecture of compositional formal meaning." Engage with philosophy of unification (Kitcher 1981, Morrison 2000). Provide honest DisCoCat empirical assessment. Position the result as structural unification akin to the Erlangen Programme.
- **Affected components:** SYN-01 paper revision
- **Category:** PROCESS (research)
- **Effort:** M (days)
- **Dependencies:** None

### P2-23: Address RP-06 Type 1 correspondence weakness

- **Source:** TRP-RP-06 A2
- **Recommendation:** Provide a concrete worked example encoding {a^n b^n c^n} as a System F typing problem, or explicitly acknowledge that this encoding is conjectural. The Type 1 (context-sensitive / parametric polymorphism) correspondence is the weakest link.
- **Affected components:** RP-06 paper revision
- **Category:** PROCESS (research)
- **Effort:** M (days)
- **Dependencies:** None

### P2-24: Propose MCS type-theoretic conjecture

- **Source:** RP-06 SS2.5, SS6.2; TRP-RP-06 A6
- **Recommendation:** Propose a concrete conjecture for the type-theoretic characterization of mildly context-sensitive languages, even if speculative. Candidates: bounded polymorphism with linearity constraints, or second-order with restricted quantification. Document as open problem.
- **Affected components:** RP-06 paper, ORGAN-I theory repos
- **Category:** ARCHITECTURE (theoretical)
- **Effort:** L (weeks)
- **Dependencies:** None

### P2-25: Design assessment for constitutive rather than just detection value

- **Source:** SYN-04 SS4.2-4.3, SS5.4
- **Recommendation:** Accept that CI checks are mediators, not intermediaries: they constitute quality, not just detect it. Design checks whose constitutive effects encourage beneficial practices. A requirement for documented architecture decisions promotes reflective design, even if it discriminates poorly.
- **Affected components:** CI pipeline check design
- **Category:** MEASUREMENT
- **Effort:** S (hours)
- **Dependencies:** P1-24

### P2-26: Implement names-stable-under-change principle

- **Source:** SYN-03 SS6.2
- **Recommendation:** Names should refer to what is stable, not what is volatile. Function and domain change less frequently than organizational reporting lines. Audit existing names for encoding organizational position vs. function. Prefer function/domain encoding (double-hyphen convention) over org-chart encoding.
- **Affected components:** Naming guidelines, repository naming
- **Category:** NAMING
- **Effort:** S (hours)
- **Dependencies:** P0-05

### P2-27: Build the compression/search ratio monitoring tool

- **Source:** RP-03 SS3.3, SS6.4 Heuristic 1
- **Recommendation:** For each domain in the system, monitor the ratio of hierarchical compression to rhizomatic search. Well-mapped domains should be more compressed; unmapped domains should preserve more connectivity. Alert when the ratio seems mismatched (too much hierarchy in creative domains, too little in coordination domains).
- **Affected components:** organvm-engine analysis, dashboard
- **Category:** TOOLING
- **Effort:** M (days)
- **Dependencies:** P2-03

### P2-28: Build explicit typological coverage in RP-06

- **Source:** TRP-RP-06 A3, A4
- **Recommendation:** Expand RP-06 linguistic examples to include polysynthetic languages, free word-order languages, and sign languages. Add scope-and-limitations addressing gradient grammaticality and non-compositionality. Acknowledge non-generativist frameworks (Construction Grammar, usage-based linguistics).
- **Affected components:** RP-06 paper revision
- **Category:** PROCESS (research)
- **Effort:** M (days)
- **Dependencies:** None

---

## Cross-Cutting Concerns

Tasks that affect multiple organs or require coordination across the system.

### CC-01: The syntactic/semantic boundary is the master organizing principle

All governance automation must respect the Rice boundary. Every check is either syntactic (decidable, fully automatable) or semantic (undecidable, requiring human judgment or explicit approximation). This distinction cross-cuts every organ, every repo, every CI pipeline, and every governance decision.

**Affected:** All organs, all repos, all CI, all governance.

### CC-02: The Governance Trilemma applies at every level

The trilemma applies not just to the system as a whole but to each organ, each repo's governance, and each governance tool. Each level makes its own trilemma choice, and the choices must be coordinated across levels (P2-07).

**Affected:** META-ORGANVM, ORGAN-IV, all organs.

### CC-03: Naming is infrastructure, not decoration

Every naming decision is an ontological commitment that shapes organizational topology. Naming debt compounds over time. Naming governance must be treated with the same rigor as API design or schema definition.

**Affected:** All repos, all naming conventions, all documentation.

### CC-04: Measurement constitutes its object

CI checks, governance scores, and quality metrics do not merely detect quality -- they constitute it. Assessment design must optimize for constitutive value (encouraging desirable practices) alongside diagnostic value (distinguishing quality levels).

**Affected:** All CI pipelines, organvm-engine scoring, governance-rules.json.

### CC-05: The human-in-the-loop is structurally necessary, not a temporary weakness

Human judgment at the semantic boundary is a response to impossibility results (Godel, Tarski, Rice, Goodhart), not a stopgap awaiting better automation. This reframes the human-AI relationship: the human is the incompleteness response.

**Affected:** IRA panel, all promotion decisions, AI interaction design.

---

## Implementation Sequence

### Phase A: Foundations (Weeks 1-4)
Establish structural preconditions.

1. P0-01: Make trilemma choice explicit
2. P0-02: Classify governance rules (syntactic/semantic)
3. P0-11: Codify hybrid topology principle
4. P0-13: Verify temporal staging in promotion pipeline
5. P0-05: Build naming convention validator
6. P0-06: Build controlled vocabulary registry
7. P0-12: Redesign governance artifacts as boundary objects
8. P0-07: Make incompleteness visible in all verdicts

### Phase B: Measurement Foundations (Weeks 3-8)
Build the psychometric infrastructure.

1. P0-03: Define "readiness" construct independently
2. P0-04: Conduct factor analysis on omega scorecard
3. P0-14: Implement context-specific governance norms
4. P1-23: Build item analysis for governance checks
5. P1-13: Validate Guttman scale for promotion pipeline
6. P1-03: Report scores with confidence intervals

### Phase C: Governance Hardening (Weeks 6-12)
Implement impossibility-aware governance.

1. P0-08: Formalize IRA panel protocol
2. P0-09: Track seed.yaml semantic accuracy
3. P0-10: Separate self-maintenance from self-improvement
4. P1-04: Build Governance Trilemma Audit
5. P1-05: Create Practitioner's Decision Matrix
6. P1-06: Implement OPP-based governance
7. P1-18: Build governance-as-type-system framework
8. P1-19: Implement approximation strategies per rule

### Phase D: Naming and Architecture (Weeks 8-14)
Strengthen naming infrastructure and organizational topology.

1. P1-08: Implement namespace governance
2. P1-09: Track naming debt
3. P1-20: Specify language games for naming contexts
4. P1-10: Monitor for emergent hierarchy
5. P1-07: Build stigmergic infrastructure layer
6. P1-15: Adopt VSM recursive structure
7. P1-29: Implement panarchy-aware phase transitions

### Phase E: Advanced Measurement (Weeks 12-20)
Implement psychometric calibration.

1. P1-01: IRT-based scoring
2. P1-28: Address small-N problem
3. P1-14: Criterion validation
4. P1-02: Goodhart monitoring
5. P1-11: Relational quality metrics
6. P1-12: Record network configuration with scores

### Phase F: Research Programme Revisions (Weeks 4-16)
Paper revisions per TRP reviews.

1. P1-27: Calibrate SYN-02 formality claims
2. P1-26: External case study for Governance Trilemma
3. P2-22: Scope-narrow SYN-01 claims
4. P2-23: Address RP-06 Type 1 weakness
5. P2-28: Expand RP-06 typological coverage

### Phase G: Enhancements (Weeks 16+)
P2 tasks as capacity allows.

Prioritized by impact: P2-01 (adaptive assessment), P2-03 (rhizomaticity index), P2-06 (dynamic trilemma navigation), P2-11 (consequential validity), P2-17 (Chomsky-level governance classification).

---

## Appendix: Source Traceability

| Task | Source Paper(s) | Section(s) |
|------|----------------|------------|
| P0-01 | SYN-02, TRP-SYN-02 | SS5.5 R1; POV-3 |
| P0-02 | RP-02, SYN-02 | SS4.5 I1, SS5.2; SS4.1 |
| P0-03 | RP-07, SYN-02, SYN-04 | SS7 I1; SS4.4; SS4.1 |
| P0-04 | RP-07, SYN-02 | SS6.2, SS6.3; SS5.5 R2 |
| P0-05 | RP-04, SYN-03, RP-02 | SS5.1 P6; SS6.4; SS4.5 I2 |
| P0-06 | RP-04, SYN-03 | SS5.1 P4; SS6.4 |
| P0-07 | RP-02, SYN-02 | SS5.5; SS5.5 R1 |
| P0-08 | RP-02, SYN-02 | SS6.3; SS4.5, SS5.3, SS5.5 R5 |
| P0-09 | RP-02, SYN-02 | SS6.2, SS6.4; SS5.4 |
| P0-10 | RP-02 | SS5.7, SS6.4 |
| P0-11 | RP-03, SYN-02 | SS6.1-6.4; SS4.2 |
| P0-12 | RP-05, SYN-02, SYN-03 | SS4.3, SS7.1; SS4.3; SS5.1-5.3 |
| P0-13 | RP-02, SYN-02 | SS5.1, SS6.1; SS4.1, SS5.2 |
| P0-14 | RP-07, SYN-02, SYN-04 | SS5.5, SS7 I4; SS5.5 R3; SS5.2 |
| P1-01 | RP-07, SYN-02 | SS5.1-5.4, SS6.3; SS4.4 |
| P1-02 | RP-07, SYN-02, SYN-04 | SS7 I7; SS5.4, SS5.5 R4; SS5.3 |
| P1-03 | RP-07, SYN-02 | SS6.4, SS7; SS4.4 |
| P1-04 | SYN-02, TRP-SYN-02 | SS6; POV-1 E2 |
| P1-05 | TRP-SYN-02, SYN-02 | POV-3; SS6 |
| P1-06 | RP-05, SYN-02 | SS7.3; SS4.3 |
| P1-07 | RP-03 | SS6.4 H5, SS7.2-7.3 |
| P1-08 | RP-04, SYN-03 | SS5.1 P3, P6; SS6.5 |
| P1-09 | RP-04, SYN-03 | SS5.3; SS3.4, SS6.2 |
| P1-10 | RP-03, SYN-02 | SS4.4; SS2.2 |
| P1-11 | SYN-04 | SS5.1 |
| P1-12 | SYN-04 | SS5.2 |
| P1-13 | RP-07, SYN-02 | SS4.1, SS6.3; SS5.2 |
| P1-14 | RP-07 | SS4.4, SS6.3, SS7 I5 |
| P1-15 | SYN-02, TRP-SYN-02 | SS4.6, SS5.5 R6; POV-1 |
| P1-16 | RP-05 | SS7.1 |
| P1-17 | RP-05 | SS7.2 |
| P1-18 | RP-02, RP-06 | SS4.4, SS4.5 I5; SS7.4 |
| P1-19 | RP-02 | SS4.3, SS5.4 |
| P1-20 | RP-04 | SS5.1 P7 |
| P1-21 | SYN-02, RP-05 | SS4.3, SS5.5 R7; SS7.1 |
| P1-22 | CAPSTONE | SS11.6 |
| P1-23 | RP-07 | SS6.3 S1 |
| P1-24 | SYN-04 | SS5.4 |
| P1-25 | SYN-01, CAPSTONE | SS6; SS10.2 |
| P1-26 | TRP-SYN-02 | A4 (all POVs) |
| P1-27 | TRP-SYN-02 | A1, A2, A3 |
| P1-28 | TRP-SYN-02 | POV-3 C3, A8 |
| P1-29 | RP-03 | SS4.5, SS6.4 H3 |
| P2-01 | RP-07 | SS7 I6 |
| P2-02 | RP-07, SYN-02 | SS5.5, SS6.3; SS5.5 R3 |
| P2-03 | RP-03 | SS2.4 |
| P2-04 | RP-04 | SS5.1 P2 |
| P2-05 | RP-04 | SS5.1 P5 |
| P2-06 | TRP-SYN-02 | POV-1 E1 |
| P2-07 | TRP-SYN-02 | POV-1 E3 |
| P2-08 | RP-02 | SS7 |
| P2-09 | RP-02 | SS4.3 |
| P2-10 | RP-02 | SS5.6 |
| P2-11 | SYN-04, RP-07 | SS5.3; SS7 I7 |
| P2-12 | SYN-03 | SS6.3 |
| P2-13 | RP-04, SYN-03 | SS5.1 P1; SS5.4 |
| P2-14 | SYN-03 | SS2.2, SS6.4 |
| P2-15 | SYN-04 | SS5.5 |
| P2-16 | TRP-SYN-02 | A3 |
| P2-17 | RP-06, TRP-RP-06 | SS7.4; POV-3 E4 |
| P2-18 | RP-05, CAPSTONE | SS5.5; SS12.5 |
| P2-19 | RP-07 | SS5.4 |
| P2-20 | RP-03 | SS4.1, SS6.4 H6 |
| P2-21 | SYN-04 | SS5.1 |
| P2-22 | TRP-SYN-01 | Priorities 1-3 |
| P2-23 | TRP-RP-06 | A2 |
| P2-24 | RP-06, TRP-RP-06 | SS2.5, SS6.2; A6 |
| P2-25 | SYN-04 | SS4.2-4.3, SS5.4 |
| P2-26 | SYN-03 | SS6.2 |
| P2-27 | RP-03 | SS3.3, SS6.4 H1 |
| P2-28 | TRP-RP-06 | A3, A4 |

---

**Legend:**
- SS = Section; I = Implication; P = Principle; H = Heuristic; R = Recommendation
- E = Expansion (TRP); C = Critique (TRP); A = Amendment (TRP)
- Source papers: RP-02, RP-03, RP-04, RP-05, RP-06, RP-07, SYN-01, SYN-02, SYN-03, SYN-04, SYN-05, CAPSTONE
- TRP reviews: TRP-SYN-02, TRP-RP-06, TRP-SYN-01
