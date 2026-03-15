# CHAPTER 9 | DEPLOYMENT ARCHITECTURE: ORGANVM AND BEYOND

## 9.1 Introduction

The preceding chapters establish the evaluative authority as a domain-agnostic system with formal specification (Chapter 3), validated statistical methods (Chapter 4), empirical demonstration (Chapters 5-6), self-governance mechanisms (Chapter 7), and generalization across domains (Chapter 8). This chapter addresses the engineering question: **how do you actually deploy this?**

The chapter specifies three deployment scenarios in increasing complexity: standalone deployment (one authority, one host), ORGANVM-native deployment (federated authorities across 8 organs), and external deployment (the authority as an open-source package adoptable by any team).

## 9.2 Standalone Deployment

### 9.2.1 Minimum Viable Deployment

The simplest deployment requires four artifacts:

1. **Rubric YAML** — defines dimensions, weights, scoring guides
2. **Persona YAML** — defines rater identities and biases
3. **Adapter module** — implements the `AuthorityAdapter` protocol for the host system
4. **API keys** — for at least 2 model providers (cross-provider minimum)

The IRA computation module, consensus engine, and meta-evaluative layer are provided by the authority package. The practitioner supplies only the domain-specific configuration.

### 9.2.2 Deployment Checklist

```
□ Define rubric dimensions (minimum: 1 objective + 1 subjective)
□ Write scoring guides for each dimension (anchors at 1, 3, 5, 7, 10)
□ Identify evidence sources per dimension
□ Define at least 3 personas with explicit scoring biases
□ Implement adapter: collect_objective_evidence() for each objective dimension
□ Implement adapter: collect_subjective_evidence() for each subjective dimension
□ Configure API keys for ≥ 2 model providers
□ Run first assessment in dry-run mode
□ Review rater outputs for prompt quality (are raters receiving adequate evidence?)
□ Run first live assessment
□ Verify ICC > 0.61 (if not: investigate rubric ambiguity or persona conflict)
□ Archive results and establish baseline
□ Schedule recurring assessment (recommended: weekly)
```

### 9.2.3 Time to First Assessment

For a practitioner familiar with their host system, the estimated effort:

| Step | Time |
|------|------|
| Rubric design | 2-4 hours (first time); 30 min (subsequent rubrics) |
| Persona design | 1-2 hours |
| Adapter implementation | 2-8 hours (depends on host system complexity) |
| First assessment run | 5-15 minutes (API call latency) |
| Review and baseline | 1 hour |
| **Total** | **6-15 hours first deployment; 1 hour subsequent** |

## 9.3 ORGANVM-Native Deployment

### 9.3.1 The Federated Model

ORGANVM's 8 organs + personal infrastructure = 9 deployment targets. Each gets its own authority instance with:

- **Organ-specific rubric** tailored to the organ's function and quality requirements
- **Organ-specific adapter** that knows how to collect evidence from that organ's repos
- **Shared panel configuration** (same 4 raters across all organs for cross-organ comparability, with optional organ-specific guest raters)
- **Instance-level archive** in each organ's signals directory
- **Meta-authority** in the Meta organ aggregating all instances

### 9.3.2 Per-Organ Rubric Proposals

**ORGAN-I (Theoria) — Foundational Theory**

| Dimension | Type | Weight | Measures |
|-----------|------|--------|----------|
| Formal Rigor | subjective | 0.20 | Mathematical correctness, proof completeness |
| Conceptual Originality | subjective | 0.20 | Novel contributions to recursive/symbolic theory |
| Implementation Fidelity | mixed | 0.15 | Do implementations match formal specifications? |
| Documentation Depth | subjective | 0.15 | Are theoretical foundations documented accessibly? |
| Test Coverage | objective | 0.15 | Test count, edge cases, property-based tests |
| Cross-Organ Influence | mixed | 0.15 | Are theoretical outputs consumed by downstream organs? |

**ORGAN-II (Poiesis) — Generative Art & Performance**

| Dimension | Type | Weight | Measures |
|-----------|------|--------|----------|
| Algorithmic Sophistication | subjective | 0.20 | Complexity and elegance of generative algorithms |
| Aesthetic Coherence | subjective | 0.20 | Visual/auditory consistency, design system adherence |
| Interactivity Depth | mixed | 0.15 | Responsive to input, parameter space richness |
| Performance Stability | objective | 0.15 | Frame rate, memory usage, crash frequency |
| Conceptual Grounding | subjective | 0.15 | Connection to ORGAN-I theoretical foundations |
| Exhibition Readiness | mixed | 0.15 | Deployable, documented, presentable to audiences |

**ORGAN-III (Ergon) — Commercial Products**

| Dimension | Type | Weight | Measures |
|-----------|------|--------|----------|
| Market Readiness | mixed | 0.20 | Deploy state, onboarding flow, pricing model |
| Code Quality | objective | 0.15 | Lint compliance, type safety, test coverage |
| User Experience | subjective | 0.20 | Usability, accessibility, documentation |
| Architecture | subjective | 0.15 | Module boundaries, dependency management |
| Security Posture | mixed | 0.15 | Dependency audit, OWASP compliance, secret management |
| Revenue Potential | subjective | 0.15 | Pricing model viability, market demand signal |

**ORGAN-IV (Taxis) — Orchestration & Governance**

| Dimension | Type | Weight | Measures |
|-----------|------|--------|----------|
| Seed Compliance | objective | 0.20 | seed.yaml present, valid, correct organ membership |
| CI Health | objective | 0.15 | Workflow passing, last run recency, branch protection |
| Governance Enforcement | mixed | 0.20 | Dependency rules honored, promotion state machine enforced |
| Cross-Organ Coherence | subjective | 0.15 | Naming conventions, aesthetic alignment, contract honor |
| Automation Coverage | mixed | 0.15 | Scheduled tasks, LaunchAgents, cron coverage |
| Documentation Completeness | subjective | 0.15 | CLAUDE.md quality, architecture docs, onboarding |

**ORGAN-V (Logos) — Public Discourse**

| Dimension | Type | Weight | Measures |
|-----------|------|--------|----------|
| Argument Coherence | subjective | 0.25 | Thesis clarity, logical structure, evidence flow |
| Evidence Sourcing | mixed | 0.20 | Citation count, source quality, recency |
| Prose Quality | subjective | 0.20 | Clarity, voice, economy of expression |
| Audience Calibration | subjective | 0.15 | Appropriate register, assumed knowledge level |
| Publication Readiness | mixed | 0.10 | Format compliance, metadata completeness |
| Originality | subjective | 0.10 | Novel contribution vs. rehash of existing ideas |

**ORGAN-VI (Koinonia) — Community**

| Dimension | Type | Weight | Measures |
|-----------|------|--------|----------|
| Engagement Design | subjective | 0.25 | Activity structure, participation scaffolding |
| Accessibility | mixed | 0.20 | Barrier to entry, inclusive design, multilingual |
| Content Quality | subjective | 0.20 | Curriculum rigor, reading list curation |
| Community Health | mixed | 0.20 | Participation rates, return rates, moderation quality |
| Infrastructure | objective | 0.15 | Platform stability, tooling, documentation |

**ORGAN-VII (Kerygma) — Distribution**

| Dimension | Type | Weight | Measures |
|-----------|------|--------|----------|
| Reach | objective | 0.25 | Follower counts, impression metrics, cross-platform |
| Consistency | objective | 0.20 | Posting frequency, schedule adherence |
| Content Alignment | subjective | 0.20 | On-brand, on-message, organ-source traceability |
| Automation Reliability | objective | 0.20 | POSSE pipeline health, failure rate |
| Audience Growth | mixed | 0.15 | Follower growth rate, engagement rate trends |

**META — Cross-Organ Governance**

| Dimension | Type | Weight | Measures |
|-----------|------|--------|----------|
| Registry Integrity | objective | 0.20 | registry-v2.json valid, repo count accurate |
| Promotion Pipeline | mixed | 0.20 | Repos progressing through state machine |
| Dashboard Accuracy | mixed | 0.15 | Dashboard reflects actual system state |
| Schema Compliance | objective | 0.15 | All schemas valid, contracts honored |
| Governance Documentation | subjective | 0.15 | Rules documented, rationale clear |
| Omega Progress | objective | 0.15 | Criteria met toward system completion target |

### 9.3.3 The Meta-Authority Dashboard

The Meta organ's authority instance consumes output from all 8 organ instances plus the pipeline instance. Its dashboard presents:

1. **System-wide health heatmap**: 9 organs × N dimensions, color-coded by consensus score
2. **Cross-organ comparison**: Which organs score highest/lowest on each shared dimension (e.g., documentation)
3. **Trend vectors**: Per-organ health trajectory (improving / stable / degrading)
4. **Promotion bottlenecks**: Which repos are stalled in the state machine and why
5. **Governance alerts**: Any organ whose ICC drops below threshold, any dimension with outlier scores, any stale assessment

### 9.3.4 Shared Panel, Organ-Specific Guests

The base panel (4 raters: architect, QA, operator, auditor) evaluates all organs for cross-organ comparability. Individual organs may add *guest raters* with organ-specific personas:

- ORGAN-I adds a *mathematical formalist* guest
- ORGAN-II adds a *curator* guest
- ORGAN-III adds a *product manager* guest
- ORGAN-V adds a *literary critic* guest

Guest raters participate in that organ's assessment only. Their scores are included in the organ's IRA computation but excluded from cross-organ comparison (which uses only the shared panel).

### 9.3.5 Implementation Roadmap

| Phase | Scope | Deliverable |
|-------|-------|-------------|
| Phase 1 | Application pipeline (done) | Validated authority, 9 dimensions, 4 raters |
| Phase 2 | ORGAN-IV (Taxis) | Governance diagnostic across 105 repos |
| Phase 3 | ORGAN-V (Logos) + ORGAN-III (Ergon) | Essay quality + product readiness |
| Phase 4 | Remaining organs | Full coverage |
| Phase 5 | Meta-authority + dashboard | System-wide aggregation |

Phase 2 is the natural next step because Taxis already has governance infrastructure (registry, dependency validation, promotion state machine) that provides evidence sources for an objective-heavy rubric. The adapter is straightforward: most evidence comes from existing CLI commands.

## 9.4 External Deployment

### 9.4.1 Package Architecture

For external adoption, the authority should be distributed as a standalone Python package:

```
conductor-ira/
├── conductor_ira/
│   ├── __init__.py
│   ├── rubric.py          # Rubric loader, validator, version manager
│   ├── panel.py           # Panel configuration, model dispatch
│   ├── providers/
│   │   ├── anthropic.py   # Anthropic API adapter
│   │   ├── google.py      # Google Gemini adapter
│   │   ├── openai.py      # OpenAI adapter
│   │   └── base.py        # Provider protocol
│   ├── ira.py             # ICC, kappa, consensus computation
│   ├── feedback.py        # Feedback channel framework
│   ├── meta.py            # Meta-evaluative layer
│   ├── archive.py         # Diagnostic history management
│   ├── adapter.py         # AuthorityAdapter protocol definition
│   └── orchestrator.py    # Assessment cycle runner
├── templates/
│   ├── rubric-software.yaml      # Template: software system evaluation
│   ├── rubric-writing.yaml       # Template: writing quality evaluation
│   ├── rubric-governance.yaml    # Template: organizational governance
│   ├── rubric-ci-cd.yaml         # Template: CI/CD quality gate
│   ├── personas-software.yaml    # Template: software evaluation personas
│   ├── personas-writing.yaml     # Template: writing evaluation personas
│   └── personas-governance.yaml  # Template: governance evaluation personas
├── examples/
│   ├── minimal/           # Minimum viable deployment (3 dimensions, 3 raters)
│   ├── software-project/  # Full software quality assessment
│   └── essay-grading/     # Writing assessment with rubric-based grading
├── tests/
├── pyproject.toml
└── README.md
```

### 9.4.2 Adoption Path

```
1. pip install conductor-ira
2. Copy a rubric template and customize dimensions
3. Copy a persona template and customize perspectives
4. Implement your adapter (or use a provided one for common systems)
5. Set API keys
6. Run: conductor-ira assess --rubric rubric.yaml --personas personas.yaml
7. Review output, establish baseline
8. Schedule recurring assessment
```

### 9.4.3 Template Library

The template library lowers the activation energy for new domains. Each template includes:

- Pre-defined dimensions with scoring guides
- Pre-defined personas with roles and biases
- A sample adapter implementation
- Expected ICC ranges based on domain characteristics (software: 0.7-1.0; writing: 0.6-0.9; art: 0.4-0.7)

Templates are starting points, not prescriptions. Practitioners are expected to customize dimensions and personas for their specific context.

## 9.5 Operational Considerations

### 9.5.1 Cost

Each assessment cycle requires 1 API call per rater per assessment. At 4 raters and current pricing:

| Provider | Model | Cost per call (est.) | Per assessment |
|----------|-------|---------------------|----------------|
| Anthropic | Opus 4.6 | $0.15-0.30 | $0.15-0.30 |
| Anthropic | Sonnet 4.6 | $0.03-0.06 | $0.03-0.06 |
| Anthropic | Haiku 4.5 | $0.01-0.02 | $0.01-0.02 |
| Google | Gemini 2.0 Flash | $0.01-0.02 | $0.01-0.02 |
| **Total** | | | **$0.20-0.40** |

At weekly cadence: ~$10-20/year. The evaluative authority is cheaper to operate than a single code review from a contractor.

### 9.5.2 Latency

Assessment wall-clock time is dominated by the slowest API call. With parallel rater invocation:

- 4 parallel API calls: 30-120 seconds (depends on prompt length and model)
- IRA computation: < 1 second (pure arithmetic)
- Consensus + archival: < 1 second
- **Total: ~1-2 minutes per assessment**

### 9.5.3 Failure Handling

- **API unavailable**: Fall back to objective-only assessment (no subjective raters, no IRA, but partial scores available)
- **Single rater fails**: Proceed with k-1 raters if k-1 ≥ min_raters (default 3)
- **All raters fail**: Produce objective-only assessment + alert
- **Rubric validation fails**: Refuse to assess (constitution is broken; fix before proceeding)
- **Archive write fails**: Assessment succeeds but flags archive integrity warning in next meta-evaluation

## 9.6 Summary

The evaluative authority deploys in three modes: standalone (one host), ORGANVM-native (federated with meta-authority), and external (pip package with templates). The ORGANVM deployment covers 8 organs with per-organ rubrics and shared rater panels, aggregated by a Meta-organ dashboard. External deployment targets a 6-15 hour first-deployment time, <$20/year operating cost, and 1-2 minute assessment cycles. The package architecture separates domain-agnostic machinery (IRA computation, consensus, meta-evaluation) from domain-specific configuration (rubrics, personas, adapters), enabling adoption without reinventing the governance infrastructure.
