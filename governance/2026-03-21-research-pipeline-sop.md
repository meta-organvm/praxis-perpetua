# Research Pipeline SOP: From Genesis to Feedback

**Date:** 2026-03-21
**Status:** ENACTED
**Source:** Empirical documentation of the SGO-2026-RP-001 research pipeline as executed 2026-03-20/21
**Scope:** All SGO research programmes; reusable for any ORGANVM research initiative
**Theoretical Basis:** Operationalized from the Triadic Review Protocol (SGO-2026-SOP-001) and the research-to-implementation pipeline (SOP: The Gold Path)

---

## Purpose

This SOP formalizes the nine-stage research pipeline that the Studium Generale ORGANVM (SGO) executed during the "Formalization of Knowledge" programme. The pipeline transforms raw source material into reviewed papers, governance documents, and system-level code changes -- then feeds empirical results back into the research cycle.

The pipeline is designed for single-practitioner operation with AI-conductor amplification: one human directing, multiple AI agents generating volume, the human reviewing and deciding at every semantic boundary.

---

## The Nine Stages

```
GENESIS --> EXPANSION --> FORMALIZATION --> COMPOSITION --> REVIEW --> REVISION --> PUBLICATION --> IMPLEMENTATION --> FEEDBACK
   |                                                                                                                    |
   +--------------------------------------------------------------------------------------------------------------------+
                                                    (spiral)
```

---

## Stage 1: GENESIS (Source Extraction and Domain Clustering)

**Purpose:** Extract the intellectual raw material from existing knowledge bases and cluster it into coherent research domains.

**Inputs:**
- Personal knowledge bases, reading notes, prior session logs
- Existing ORGANVM documentation corpus (740K+ words across praxis-perpetua)
- Prior research (dissertations, papers, studies in `research/`)

**Process:**
1. **Source inventory.** Catalog all source material using `alchemia intake` or manual inventory. Record provenance, date, format, and estimated relevance.
2. **Atlas construction.** Build a research atlas -- a structured map of topics, questions, and connections discovered in the source material. Use SQLite databases for structured querying when the corpus exceeds what fits in a single context window.
   - Tool: `sqlite3` for atlas queries across large source sets
   - Tool: `alchemia synthesize` for cross-document pattern extraction
3. **Domain clustering.** Group related topics into coherent research domains. Each cluster becomes a candidate "adventure" -- an exploratory research session.
   - Heuristic: 5-8 clusters is typical for a programme-scale effort
   - Each cluster should have a central question that can sustain a full research paper

**Outputs:**
- Research atlas document (structured topic map with cross-references)
- Domain cluster list with central questions per cluster
- Source inventory with provenance metadata

**Quality gate:** Each cluster must have a central question that is (a) non-trivial, (b) researchable through available sources, and (c) connected to at least one other cluster.

---

## Stage 2: EXPANSION (Adventures and Frontier Discovery)

**Purpose:** Explore each domain cluster through directed research, discovering connections, filling gaps, and identifying frontier questions.

**Inputs:**
- Domain clusters from Stage 1
- Wikipedia as a structured knowledge graph for frontier discovery
- Academic databases, arXiv, and domain-specific sources

**Process:**
1. **Adventure execution.** For each domain cluster, conduct a research adventure: a structured exploration session that follows the question through sources, cross-references, and synthesis.
   - Tool: Wikipedia MCP tools (`search_wikipedia`, `get_article`, `get_sections`, `get_links`, `get_related_topics`) for systematic frontier discovery
   - Tool: `perplexity_research` for targeted deep-dive questions
   - Tool: `tavily_research` for current-state-of-the-art searches
   - Method: Follow the "three clicks" heuristic -- from any starting article, explore three levels of cross-references to discover adjacent domains
2. **Frontier identification.** For each adventure, identify the frontier: where does current knowledge end? What questions remain open? Where do different domains intersect in unexplored ways?
3. **Cross-adventure synthesis.** After all adventures are complete, identify cross-cutting themes that span multiple adventures. These become synthesis paper candidates.

**Outputs:**
- Adventure documents (one per domain cluster, 4,000-7,000 words each)
- Cross-reference map linking adventures to each other
- Frontier questions list per adventure
- Synthesis paper candidates (cross-cutting themes)

**Quality gate:** Each adventure must cite at least 10 substantive sources and identify at least 2 frontier questions not addressed in the existing literature.

---

## Stage 3: FORMALIZATION (Prospectus and Research Design)

**Purpose:** Transform exploratory adventures into formal research proposals with explicit questions, methodology, and expected contributions.

**Inputs:**
- Adventure documents from Stage 2
- Cross-reference map and synthesis candidates
- Existing SGO governance (charter.yaml, defense-protocol.yaml)

**Process:**
1. **Prospectus drafting.** Write a formal research programme prospectus declaring:
   - Programme title and central thesis
   - Individual paper prospectuses (one per adventure + synthesis papers + capstone)
   - Dependency graph between papers
   - Phasing plan (which papers can be written in parallel)
   - Academic tier targets per paper (Paper, Thesis, Dissertation)
   - Expected word counts and completion timeline
2. **Research question formalization.** For each paper, formalize:
   - Primary research question (one sentence)
   - Secondary questions (2-4 supporting questions)
   - Methodology (theoretical, empirical, mixed)
   - Expected contributions (what is novel)
   - Relationship to existing literature
3. **Programme registration.** Register the programme in the SGO research registry (RESEARCH-REGISTRY.yaml) with a programme ID.

**Outputs:**
- Research Programme Prospectus (single comprehensive document)
- Per-paper prospectuses (embedded in the programme prospectus)
- Dependency graph (DAG of paper dependencies)
- RESEARCH-REGISTRY.yaml entry

**Quality gate:** The prospectus must be internally consistent -- no paper should depend on a paper that depends on it (DAG property). Every paper must have at least one novel contribution claim.

---

## Stage 4: COMPOSITION (Paper Drafting with Parallel Agents)

**Purpose:** Draft all papers, exploiting the dependency graph for maximum parallelism.

**Inputs:**
- Prospectus and per-paper research designs from Stage 3
- Adventure documents and source material
- Dependency graph (determines phasing)

**Process:**
1. **Phase planning.** Group papers by dependency tier:
   - Phase 1: Papers with no dependencies (can be drafted in parallel)
   - Phase 2: Papers depending only on Phase 1 outputs
   - Phase 3: Papers depending on Phase 2 outputs
   - Phase 4: Capstone and final synthesis (depends on everything)
2. **Parallel drafting.** Within each phase, draft papers in parallel using multiple agent sessions:
   - Tool: Parallel Claude Code sessions (one per paper within a phase)
   - Method: Each session receives the relevant adventure document, the paper prospectus, and any completed Phase N-1 papers as context
   - Constraint: Memory-aware parallelism -- on 16GB RAM, limit to 2-3 concurrent drafting sessions
3. **Cross-paper consistency.** After each phase, review cross-references between papers for consistency. Terminology, notation, and claims must be aligned.
4. **Version control.** Each draft is versioned: `DRAFT-v1.md` (initial), `DRAFT-v2.md` (post-review revision), etc. Never overwrite -- always create a new version.

**Outputs:**
- Draft papers (one per work, versioned)
- Cross-reference consistency report
- Word count and tier compliance check

**Quality gate:** Each paper must meet minimum word count for its tier (Paper: 6K+, Thesis: 10K+, Dissertation: 13K+). All cross-references must resolve.

---

## Stage 5: REVIEW (Triadic Review Protocol)

**Purpose:** Subject each paper (or batch of papers) to structured adversarial review using the Triadic Review Protocol (TRP).

**Inputs:**
- Draft papers from Stage 4
- TRP SOP (SGO-2026-SOP-001)
- Faculty registry (governance/faculty-registry.yaml)

**Process:**
1. **Panel constitution.** For each review batch, constitute a panel of three Points of View (POVs). The panel is "amorphous triadic" -- its composition is shaped by the venture's domain signature, not by fixed roles:
   - POV-1: Strongest domain expertise (e.g., formal semantics for a logic paper)
   - POV-2: Adjacent domain perspective (e.g., philosophy for a logic paper)
   - POV-3: Practitioner/outsider perspective (e.g., software engineering for a logic paper)
   - The three POVs must be non-redundant -- their expertise sets must not fully overlap
2. **Batching strategy.** Papers can be reviewed in batches when they share enough context to benefit from cross-paper assessment. The SGO-2026 programme used three batches:
   - Batch 1: Phase 1 papers + RP-01 (4 papers)
   - Batch 2: Phase 2-3 synthesis papers + SYN-05 (5 papers)
   - Batch 3: Individual deep reviews (RP-06, SYN-01, SYN-02)
3. **Review execution.** Each POV produces:
   - Critiques (weaknesses, errors, gaps)
   - Expansions (directions the paper should explore further)
   - Amendments (specific changes required)
   - An overall assessment with ICC-compatible scoring
4. **Synthesis.** After all three POVs report, synthesize:
   - Points of agreement (high-confidence findings)
   - Points of productive disagreement (areas needing author judgment)
   - Prioritized action items

**Outputs:**
- TRP review documents (one per review batch or per individual paper)
- Synthesized action items with priority rankings
- ICC scores where applicable

**Quality gate:** Every paper must receive assessments from all three POVs. The synthesis must explicitly address all amendments rated "critical" or "high priority."

---

## Stage 6: REVISION (Amendment Incorporation)

**Purpose:** Incorporate TRP amendments into revised drafts, creating v2 papers.

**Inputs:**
- TRP review documents from Stage 5
- Original draft papers (v1)
- Synthesized action items

**Process:**
1. **Amendment triage.** Classify each amendment:
   - **Accept:** Incorporate directly into v2
   - **Partially accept:** Incorporate with modification, noting why
   - **Reject with justification:** Document why the amendment is not incorporated
   - **Defer:** Mark for future revision (e.g., requires additional research)
2. **Parallel revision.** Revise papers in parallel, following the same phasing as composition:
   - Tool: Parallel Claude Code sessions with TRP review + v1 paper as context
   - Method: Each session addresses all amendments for its paper
3. **Revision log.** Maintain a revision log per paper documenting what changed and why. This is the audit trail for TRP compliance.
4. **Re-review trigger.** If revisions are substantial (>30% of paper content changed, or fundamental argument restructured), trigger a re-review (Stage 5 again, possibly with a modified panel).

**Outputs:**
- Revised papers (v2)
- Revision logs (per paper)
- Re-review flags (if triggered)

**Quality gate:** Every critical amendment must be addressed (accepted, partially accepted, or rejected with justification). No amendment may be silently ignored.

---

## Stage 7: PUBLICATION (arXiv, Journal, and Wikipedia Contributions)

**Purpose:** Prepare reviewed papers for external publication and community contribution.

**Inputs:**
- Revised papers (v2) from Stage 6
- arXiv metadata requirements
- Journal submission guidelines
- Wikipedia article assessment

**Process:**
1. **arXiv preparation.** For each paper targeted for arXiv:
   - Prepare submission metadata (title, abstract, categories, keywords, MSC codes)
   - Convert from Markdown to LaTeX (or use pandoc pipeline)
   - Verify abstract length (under 1920 characters)
   - Prepare acknowledgments (AI assistance disclosed transparently)
   - Run submission checklist
   - Plan submission sequence (order matters -- earlier papers establish credibility for later ones)
2. **Journal targeting.** For papers suitable for peer review:
   - Identify target journal based on paper domain and scope
   - Draft cover letter
   - Format per journal requirements
3. **Wikipedia contributions.** For topics where Wikipedia coverage is thin:
   - Identify articles that would benefit from the research
   - Draft contributions following Wikipedia's WP:RS and WP:OR policies
   - Ensure all contributions cite published sources (not the programme's own papers until they are published)

**Outputs:**
- arXiv submission packages (metadata, abstract, checklist, cover letter)
- Journal submission packages
- Wikipedia contribution drafts

**Quality gate:** All submission checklists must pass. AI assistance must be disclosed. No institutional affiliation claims beyond actual affiliation.

---

## Stage 8: IMPLEMENTATION (Manifest Extraction and System Changes)

**Purpose:** Extract actionable design recommendations from the research and implement them as governance documents, code changes, and system modifications.

**Inputs:**
- All reviewed papers (especially design recommendations, implications sections)
- TRP reviews (especially amendments and expansions)
- Existing ORGANVM governance corpus and codebase

**Process:**
1. **Manifest extraction.** Systematically scan all papers and reviews for actionable recommendations:
   - For each paper section, ask: "Does this recommend a change to ORGANVM?"
   - Classify by category (GOVERNANCE, MEASUREMENT, NAMING, ARCHITECTURE, TOOLING, PROCESS)
   - Prioritize: P0 (foundational, must be done first), P1 (important, clear value), P2 (enhancement)
   - Estimate effort: S (hours), M (days), L (weeks), XL (months)
   - Map dependencies between tasks
   - Record source traceability (paper + section + recommendation)
2. **Implementation manifest.** Produce a comprehensive manifest document:
   - Total task count and breakdown by priority/category/effort
   - Implementation sequence (phased, respecting dependencies)
   - Cross-cutting concerns
   - Source traceability appendix
3. **Governance document creation.** For P0 tasks that are documentation-only:
   - Write governance declarations, specifications, and classifications
   - Follow the established pattern: date-prefixed filenames, ENACTED status, source traceability, cross-references
   - Place in `praxis-perpetua/governance/`
4. **Code change tickets.** For tasks requiring code changes:
   - Create detailed implementation specifications
   - Reference manifest task IDs
   - Target specific files in organvm-engine or other codebases

**Outputs:**
- Implementation manifest (IMPLEMENTATION-MANIFEST.md)
- Governance documents (in `praxis-perpetua/governance/`)
- Code change specifications
- Research registry updates (RESEARCH-REGISTRY.yaml)

**Quality gate:** Every manifest task must have source traceability back to a specific paper section. Every P0 governance document must follow the established template pattern.

---

## Stage 9: FEEDBACK (Empirical Data and Spiral Continuation)

**Purpose:** Collect empirical data from implementation, feed it back into the research, and plan the next iteration of the spiral.

**Inputs:**
- Implementation results from Stage 8
- System metrics before and after changes
- Session retrospective
- Open questions from TRP reviews

**Process:**
1. **Empirical data collection.** After implementation:
   - Run `organvm governance audit` to measure governance health
   - Run `organvm metrics calculate` to capture system metrics
   - Compare before/after metrics for implemented changes
   - Document what worked and what did not
2. **Paper revision triggers.** Implementation experience may reveal:
   - Theoretical claims that do not survive contact with practice
   - New implications not anticipated in the papers
   - Validation data for or against the papers' predictions
   - These trigger v3 revisions or new papers
3. **Session retrospective.** Document:
   - What was accomplished (quantified)
   - What worked well in the pipeline
   - What could improve
   - Lessons for next session
   - Open items and next actions
4. **Spiral continuation.** The feedback stage connects back to Stage 1:
   - New questions discovered during implementation become new Genesis material
   - Revised papers may need re-review (back to Stage 5)
   - New governance documents may trigger new research (back to Stage 2)
   - The spiral is indefinite -- each cycle deepens the system

**Outputs:**
- Empirical data reports
- Paper revision triggers
- Session retrospective (SESSION-RETROSPECTIVE-YYYY-MM-DD.md)
- Updated research registry
- Next-cycle research agenda

**Quality gate:** The session retrospective must be written. Open items must be tracked. The research registry must be updated to reflect current status.

---

## Pipeline Metrics

Track these metrics across programme executions to assess pipeline health:

| Metric | Description | Target |
|--------|-------------|--------|
| Adventures-to-papers ratio | How many adventures produce papers | > 0.8 |
| TRP amendment acceptance rate | Fraction of amendments accepted or partially accepted | > 0.7 |
| P0 completion rate | Fraction of P0 manifest tasks completed per cycle | > 0.5 per session |
| Cross-reference consistency | Fraction of cross-references that resolve | 1.0 |
| Source traceability coverage | Fraction of manifest tasks with full source traceability | 1.0 |
| Revision-to-re-review ratio | Fraction of v2 papers triggering re-review | 0.1 - 0.3 (too low = insufficient scrutiny; too high = insufficient initial quality) |
| Words per agent-hour | Throughput of composition stage | Track trend, not absolute |
| Governance docs per cycle | Count of enacted governance documents per pipeline cycle | Track trend |

---

## Tool Reference

| Stage | Primary Tools | Secondary Tools |
|-------|--------------|-----------------|
| GENESIS | `alchemia intake`, `sqlite3`, `alchemia synthesize` | `organvm session transcript` |
| EXPANSION | Wikipedia MCP (`search_wikipedia`, `get_article`, `get_sections`, `get_links`), `perplexity_research`, `tavily_research` | `get_related_topics`, `summarize_article_for_query` |
| FORMALIZATION | Text editor, `organvm registry show` | Dependency graph visualization |
| COMPOSITION | Parallel Claude Code sessions, `Read`/`Write` tools | `organvm context sync` for cross-repo context |
| REVIEW | TRP SOP, parallel Claude Code sessions (one per POV) | `faculty-registry.yaml` for panel constitution |
| REVISION | Parallel Claude Code sessions, diff tools | `git diff` for revision tracking |
| PUBLICATION | `pandoc` (Markdown to LaTeX), arXiv submission UI | Journal submission portals |
| IMPLEMENTATION | `Read`/`Write`/`Edit` tools, `organvm` CLI suite | `pytest`, `ruff` for code changes |
| FEEDBACK | `organvm governance audit`, `organvm metrics calculate` | `organvm session review` |

---

## Anti-Patterns

These failure modes were observed or anticipated during the SGO-2026 programme:

1. **Scope inflation.** Adventures that expand beyond their central question, pulling in adjacent topics without boundary discipline. Mitigation: enforce the domain signature declared at adventure start.
2. **Echo-chamber review.** TRP panels where all three POVs share the same disciplinary background. Mitigation: require non-overlapping expertise sets in panel constitution.
3. **Amendment amnesia.** TRP amendments that are acknowledged in the synthesis but silently dropped during revision. Mitigation: revision logs with per-amendment disposition.
4. **Parallel drift.** Papers drafted in parallel that develop inconsistent terminology or contradictory claims. Mitigation: cross-paper consistency review after each composition phase.
5. **Implementation without research.** Governance changes implemented without theoretical grounding. Mitigation: every manifest task must trace to a paper section.
6. **Research without implementation.** Papers that recommend changes but never trigger system modifications. Mitigation: mandatory manifest extraction at Stage 8.
7. **Cross-cultural blind spots.** Research claims that are Western-centric without acknowledging non-Western traditions (caught by TRP in SYN-01). Mitigation: require typological diversity in linguistic claims; require cross-cultural consideration in governance claims.

---

## Cross-References

- **SGO-2026-SOP-001:** Triadic Review Protocol (Stage 5 operating procedure)
- **SOP: The Gold Path:** Research-to-implementation pipeline (Stage 8 alignment)
- **2026-03-21-governance-trilemma-declaration.md:** First governance document produced by this pipeline
- **2026-03-21-syntactic-semantic-boundary.md:** Second governance document produced by this pipeline
- **2026-03-21-naming-convention-spec.md:** Third governance document produced by this pipeline
- **IMPLEMENTATION-MANIFEST.md:** Stage 8 output of the SGO-2026 programme
- **RESEARCH-REGISTRY.yaml:** Programme registration (Stage 3 output)
- **SESSION-RETROSPECTIVE-2026-03-21.md:** Stage 9 output of the SGO-2026 programme

---

*This SOP documents a process that was executed before it was formalized. The formalization is itself a Stage 8 output -- extracting the implicit pipeline into an explicit, repeatable process. Future programmes should follow this SOP from Stage 1; the SGO-2026 programme discovered it by doing it.*
