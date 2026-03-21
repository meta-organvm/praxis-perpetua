# Session Retrospective: SGO-2026 Research Programme

**Date:** 2026-03-21
**Session span:** 2026-03-20 through 2026-03-21
**Scope:** Full execution of the SGO-2026 "Formalization of Knowledge" research pipeline
**Status:** Pipeline Stages 1-8 complete; Stage 9 (this document) in progress

---

## What Was Accomplished (Quantified)

### Research Output

| Artifact | Count | Total Words |
|----------|------:|------------:|
| Research adventures | 7 | 39,602 |
| Research programme prospectus | 1 | 7,788 |
| Primary research papers (v1) | 7 | ~86,000 |
| Synthesis papers (v1) | 5 | ~61,500 |
| Capstone dissertation (v1) | 1 | ~20,000 |
| Revised papers (v2) | 13 | ~166,000 |
| **Total paper words** | **13 works** | **~166,000** |

### Review Output

| Artifact | Count | Approx. Words |
|----------|------:|------------:|
| TRP batch reviews | 3 | ~238,000 |
| TRP individual reviews | 3 | ~116,000 |
| TRP re-reviews | 1 | ~39,000 |
| **Total review words** | **7 documents** | **~393,000** |

### Implementation Output

| Artifact | Count |
|----------|------:|
| Implementation manifest tasks | 74 (14 P0, 32 P1, 28 P2) |
| arXiv submission packages prepared | 3 |
| Governance documents enacted | 4 |
| Research pipeline SOP | 1 |
| Research registry (YAML) | 1 |
| Session retrospective | 1 (this document) |

### Pipeline Coverage

| Stage | Status |
|-------|--------|
| 1. GENESIS (source extraction) | Complete |
| 2. EXPANSION (adventures) | Complete -- 7 adventures |
| 3. FORMALIZATION (prospectus) | Complete -- programme registered |
| 4. COMPOSITION (paper drafting) | Complete -- 13 works across 4 phases |
| 5. REVIEW (TRP) | Complete -- 7 review documents (including batch reviews covering multiple works), all works reviewed |
| 6. REVISION (v2 drafts) | Complete -- all 13 works revised; SYN-01 re-reviewed |
| 7. PUBLICATION (arXiv prep) | Partial -- 3 of 13 papers have submission packages |
| 8. IMPLEMENTATION (manifest + governance) | In progress -- 4 of 14 P0 tasks complete |
| 9. FEEDBACK (this retrospective) | In progress |

### Aggregate Statistics

- **Total words produced this session:** ~560,000+ (papers + reviews + infrastructure docs)
- **Distinct intellectual domains traversed:** 7 (formal semantics, computability, organizational theory, naming theory, ANT/STS, formal language theory, psychometrics)
- **Academic tiers achieved:** 13 works classified as 5 Dissertations (including 1 Capstone), 5 Theses, 3 Papers
- **Papers ready for arXiv:** 3 (RP-06, SYN-01, SYN-02)
- **Governance documents enacted:** 4

---

## What Worked Well

### 1. The Adventure-First Research Model

Starting with exploratory "adventures" -- structured Wikipedia-driven research sessions -- rather than jumping directly to paper writing was the single most productive decision. The adventures:

- Provided a natural clustering of ideas into paper-sized units
- Discovered cross-domain connections that would not have emerged from siloed paper planning
- Generated source material rich enough that paper composition could proceed from synthesis rather than from scratch
- Created a traceable provenance chain (source -> adventure -> prospectus -> paper)

### 2. Parallel Composition with Dependency-Phased Batching

Organizing 13 papers into 4 dependency phases and composing within each phase in parallel exploited the independence structure of the research programme. Phase 1 papers (no dependencies) could be drafted simultaneously; Phase 2 papers could begin as soon as their Phase 1 dependencies were complete.

This was the right granularity. Finer parallelism (within a single paper) would have produced inconsistencies. Coarser parallelism (one paper at a time) would have been prohibitively slow for 13 works.

### 3. The Triadic Review Protocol

The TRP was the quality backbone of the programme. Three non-redundant points of view per review produced:

- Critiques that no single reviewer would have identified (the cross-cultural gap in SYN-01 was caught by POV-3, not by the domain-expert POV-1)
- Amendments that strengthened papers substantially (the formality calibration for SYN-02 was a TRP amendment, not an author insight)
- Expansions that identified follow-on research directions (the Governance Trilemma Audit instrument was a TRP expansion)

The "amorphous triadic constitution" -- where panel composition is shaped by the venture's domain signature rather than by fixed roles -- was essential for handling 13 papers spanning 7 domains.

### 4. Implementation Manifest Extraction

Systematically scanning all papers and reviews for actionable recommendations produced a 74-task manifest that would not have emerged from ad hoc reading. The manifest's structure (priority tiers, category classification, dependency mapping, effort estimates, source traceability) makes it a genuine project plan, not just a wish list.

### 5. Immediate Governance Enactment

Converting the first three P0 tasks into enacted governance documents in the same session that produced the research demonstrated the full pipeline from theory to practice. The governance trilemma declaration, syntactic-semantic boundary classification, and naming convention spec are not abstractions -- they are operational documents that change how ORGANVM governs itself.

---

## What Could Improve

### 1. The Cross-Cultural Blind Spot

The TRP review of SYN-01 (Grand Unified Semantics) identified a significant Western-centrism in the linguistic evidence. The paper claimed universality while drawing almost exclusively from Indo-European language families. This was caught by POV-3 (the practitioner perspective, not the domain expert), which suggests:

- **The blind spot was structural, not accidental.** Domain expertise in formal semantics naturally gravitates toward well-studied (Western) languages. The outsider perspective was needed precisely because insiders share the blind spot.
- **Lesson:** For any paper claiming cross-cultural or universal scope, the TRP panel must include a POV specifically tasked with evaluating typological diversity. This should be a TRP panel constitution rule, not left to chance.

The v2 revision addressed this by incorporating Turkish, Mandarin, ASL, Warlpiri, and Mohawk examples. The re-review confirmed the improvement but noted ongoing limitations with gradient grammaticality.

### 2. Scope Inflation Pattern

Several papers exhibited scope inflation during composition: the initial paper prospectus targeted a specific question, but the draft expanded to address adjacent questions, increasing word count and diluting focus. Specific cases:

- RP-06 (Fourfold Correspondence) grew from a Chomsky hierarchy extension to a comprehensive cross-linguistic survey
- SYN-02 (Governance Impossibility) expanded from a trilemma argument to a full design framework
- The Capstone attempted to integrate all seven threads plus meta-reflection

**Lesson:** Scope boundaries set in the prospectus should be enforced during composition. Each paper should have a "not in scope" declaration that is checked during drafting. The TRP should assess scope discipline alongside content quality.

### 3. Review Batch Size

The first two TRP batches (4 and 5 papers respectively) were too large for deep review of each paper. The per-paper review depth was necessarily shallower than the individual reviews (RP-06, SYN-01, SYN-02). The individual reviews produced more actionable amendments.

**Lesson:** Batch reviews are appropriate for thematic assessment and cross-paper consistency. Deep reviews require individual treatment. The two are complementary, not substitutes. Future programmes should plan for both: a batch review for cross-paper themes, followed by individual reviews for papers targeted for publication.

### 4. Version Control Friction

Papers in `praxis-perpetua/intake/research-adventures-2026-03/` and copies in `praxis-perpetua/research/sgo-2026-formalization-of-knowledge/` create a two-location problem. The canonical versions live in the intake directory (where they were produced), but the research programme lives in praxis-perpetua (where they are governed).

**Lesson:** Establish a single canonical location for research artefacts at programme start. The intake directory should be for raw inbound material; once a paper enters the research programme, it should live in the programme directory. File moves should happen at programme registration (Stage 3), not retroactively.

### 5. Empirical Grounding Gap

The research programme is theoretical. All 13 papers argue from existing literature and formal reasoning. None present original empirical data (experiments, measurements, case studies beyond ORGANVM itself). The TRP reviews consistently noted this limitation, particularly for:

- RP-07 (Measuring the Unmeasurable) -- proposes psychometric methods but does not apply them
- SYN-02 (Governance Impossibility) -- proposes the Governance Trilemma but tests it only on the author's own system
- SYN-04 (Measuring Actants) -- critiques existing metrics but does not propose validated alternatives

**Lesson:** The next pipeline cycle (Stage 9 -> Stage 1) should prioritize empirical work: applying the proposed methods to ORGANVM's actual data (117 repos, 17 omega criteria, promotion history) and to at least one external system (per P1-26).

---

## Lessons for Next Session

1. **Start with the research registry.** Create RESEARCH-REGISTRY.yaml at Stage 3 (formalization), not retroactively at Stage 8. The registry is the programme's source of truth; it should exist before papers are written.

2. **Enforce scope boundaries during composition.** Each paper's prospectus should include a "not in scope" section. During drafting, check against this boundary. Scope inflation is the most predictable failure mode.

3. **Plan both batch and individual TRP reviews.** Batch reviews for cross-paper consistency; individual reviews for publication-targeted papers. Budget time for both.

4. **Single canonical location for all programme artefacts.** Decide at programme start whether artefacts live in intake or in the research programme directory. Do not maintain two copies.

5. **Interleave empirical work.** After the theoretical papers are drafted, pause composition to run empirical analyses (factor analysis on omega scorecard, IRT estimation, Guttman scale analysis). Feed results back into paper revisions before final submission.

6. **Track TRP amendments with disposition codes.** Every amendment should be tracked as ACCEPTED / PARTIALLY_ACCEPTED / REJECTED_WITH_JUSTIFICATION / DEFERRED. Currently, this tracking is implicit in the revision process; it should be explicit in a structured log.

7. **Memory-aware parallelism.** On 16GB RAM with background services (Dropbox, Backblaze), limit concurrent AI sessions to 2-3. The SGO-2026 session pushed this limit during Phase 3/4 composition.

---

## Open Items and Next Actions

### Immediate (Next Session)

| ID | Task | Priority | Source |
|----|------|----------|--------|
| NEXT-01 | Complete remaining P0 governance tasks (P0-03, P0-04, P0-06 through P0-14) | P0 | IMPLEMENTATION-MANIFEST.md |
| NEXT-02 | Move canonical paper copies from intake to praxis-perpetua programme directory | Housekeeping | Retrospective lesson 4 |
| NEXT-03 | Convert RP-06 from Markdown to LaTeX for arXiv submission | P0 | ARXIV-SUBMISSION-PACKAGES.md |
| NEXT-04 | Run factor analysis on omega scorecard (P0-04) to ground RP-07 claims empirically | P0 | IMPLEMENTATION-MANIFEST.md |
| NEXT-05 | Build the naming convention validator (P0-05 code implementation) | P0 | IMPLEMENTATION-MANIFEST.md |

### Near-Term (Weeks 1-4)

| ID | Task | Priority | Source |
|----|------|----------|--------|
| NT-01 | Submit RP-06 to arXiv (cs.FL) | High | ARXIV-SUBMISSION-PACKAGES.md |
| NT-02 | Submit SYN-02 to arXiv (cs.AI) | High | ARXIV-SUBMISSION-PACKAGES.md |
| NT-03 | Submit SYN-01 to arXiv (cs.LO) | High | ARXIV-SUBMISSION-PACKAGES.md |
| NT-04 | Complete Phase A implementation tasks (IMPLEMENTATION-MANIFEST.md Phase A) | P0 | Manifest |
| NT-05 | Begin Phase B measurement foundations (P0-03, P0-04, P0-14) | P0 | Manifest |
| NT-06 | Conduct external case study for Governance Trilemma (P1-26) | P1 | Manifest / TRP-SYN-02 |

### Medium-Term (Weeks 4-12)

| ID | Task | Priority | Source |
|----|------|----------|--------|
| MT-01 | Implement IRT-based scoring (P1-01) after factor analysis | P1 | Manifest Phase E |
| MT-02 | Build Goodhart monitoring system (P1-02) | P1 | Manifest Phase E |
| MT-03 | Revise SYN-02 with external case study data | P1 | Manifest P1-26 |
| MT-04 | Journal submission: RP-06 to JoLLI | P1 | ARXIV-SUBMISSION-PACKAGES.md |
| MT-05 | Journal submission: SYN-02 to Philosophy and Technology | P1 | ARXIV-SUBMISSION-PACKAGES.md |

---

## Session Metrics

| Metric | Value |
|--------|-------|
| Pipeline stages completed | 8 of 9 |
| Total works produced | 13 papers + 7 adventures + 1 prospectus |
| Total words (papers) | ~166,000 |
| Total words (reviews) | ~393,000 |
| Total words (all artefacts) | ~560,000+ |
| TRP reviews executed | 7 (including 1 re-review) |
| Governance documents enacted | 4 |
| Implementation tasks extracted | 74 |
| P0 tasks completed | 4 of 14 (29%) |
| Papers ready for arXiv | 3 of 13 (23%) |
| Domains traversed | 7 |
| Academic tiers: Capstone | 1 |
| Academic tiers: Dissertation | 5 |
| Academic tiers: Thesis | 4 |
| Academic tiers: Paper | 3 |

---

## The Spiral Continues

This session demonstrated that a single practitioner with AI-conductor amplification can produce a doctoral-scale research programme in two days. The output is not finished -- 10 of 14 P0 tasks remain, no papers have been submitted, and empirical validation is pending. But the intellectual infrastructure is in place: the questions are formalized, the arguments are drafted, the reviews are complete, and the implementation path is mapped.

The next cycle of the spiral begins where this one ends: with the implementation experience feeding back into the research, the empirical data grounding the theoretical claims, and the governance documents changing how the system operates. The pipeline is now documented (2026-03-21-research-pipeline-sop.md), the registry is initialized (RESEARCH-REGISTRY.yaml), and the open items are tracked (this document).

The Governance Trilemma declaration says ORGANVM chooses Consistency and Measurability, accepting Incompleteness. This session was an exercise in incompleteness management: producing enough to be useful, documenting what remains undone, and building the infrastructure to continue.

---

*This retrospective is itself a Stage 9 (FEEDBACK) output of the research pipeline SOP. It closes the first cycle and opens the second.*
