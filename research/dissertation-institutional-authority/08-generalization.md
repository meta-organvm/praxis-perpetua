---
status: reference-activated
---
# CHAPTER 8 | GENERALIZATION: THE AUTHORITY AS PORTABLE META-ENTITY

## 8.1 Introduction

The preceding chapters establish the evaluative authority through first-principles specification (Chapter 3), statistical formalization (Chapter 4), empirical validation (Chapters 5-6), and self-governance design (Chapter 7). This chapter addresses RQ5: *Does the authority's architecture generalize across domains?*

The argument proceeds in three steps: (1) identify the domain-agnostic core that requires no modification across deployments; (2) identify the domain-specific configuration that must be authored per host system; (3) demonstrate through structural analysis that the three preconditions (structured pipeline, measurable dimensions, evaluative diversity) are satisfied across a representative set of external domains.

## 8.2 The Domain-Agnostic Core

The following components are invariant across all deployments:

| Component | Implementation | Why It's Domain-Agnostic |
|-----------|---------------|-------------------------|
| ICC(2,1) computation | `ira.py` | Operates on any n×k ratings matrix regardless of what rows/columns represent |
| Cohen's kappa | `ira.py` | Operates on any pairwise confusion matrix |
| Fleiss' kappa | `ira.py` | Operates on any multi-rater category assignment matrix |
| Consensus (median + IQR outlier detection) | `ira.py` | Operates on any set of numeric scores |
| Composite scoring (weighted sum) | `rubric.py` | Operates on any dimension-weight pairs |
| Re-rate threshold protocol | `ira.py` | Triggered by ICC value regardless of domain |
| Interpretation bands (Landis & Koch) | `ira.py` | Domain-independent statistical interpretation |
| Meta-diagnostic (6 meta-dimensions) | `meta.py` | Evaluates the authority's own health, not the host's |
| Archive management | `archive.py` | Stores/retrieves JSON regardless of content |
| Panel orchestration | `orchestrator.py` | Dispatches prompts to models regardless of content |

This core constitutes approximately 70% of the authority's codebase. It is authored once and reused everywhere.

## 8.3 The Domain-Specific Configuration

The following must be authored per host system:

| Configuration | Format | Authoring Effort |
|--------------|--------|-----------------|
| Rubric YAML | `system-grading-rubric.yaml` | 2-4 hours (first time); requires domain expertise |
| Persona YAML | `rater-personas.yaml` | 1-2 hours; requires understanding of evaluative perspectives |
| Adapter module | Python class implementing `AuthorityAdapter` | 2-8 hours; requires host system knowledge |
| Evidence collection logic | Within adapter methods | Part of adapter implementation |
| Outcome data mapping | Within adapter's `get_outcome_data()` | Part of adapter implementation |

This configuration constitutes approximately 30% of the deployment effort. It is the intellectual work — deciding *what to measure* and *from whose perspective*.

## 8.4 Precondition Analysis Across Domains

### 8.4.1 Precondition 1: Structured Pipeline with Quality Gates

A domain satisfies this precondition if its work product passes through defined stages where quality decisions are made.

| Domain | Pipeline Stages | Quality Gates |
|--------|----------------|---------------|
| Software development | design → implement → test → review → deploy | Code review, CI/CD, staging |
| Academic publishing | draft → submit → review → revise → publish | Peer review, editorial decision |
| Grant management | discover → draft → internal review → submit → report | PI review, institutional approval |
| Hiring (employer side) | source → screen → interview → offer → onboard | Resume screen, panel interview |
| Education | assign → draft → peer review → revise → grade | Rubric-based assessment |
| CI/CD | commit → build → test → stage → deploy | Test gates, approval gates |
| Creative production | concept → prototype → refine → exhibit → archive | Critique, curation |

All seven domains satisfy the precondition. The stages differ, but the *structure* — sequential progression with quality decisions between stages — is isomorphic.

### 8.4.2 Precondition 2: Measurable Quality Dimensions (Objective + Subjective Mix)

A domain satisfies this precondition if its quality can be decomposed into named dimensions, at least some of which are objectively measurable and at least some of which require interpretive judgment.

| Domain | Objective Dimensions (examples) | Subjective Dimensions (examples) |
|--------|-------------------------------|----------------------------------|
| Software | Test count, lint errors, CI status | Architecture quality, documentation clarity |
| Publishing | Word count, citation count, format compliance | Argument coherence, originality, writing quality |
| Grants | Budget completeness, eligibility match | Narrative quality, innovation potential |
| Hiring | Years experience, skills match score | Cultural fit, growth potential, communication |
| Education | Submission completeness, word count | Critical thinking, argument structure, creativity |
| CI/CD | Test pass rate, build time, coverage % | Architecture quality, security posture |
| Creative | Technical specifications met, format compliance | Aesthetic coherence, conceptual depth |

All seven domains exhibit the objective/subjective mix. The ratio varies (education is more subjective; CI/CD is more objective), but the mix exists in all.

### 8.4.3 Precondition 3: Meaningful Evaluative Diversity

A domain satisfies this precondition if multiple stakeholder perspectives exist that produce genuinely different quality judgments.

| Domain | Diverse Perspectives |
|--------|---------------------|
| Software | Architect, QA, operator, security, product manager, end user |
| Publishing | Methodologist, domain expert, generalist reader, statistical reviewer |
| Grants | Program officer, fiscal reviewer, domain expert, community representative |
| Hiring | Hiring manager, technical lead, HR partner, team peer |
| Education | Strict formalist, encouraging mentor, standards-based assessor, discipline expert |
| CI/CD | SRE, security engineer, product manager, platform architect |
| Creative | Formalist, expressionist, technologist, curator, audience member |

All seven domains have 4+ perspectives that would produce meaningfully different evaluations. The perspectives are not random — they reflect actual institutional roles with different evaluative priorities.

### 8.4.4 Summary

All seven candidate domains satisfy all three preconditions. The authority is structurally applicable to each; only the configuration (rubric, personas, adapter) needs to be authored.

## 8.5 Case Analysis: Academic Peer Review

Academic peer review is the domain closest to the authority's first instantiation — it already uses multiple evaluators, structured rubrics, and agreement measurement. The authority would formalize and augment existing practice.

**Current practice**: Journals assign 2-3 human reviewers who evaluate manuscripts independently against informal criteria, producing narrative reviews and an accept/revise/reject recommendation. Agreement is rarely measured formally; editorial decisions synthesize reviews through judgment, not statistics.

**Authority-augmented practice**:

1. **Rubric**: Formalize review criteria as a YAML rubric with scoring guides. Example dimensions: methodology_rigor (objective: are methods described reproducibly?), contribution_significance (subjective: does this advance the field?), writing_quality (subjective), statistical_validity (mixed: are analyses correct?), ethical_compliance (objective: IRB/consent documented?), reproducibility (mixed: code/data available?).

2. **Panel**: Deploy 4 AI raters as first-pass reviewers: the methodologist (penalizes weak methods), the domain expert (penalizes work that ignores prior literature), the practitioner (penalizes work with no practical implications), the statistical reviewer (penalizes analysis errors).

3. **Protocol**: AI panel produces first-pass scores with evidence and strengths/weaknesses. ICC measures agreement. Consensus scores with disagreement patterns are provided to human reviewers as structured context. Human reviewers still make the final decision.

4. **Value**: (a) Reduces reviewer workload by providing structured first-pass analysis. (b) Ensures every manuscript is evaluated from 4 perspectives, not the 2-3 that happen to be assigned. (c) ICC provides a quantitative measure of review consistency that journals can report. (d) Disagreement patterns flag dimensions where the manuscript provokes genuine evaluative controversy — often the most interesting part of a review.

**Feasibility**: Recent evidence supports this: ~20% of ICLR 2025 reviews were classified as AI-generated (arXiv, 2025), and LLMs have demonstrated ICC 0.919-0.972 on writing assessment rubrics (ScienceDirect, 2025). The authority would formalize what is already happening informally, adding statistical rigor and persona-driven diversity.

## 8.6 Case Analysis: CI/CD Quality Gating

CI/CD is the domain with the most immediate deployment path — engineering teams already use quality gates and would benefit most from moving beyond binary pass/fail.

**Current practice**: CI pipelines gate deployment on binary checks: tests pass/fail, lint pass/fail, security scan pass/fail, coverage threshold met/not met. These gates catch syntactic failures but cannot detect semantic degradation.

**Authority-augmented practice**:

1. **Pre-deployment diagnostic**: After tests pass, the authority evaluates the release across 6 dimensions: architecture_quality, test_coverage_depth (not just percentage — are the right things tested?), documentation_currency (is the documentation up to date with code changes?), security_posture (beyond automated scans — does the error handling follow security best practices?), operational_readiness (monitoring, alerting, runbooks updated?), backward_compatibility (breaking changes documented and communicated?).

2. **Panel**: SRE (values stability), security engineer (values defense), product manager (values completeness), platform architect (values long-term maintainability).

3. **Gate logic**: Instead of binary pass/fail, the gate produces a quality score. Releases scoring above threshold deploy automatically; releases below threshold require human approval; releases with low ICC (raters disagree significantly) require architectural review.

4. **Value**: Catches the "tests pass but the release is bad" failure class. Provides a quality trajectory across releases. Enables organizations to set quality standards that transcend binary checks.

## 8.7 Case Analysis: Multi-Organ ORGANVM Governance

The most ambitious generalization target: federated authority across ORGANVM's 8 organs, aggregated by a meta-authority in the Meta organ. (See Chapter 9 for deployment architecture.)

**What this enables**:

1. **System-wide health visibility**: A single dashboard showing quality scores across all 8 organs and 105 repositories
2. **Cross-organ comparison**: Which organ has the best documentation? The worst CI health? The most stale rubric?
3. **Promotion readiness assessment**: When a repository requests promotion (LOCAL → CANDIDATE → PUBLIC_PROCESS), the authority provides a multi-perspective quality score that informs the promotion decision
4. **Governance enforcement**: The authority can flag repositories that violate cross-organ contracts (dependency back-edges, seed.yaml non-compliance, naming convention drift)
5. **Trend intelligence**: System-wide quality trajectories over time — is the institution improving, degrading, or holding steady?

This is the evaluative authority at its most powerful: not evaluating a single system, but governing an entire institutional structure. The meta-authority consuming 8 organ-level authority instances is Beer's System 5 — the policy function — implemented as a computational governance layer.

## 8.8 The Generalization Formula

Restated from Chapter 3 with domain examples:

```
For any domain D satisfying preconditions (structured pipeline +
measurable dimensions + evaluative diversity):

  1. CONFIGURE: Author rubric(D), personas(D), adapter(D)
  2. DEPLOY: Instantiate authority with configuration
  3. ASSESS: Run evaluation cycle → ratings matrix → IRA → consensus
  4. INTERPRET: Consensus scores + disagreement patterns → diagnostic intelligence
  5. FEEDBACK: Route findings into operational parameters
  6. META-EVALUATE: Quarterly governance health check
```

Steps 2-6 are identical across domains. Step 1 is the intellectual work. The formula separates *what you know about your domain* (Step 1) from *how evaluation works* (Steps 2-6).

## 8.9 Boundary Conditions

The authority does not generalize to domains that:

- **Resist decomposition**: Quality is experienced holistically and cannot be meaningfully separated into dimensions (rare — even aesthetic judgment can be partially decomposed)
- **Lack reproducible evidence**: Evaluators cannot inspect the same artifacts (e.g., live performance evaluated only in the moment)
- **Have no evaluative diversity**: All stakeholders agree completely on what "good" means (very rare in practice)
- **Have no observable outcomes**: The feedback loop cannot close without success/failure signals

Within these boundaries, the authority is applicable to any domain that traditional quality assurance serves — and many that it currently does not.

## 8.10 Summary

The evaluative authority generalizes across domains because 70% of its implementation (the statistical, consensus, archival, and meta-evaluative machinery) is domain-agnostic. The remaining 30% (rubric, personas, adapter) is authored per domain. Seven candidate domains (software, publishing, grants, hiring, education, CI/CD, creative production) all satisfy the three structural preconditions. Detailed case analyses of academic peer review, CI/CD quality gating, and multi-organ ORGANVM governance demonstrate that the authority adds specific, identifiable value to each domain. The generalization formula separates domain knowledge (Step 1) from evaluation machinery (Steps 2-6), enabling adoption without reinventing the governance infrastructure.
