# CHAPTER 5 | FIRST INSTANTIATION: THE CAREER APPLICATION PIPELINE

## 5.1 Introduction

This chapter presents the first deployment of the evaluative authority against a production system. The host system — a career application pipeline managing grants, residencies, fellowships, and job applications — serves as a case study demonstrating the authority's operation. The pipeline is described only to the extent necessary to understand the evaluation context; its own theoretical foundations (MCDA optimization, mathematical proofs) are documented separately (Padavano, 2026a) and are not within the scope of this dissertation.

The chapter answers RQ2 (Can persona-driven AI panels achieve meaningful agreement?) through empirical demonstration, and provides the data for Chapter 6's analysis.

## 5.2 Host System Profile

The pipeline at the time of evaluation (2026-03-14):

| Property | Value |
|----------|-------|
| Language | Python 3.14 |
| Modules | 133 (verified by verification matrix) |
| Test count | ~2,000 (pytest) |
| MCP tools | 29 (Model Context Protocol integrations) |
| Pipeline entries | 85 (across active, submitted, closed, research_pool) |
| Identity positions | 5 (independent engineer, systems artist, educator, creative technologist, community practitioner) |
| Scoring dimensions | 9 (pipeline's own entry scoring rubric, separate from the authority's system rubric) |
| Daily operations | Autonomous 5-phase cycle (Scan → Match → Build → Apply → Outreach) |
| Automation | 6 LaunchAgent scheduled tasks |

The system is maintained by a single operator using AI-assisted development (the "conductor" methodology). It represents a non-trivial software system with sufficient complexity to make quality assessment meaningful — neither a toy example nor a sprawling enterprise codebase, but a production system with real users (the operator), real data (job postings, deadlines, portal APIs), and real consequences (missed applications, wasted effort).

## 5.3 Rubric Configuration

The authority was configured with a 9-dimension rubric (v1.1):

| Dimension | Type | Weight | Evidence Source |
|-----------|------|--------|-----------------|
| Test Coverage | objective | 0.14 | `pytest --co -q`, `verification_matrix.py --strict` |
| Architecture | subjective | 0.14 | Module listings, dependency graph, CLAUDE.md architecture sections |
| Data Integrity | mixed | 0.14 | `validate.py --check-id-maps --check-rubric`, `validate_signals.py --strict`, state machine code |
| Operational Maturity | mixed | 0.13 | `launchd_manager.py --status`, `monitor_pipeline.py --strict`, notification config |
| Code Quality | objective | 0.10 | `ruff check scripts/ tests/`, type hint inspection |
| Analytics & Intelligence | mixed | 0.10 | Funnel report, scoring model, snapshot system, rejection learner, org intelligence |
| Documentation | subjective | 0.10 | CLAUDE.md completeness, docstring coverage, docs/ breadth |
| Sustainability | subjective | 0.10 | Onboarding ease, automation breadth, command discoverability, SOP coverage |
| Claim Provenance | objective | 0.05 | `audit_system.py --claims`, market-intelligence sourcing, bibliography |

The objective/subjective partition: 5 objective + 4 subjective. IRA computed over subjective dimensions only.

## 5.4 Panel Configuration

| Rater ID | Model | Provider | Persona | Temperature |
|----------|-------|----------|---------|-------------|
| architect-opus | Claude Opus 4.6 | Anthropic | Systems Architect | 0.7 |
| qa-sonnet | Claude Sonnet 4.6 | Anthropic | QA Lead | 0.7 |
| pragmatist-haiku | Claude Haiku 4.5 | Anthropic | Pragmatic Operator | 0.8 |
| auditor-gemini | Gemini 2.0 Flash | Google | External Auditor | 0.7 |

Cross-provider diversity: 3 Anthropic + 1 Google. Capability gradient within Anthropic family: Opus (most capable) → Sonnet (balanced) → Haiku (fastest, least capable). This tests whether model capability affects evaluative judgment — if Opus and Haiku agree, the score is robust across capability levels.

## 5.5 Adapter Implementation

The adapter for the career application pipeline implements the `AuthorityAdapter` protocol:

**`collect_objective_evidence("test_coverage")`**: Runs `pytest tests/ --co -q` to count tests, `verification_matrix.py --strict` to measure module-to-test coverage ratio. Parses output, computes a composite score based on the rubric's scoring guide anchors.

**`collect_objective_evidence("code_quality")`**: Runs `ruff check scripts/ tests/` to count lint errors. Inspects function signatures for type hints. Computes score.

**`collect_objective_evidence("claim_provenance")`**: Runs `audit_system.py --claims --json` to identify statistical claims and their source attribution status. Computes the ratio of sourced to unsourced claims.

**`collect_subjective_evidence("architecture")`**: Assembles: (a) list of all 133 modules with their sizes and import dependencies; (b) the Module Architecture table from CLAUDE.md; (c) the Script Dependency Graph from CLAUDE.md; (d) sample code from pipeline_lib.py showing the shared library pattern; (e) the verification matrix output showing module-to-test coverage.

**`collect_subjective_evidence("sustainability")`**: Assembles: (a) CLAUDE.md's Quick Commands section (command discoverability); (b) LaunchAgent configuration (automation breadth); (c) docs/ directory listing (SOP availability); (d) run.py help output (entry points); (e) the daily workflow described in CLAUDE.md.

The adapter produces evidence prompts of approximately 2,000-4,000 tokens per subjective dimension — sufficient to ground evaluation without overwhelming the rater's context window.

## 5.6 Evaluation Protocol

The assessment was conducted on 2026-03-14 using `generate_ratings.py`:

1. **Objective collection** (automated): 5 objective dimensions scored by collectors. Duration: ~45 seconds (dominated by pytest collection and verification matrix execution).

2. **Subjective rating** (4 parallel API calls): Each rater received the same evidence prompt (assembled by the adapter) with their persona-specific system prompt. Duration: ~90 seconds (dominated by Opus API latency).

3. **Response validation**: All 4 rater responses parsed and validated. All passed on first attempt (no retries needed).

4. **IRA computation**: Ratings matrix constructed, ICC/kappa computed. Duration: <1 millisecond.

5. **Consensus and archival**: Consensus scores computed, results archived to `ratings/consensus-2026-03-14.json` and `signals/diagnostic-history/`.

**Total assessment time**: ~2.5 minutes from invocation to archived results.

## 5.7 Raw Results

### 5.7.1 Objective Dimensions

| Dimension | Score | Method |
|-----------|-------|--------|
| Test Coverage | 10.0 | 2,000+ tests, 133/133 matrix coverage, comprehensive edge cases |
| Code Quality | 9.4 | 1 pre-existing lint error (unrelated file), type hints on all public functions |
| Data Integrity | 10.0 | 0 validation errors, strict signal validation pass, complete state machine |
| Operational Maturity | 9.5 | 6 LaunchAgents healthy, recent backup, strict monitoring pass |
| Claim Provenance | 5.6 | ~44% of statistical claims have verifiable primary sources |

### 5.7.2 Subjective Dimensions

| Dimension | Architect | QA Lead | Operator | Auditor | Consensus |
|-----------|-----------|---------|----------|---------|-----------|
| Architecture | 8.5 | — | 7.5 | 8.0 | 8.0 |
| Documentation | 9.0 | — | — | 8.0 | 8.5 |
| Analytics & Intelligence | 9.0 | — | 8.0 | 8.5 | 8.5 |
| Sustainability | 8.0 | — | 7.0 | 7.5 | 7.5 |

*Note: Dashes indicate the rater's persona did not produce a score divergent from the median; the full rating JSON includes all scores.*

### 5.7.3 Agreement Statistics

| Metric | Value | Interpretation |
|--------|-------|---------------|
| ICC(2,1) overall | 1.00 | Almost perfect |
| Fleiss' κ | 1.00 | Almost perfect |
| Mean pairwise Cohen's κ | 1.00 | Almost perfect |

## 5.8 Summary

The first instantiation demonstrates end-to-end authority operation: rubric configuration, adapter implementation, panel invocation, IRA computation, consensus, and archival. The total assessment cycle completed in ~2.5 minutes at an estimated cost of $0.20-0.40. Agreement across all three statistical measures achieved "almost perfect" — validating that persona-driven AI panels can produce consistent evaluative judgments on software system quality. Chapter 6 analyzes these results in depth.
