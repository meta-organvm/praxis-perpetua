# CHAPTER 3 | THE AUTHORITY: SYSTEM ARCHITECTURE INDEPENDENT OF HOST

## 3.1 Introduction

This chapter specifies the evaluative authority as a standalone system — independent of any host system it might evaluate. The architecture is presented in five layers, each with formal specification, interface contracts, and governance rules. A host system connects to the authority through an adapter interface (Section 3.7) that translates between the authority's generic evaluation protocol and the host's domain-specific evidence.

The chapter answers RQ1: *What is the minimal viable architecture for a self-governing evaluative authority?*

## 3.2 Architectural Overview

The authority comprises five layers, each implementing a distinct governance function:

```
Layer 5: Meta-Evaluative    ← Monitors the authority itself
Layer 4: Executive           ← Routes findings into operational changes
Layer 3: Judicial            ← Resolves evaluative disagreements into consensus
Layer 2: Deliberative        ← Produces independent evaluative judgments
Layer 1: Constitutional      ← Defines what is measured and how
```

Information flows upward (evidence → judgment → consensus → action → meta-assessment) and downward (meta-findings → governance adjustments → panel reconfiguration → rubric amendment).

Each layer is *independently specifiable* — a practitioner can adopt Layer 1-3 (rubric + panel + consensus) without Layers 4-5 (feedback + meta-evaluation) and still receive valid quality assessments. The full five-layer architecture is necessary only for self-governing operation.

## 3.3 Layer 1: Constitutional (The Rubric)

### 3.3.1 Specification

The rubric is a structured configuration document defining:

```yaml
version: string           # Semantic version (e.g., "1.1")
effective_date: date      # When this version took effect
composite_method: enum    # weighted_sum | multiplicative | lexicographic
scale:
  min: float              # Lower bound (e.g., 1.0)
  max: float              # Upper bound (e.g., 10.0)
  precision: int          # Decimal places for reporting

dimensions:
  <dimension_key>:
    label: string         # Human-readable name
    type: enum            # objective | subjective | mixed
    weight: float         # [0.0, 1.0], all weights sum to 1.0
    description: string   # What this dimension measures
    scoring_guide:        # Anchored descriptions at scale points
      1: string
      3: string
      5: string
      7: string
      10: string
    evidence_sources:     # How to gather grounding data
      - type: enum        # command | path | section | api
        target: string    # The command, path, section ref, or API endpoint
        measures: string  # What aspect this source measures
    ira_config:
      agreement_method: enum      # icc | kappa | both
      consensus_method: enum      # median | mean | trimmed_mean
      outlier_threshold: float    # IQR factor (e.g., 1.5)
```

### 3.3.2 Design Constraints

- **Σ weights = 1.0** (enforced by validator)
- **At least 1 objective dimension** (guarantees a reliability floor)
- **At least 1 subjective dimension** (otherwise IRA computation is vacuous)
- **Scoring guide anchors at 1, 3, 5, 7, 10** (provides evaluators with concrete criteria at regular intervals)
- **Every dimension has at least 1 evidence source** (no dimension may be evaluated without grounding)

### 3.3.3 The Objective/Subjective Partition

The partition is the rubric's most consequential design choice. It determines which dimensions are measured by automated collectors (deterministic, zero variance) and which are evaluated by the rater panel (stochastic, measurable variance).

**Design rule**: A dimension is classified as `objective` if and only if a deterministic function can compute its score from observable system state without interpretive judgment. If any ambiguity exists in the scoring (e.g., "is this architecture clean?"), the dimension is `subjective` or `mixed`.

The partition serves three functions:
1. **Prevents ICC inflation** — objective dimensions would artificially inflate agreement
2. **Provides a reliability floor** — partial assessment is always available without API dependency
3. **Separates epistemologies** — counting (objective) and judging (subjective) require different methods; conflating them produces neither good counts nor good judgments

## 3.4 Layer 2: Deliberative (The Rater Panel)

### 3.4.1 Specification

The panel is configured as a list of rater definitions:

```yaml
panel:
  - rater_id: string        # Unique identifier
    model: string           # Model identifier (e.g., "claude-opus-4-6")
    provider: enum          # anthropic | google | meta | mistral | openai
    persona: string         # Reference to persona definition
    temperature: float      # [0.0, 1.0]

personas:
  <persona_key>:
    role: string            # Identity framing (who the evaluator is)
    scoring_bias: string    # Ambiguity resolution instruction
```

### 3.4.2 Design Constraints

- **Minimum 3 raters** (ICC requires ≥ 2; meaningful outlier detection requires ≥ 3)
- **Maximum 7 raters** (diminishing returns on ICC confidence interval narrowing beyond 5-7)
- **Cross-provider minimum**: At least 1 rater from a non-majority provider family
- **Persona uniqueness**: No two raters may share the same persona
- **Explicit bias**: Every persona must have a `scoring_bias` field. Personas without explicit bias instructions produce agreeableness-collapsed evaluations

### 3.4.3 The Persona Contract

A persona is well-formed if and only if:
1. The `role` establishes a recognizable evaluative identity (not a generic "AI assistant")
2. The `scoring_bias` specifies a directional preference for resolving ambiguity ("when in doubt, penalize X and reward Y")
3. The bias is *defensible* — it represents a perspective that a reasonable human expert in that role would hold
4. The bias is *distinct* — it produces meaningfully different scores from at least one other persona in the panel on at least one rubric dimension

### 3.4.4 Evaluation Protocol

For each assessment cycle:

1. **Evidence assembly**: For each subjective dimension, the authority's prompt generator collects evidence from the host system via the adapter interface (Section 3.7) and assembles it into a structured prompt
2. **System prompt construction**: Persona (role + bias) + rubric scoring guides + output format specification
3. **Model invocation**: System prompt + evidence prompt → model API call at configured temperature
4. **Response validation**: Parsed JSON checked for all required fields, score range compliance, dimensional completeness
5. **Retry policy**: Up to 2 retries on validation failure; if all retries fail, the rater is marked as `failed` for this cycle and excluded from consensus computation (minimum rater threshold still must be met)

### 3.4.5 Output Format

Each rater produces, per subjective dimension:

```json
{
  "score": float,           // [scale.min, scale.max]
  "confidence": enum,       // "high" | "medium" | "low"
  "evidence": string,       // Grounding citation
  "strengths": [string],    // What the rater found positive
  "weaknesses": [string]    // What the rater found negative
}
```

The `confidence`, `strengths`, and `weaknesses` fields are not used in IRA computation but are preserved in the archive for qualitative analysis and human review.

## 3.5 Layer 3: Judicial (Consensus Mechanism)

### 3.5.1 Agreement Computation

Given a ratings matrix R of shape (n_dimensions × k_raters):

**ICC(2,1)**: Two-way random, single measures, absolute agreement. Computed over subjective dimensions only. Interpretation via Landis & Koch (1977) bands.

**Cohen's kappa**: Computed for all (k choose 2) rater pairs. Scores are binned into categories ([1-3], [4-6], [7-9], [10]) for chance correction.

**Fleiss' kappa**: Computed across all k raters simultaneously.

### 3.5.2 Consensus Computation

For each dimension:

1. Collect all rater scores (for objective dimensions: the single automated score repeated; for subjective: individual rater scores)
2. Compute median, Q1, Q3, IQR
3. Flag scores outside [Q1 - f×IQR, Q3 + f×IQR] as outliers (f = configurable, default 1.5)
4. Consensus score = median (outliers flagged but not removed)

### 3.5.3 Composite Score

Composite = Σ(weight_i × consensus_i) for all dimensions.

### 3.5.4 Re-Rate Threshold

If overall ICC < configurable threshold (default 0.61):
- Flag the assessment as **governance crisis**
- Do not compute composite (it would be meaningless)
- Trigger investigation protocol (see Chapter 7)

## 3.6 Layer 4: Executive (Feedback Channels)

### 3.6.1 Channel Specification

The authority defines four feedback channel types. Each channel has a trigger condition, a recommendation format, and an authorization requirement:

| Channel | Trigger | Recommendation | Authorization |
|---------|---------|---------------|---------------|
| **Threshold calibration** | Operational output drops to zero despite healthy infrastructure | Adjust scoring thresholds ±N | Human confirmation required |
| **Content correlation** | Outcome data available for content used in submissions | Classify content units as effective/ineffective | Automatic below threshold; human above |
| **External validation** | External data source updated | Compare internal assumptions vs external ground truth | Advisory only (no auto-adjust) |
| **Longitudinal tracking** | New assessment completed | Compute trends, detect inflections | Advisory only |

### 3.6.2 The Separation of Powers

**The authority may advise but not act.** All feedback channels produce recommendations, not commands. The host system's operator decides whether to implement recommendations. This separation prevents the evaluative institution from becoming an autonomous governor.

Exception: *pre-authorized narrow adjustments*. The host system may pre-authorize specific adjustment types within defined bounds (e.g., "threshold adjustments of ±0.5 may be applied automatically"). Pre-authorization is explicit, bounded, and revocable.

## 3.7 The Adapter Interface

### 3.7.1 Purpose

The adapter interface is the boundary between the domain-agnostic authority and the domain-specific host system. It translates the authority's generic evidence requests into host-specific data collection operations.

### 3.7.2 Interface Contract

A host system adapter must implement:

```python
class AuthorityAdapter(Protocol):
    """Interface contract for connecting a host system to the evaluative authority."""

    def get_system_id(self) -> str:
        """Unique identifier for this host system."""

    def get_rubric_path(self) -> Path:
        """Path to this host's rubric YAML."""

    def collect_objective_evidence(self, dimension: str) -> dict:
        """Run automated collectors for an objective dimension.

        Returns: {score: float, evidence: str, raw_output: str}
        """

    def collect_subjective_evidence(self, dimension: str) -> str:
        """Assemble evidence for a subjective dimension.

        Returns: Structured text suitable for inclusion in an LLM prompt.
        Evidence should include file listings, code samples, metrics,
        and any other artifacts that ground the dimension's scoring guide.
        """

    def get_outcome_data(self) -> list[dict]:
        """Return outcome records for feedback loop computation.

        Each record: {item_id: str, outcome: str, metadata: dict}
        Outcomes are domain-specific (e.g., 'accepted', 'rejected',
        'deployed', 'reverted', 'published', 'cited').
        """

    def apply_recommendation(self, channel: str, recommendation: dict) -> bool:
        """Apply a feedback recommendation to the host system.

        Returns True if applied, False if rejected or deferred.
        The adapter may enforce its own authorization checks.
        """

    def get_archive_path(self) -> Path:
        """Path to this host's diagnostic archive directory."""
```

### 3.7.3 Adapter Examples

**Career application pipeline adapter**: `collect_objective_evidence("test_coverage")` runs `pytest --co` and `verification_matrix.py --strict`. `collect_subjective_evidence("architecture")` assembles module listings, dependency graph, CLAUDE.md architecture sections.

**ORGANVM governance adapter**: `collect_objective_evidence("seed_compliance")` validates all seed.yaml files against schema. `collect_subjective_evidence("cross_organ_coherence")` assembles naming convention samples, aesthetic alignment checks, contract honor status.

**Essay quality adapter**: `collect_objective_evidence("word_count")` counts words. `collect_subjective_evidence("argument_coherence")` assembles the essay text, thesis statement, evidence citations.

The adapter pattern ensures the authority never needs to understand host-system internals. It requests evidence through a standard interface; the adapter translates.

## 3.8 Layer 5: Meta-Evaluative

### 3.8.1 Purpose

Layer 5 monitors the authority itself — detecting governance failures that Layers 1-4 cannot detect because they are the source of the failures.

### 3.8.2 Meta-Rubric

A second rubric evaluates the authority's governance health:

| Meta-Dimension | Type | What It Measures |
|---------------|------|------------------|
| Rubric currency | objective | Do evidence sources still exist? Are scoring guides still achievable? |
| Persona diversity | objective | Coefficient of variation across rater scores (CV > threshold?) |
| Statistical robustness | objective | ICC confidence interval width; minimum rater count met? |
| Feedback latency | objective | Time between detection and recommendation |
| Archive integrity | objective | All historical assessments preserved? Date continuity? |
| External coverage | mixed | Fraction of internal assumptions with external ground truth |

### 3.8.3 The Three-Tier Resolution

The meta-evaluative problem (what evaluates the evaluator?) is resolved through three tiers:

1. **Statistical self-monitoring** (automated): ICC as internal consistency check. Detects rater disagreement.
2. **Meta-diagnostic** (periodic): The meta-rubric applied to the authority itself. Detects institutional degradation.
3. **Human epistemic audit** (quarterly): The irreducible human capacity to ask "what might we be missing?" Detects unknown unknowns.

The recursion terminates at tier 3 — we do not propose a meta-meta-diagnostic. The human's epistemic contribution is the authority's ground floor.

## 3.9 Deployment Modes

### 3.9.1 Single-Host

One authority instance evaluating one host system. The simplest deployment. The authority's rubric, panel, and feedback channels are configured for the single host.

### 3.9.2 Multi-Host

One authority instance evaluating multiple host systems through multiple adapters. Each host has its own rubric and adapter, but the panel configuration and IRA computation are shared. This enables cross-system comparison: "Host A scores 8.5 on documentation; Host B scores 6.2 — investigate Host B."

### 3.9.3 Federated

Multiple authority instances, each evaluating its own host, with a meta-authority aggregating cross-instance health. This is the ORGANVM deployment model: each organ gets its own authority instance with organ-specific rubric and personas; the Meta organ runs a meta-authority that aggregates cross-organ health into a system-wide dashboard.

```
Meta-Authority (META organ)
├── Authority Instance: ORGAN-I (Theoria)
│   └── Adapter: knowledge-engine, symbolic-computing repos
├── Authority Instance: ORGAN-II (Poiesis)
│   └── Adapter: generative-art, performance-system repos
├── Authority Instance: ORGAN-III (Ergon)
│   └── Adapter: product repos, SaaS tools
├── Authority Instance: ORGAN-IV (Taxis)
│   └── Adapter: orchestration, governance repos
├── Authority Instance: ORGAN-V (Logos)
│   └── Adapter: essay-pipeline, editorial repos
├── Authority Instance: ORGAN-VI (Koinonia)
│   └── Adapter: community, learning repos
├── Authority Instance: ORGAN-VII (Kerygma)
│   └── Adapter: distribution, social-automation repos
└── Authority Instance: Application Pipeline (personal)
    └── Adapter: pipeline scripts, YAML entries
```

The meta-authority's rubric dimensions are:
- Per-organ health score (the weighted composite from each instance)
- Cross-organ consistency (do inter-organ dependencies honor contracts?)
- Promotion pipeline health (are repos progressing through the state machine?)
- System-wide trend (is the overall health trajectory improving?)

## 3.10 Summary

The five-layer architecture — Constitutional, Deliberative, Judicial, Executive, Meta-Evaluative — constitutes the minimal viable governance for self-regulating quality assessment. Each layer is independently specifiable and adoptable. The adapter interface decouples the authority from any specific host system. Three deployment modes (single-host, multi-host, federated) accommodate scales from a single project to a multi-organ institutional system.

The architecture is specified at sufficient detail to implement. Chapter 4 formalizes the statistical mechanisms. Chapter 5 demonstrates the first implementation.
