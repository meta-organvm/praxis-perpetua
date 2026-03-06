# SOP v2.0 — Document Audit & Feature Extraction (Universal)

## Context

The current SOP (`meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md`, 739 lines) was written from a single execution on Styx/ORGAN-III (52 authored docs → 74 issues, single repo). The ORGAN-IV execution (16 AI chat transcripts → 73 issues across 4 repos) exposed critical structural gaps:

- **70% first-pass coverage** → 30% of extractable content missed without a completeness proof
- **8 antagonistic tensions** between documents went completely undetected
- **5 under-extracted documents** (<60%) because chat transcripts need different heuristics
- **Multi-repo routing** was invented ad-hoc — not a first-class concern
- **Alchemical synthesis** (cross-cutting themes) produced the most valuable strategic output but wasn't in the SOP
- **No self-correction mechanism** — the SOP had no way to verify its own output quality

The user requests a universal revision usable "everywhere" — any organ, any document type, any repo topology.

---

## Target File

`/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/sop--document-audit-feature-extraction.md`

The v1 file is **replaced in-place** (not a new file). The v2 SOP supersedes v1 entirely.

---

## Structural Changes: v1 → v2

| Aspect | v1 (5 phases) | v2 (8 phases) | Rationale |
|--------|---------------|---------------|-----------|
| Source classification | Not present | Phase 0 | Misclassification cascades into under-extraction |
| Reading order | Folder-based only | Thematic cohort with folder fallback | Flat corpora have no folders |
| Multi-repo routing | Not present | Phase 0 deliverable | First-class concern, not afterthought |
| Completeness proof | Not present | **Mandatory gate** (Phase 3) | 30% of content missed without it |
| Tension detection | Not present | Phase 3 identification → Phase 4 resolution | 8/8 tensions missed in v1 |
| Synthesis | Not present | Dedicated Phase 5 | Most strategically valuable output |
| Coverage thresholds | None | 80% overall, 50% per-document | Prevents the 70% first-pass problem |
| Agent allocation | Fixed (5 for 20+) | Scaled by corpus size AND density | 16 docs needed 2-3, not 5 |
| SYLLABUS variant | Academic only | Academic / Tooling / Mixed / None | Tools ≠ books |
| Self-improvement | Not present | Retrospective + amendment protocol | Living document that learns |
| Issue creation rate | Unspecified | Sequential with 2s delay | GitHub API 502 prevention |
| Appendices | A-E | A-J (5 new) | Document types, routing, completeness, SYLLABUS variants, retrospective |

---

## v2 Phase Architecture

### Phase 0 — Scope & Classify (NEW, ~15 min)

**Purpose**: Determine WHAT the corpus is before reading it.

Deliverables:
1. **Scope declaration**: single-repo / multi-repo / cross-organ; trigger (onboarding, quarterly, pre-beta, post-mortem)
2. **Document type classification** with heuristic selection per type:
   - Authored docs → v1 heuristics ("We could...", "Future work", "Risk: ...")
   - AI chat transcripts → numbered lists, named tools, "strategic gap", statistical claims, roadmaps
   - Reference books → chapter summaries, framework applications, case studies
   - RFCs/ADRs → "Consequences", rejected alternatives, open questions
   - Code/wiki → TODO/FIXME, deprecated patterns, roadmap sections
3. **Issue routing table** (if multi-repo): category → target repo → label. Template from ORGAN-IV MANIFEST.md lines 15-29
4. **Agent allocation plan**: corpus size × density → agent count
   - 5-15 docs: 1-2 agents
   - 15-40 docs: 2-3 agents (thematic cohort split)
   - 40-100 docs: 3-5 agents
   - 100+: 5 max, sequential cohort batches
5. **Disabled-issues routing overrides**: if any target repo has issues disabled, document the redirect

### Phase 1 — Inventory & Triage (REVISED, ~15-30 min)

**Changes from v1**:
- Reading order decision tree: folders (if meaningful subdirs) OR thematic cohorts (if flat/mixed)
- **Source clustering**: group documents sharing the same prompt, topic, or generation session. Mark clusters for aggressive dedup in Phase 4 (expect 30-50% overlap within clusters)
- **Density estimation** per document: word count / line count ratio. Flag high-density docs (>15 extractable items per 100 lines) for double-read in Phase 2
- MANIFEST.md gains: cohort assignment, density flag, source cluster ID, document type

Deliverables: MANIFEST.md with DOC-IDs, cohorts, clusters, density flags, conversion status

### Phase 2 — Exhaustive Read & Extraction (REVISED, ~1-3 hrs)

**Changes from v1**:
- Multiple extraction heuristic sets selected by document type (Appendix F)
- **Density-aware reading**: high-density flagged docs get a within-Phase-2 second read (not the completeness proof — that's Phase 3)
- Per-document **coverage self-estimate** by the reading agent: "I estimate I captured N of ~M extractable items in this document (~X%)"
- Documents with self-estimated coverage <70% get immediate re-read within Phase 2

Deliverables: Extraction list (EXT-NNN entries) with per-document coverage estimates

### Phase 3 — Completeness Proof (NEW, mandatory gate, ~1-2 hrs)

**The single most important v2 addition.** This phase uses fresh agents (NOT the Phase 2 agents) to re-read every document adversarially.

Activities:
1. Assign 1-2 fresh agents to re-read all documents line-by-line
2. Produce per-document coverage table: total items, covered items, coverage %
3. Classify gaps: OBVIOUS (should have been caught) vs NON-OBVIOUS (cross-document inference)
4. Detect **antagonistic tensions**: where documents disagree. Format: Pole A, Pole B, classification (COMPLEMENTARY / CONTEXT-DEPENDENT / TEMPORAL / DATA-QUALITY-ISSUE / NUANCED / UNRESOLVED)
5. Produce gap register with recommended actions

**GATE CRITERIA** (must pass before proceeding):
- Overall coverage ≥ 80%
- No document below 50% without documented justification
- All antagonistic tensions identified and classified

If gate fails → return to Phase 2 for targeted re-extraction → re-run Phase 3.

Deliverables: Completeness proof document, gap register, antagonistic tension register, remediation extractions

### Phase 4 — Deduplication & Tension Resolution (REVISED, ~1-2 hrs)

**Changes from v1**:
- Operates on the FULL extraction set (Phase 2 + Phase 3 remediation), not a partial set
- **Tension resolution** integrated into dedup: when comparing extractions, classify as DUPLICATE (merge), COMPLEMENT (merge both), or ANTAGONIST (flag + resolve)
- Resolution types: COMPLEMENTARY, CONTEXT-DEPENDENT, TEMPORAL, DATA-QUALITY-ISSUE, NUANCED, UNRESOLVED
- Source-cluster dedup: docs in same cluster get aggressive merge (30-50% overlap expected)
- Classification: SKIP / ENHANCE / CREATE (unchanged) + TENSION (new — creates issue with both poles + resolution)

Deliverables: Deduplicated candidate list with routing + resolved tension register

### Phase 5 — Synthesis (NEW, ~30-60 min)

**Purpose**: Identify emergent strategic themes that no single issue captures.

Activities:
1. Identify cross-cutting themes spanning 3+ documents or 2+ repos
2. For each theme: name, source citations, convergence description, strategic implication
3. Map theme dependencies (requires / enables / conflicts)
4. Produce recommended execution order
5. Integrate antagonistic tensions as a named theme
6. Compile statistical/risk data appendix if present in corpus

Deliverables: Synthesis document (themes, dependency map, execution order, risk data appendix)

### Phase 6 — Issue Creation (MOVED from v1 Phase 4, ~1-3 hrs)

**Changes from v1**:
- Multi-repo routing from Phase 0 routing table
- **Sequential creation** with ≥2s delay between API calls (prevents 502 errors)
- Issue body template gains "Tensions" section for antagonistic positions
- ENHANCE comment template gains completeness-proof provenance
- Thematic grouping retained (by category, not source document)
- Running tally by target repo (not by folder)

Deliverables: Created issues with tally, enhanced existing issues

### Phase 7 — Post-Audit Artifacts (MOVED from v1 Phase 5, expanded, ~30-60 min)

**Changes from v1**:
- SYLLABUS variant selection (from Phase 0): Academic / Tooling / Mixed / None (Appendix I)
- **Mandatory artifacts** (all committed):
  1. MANIFEST.md (updated)
  2. FEATURE-BACKLOG.md (with all F-IDs)
  3. SYLLABUS.md (variant per Phase 0)
  4. Synthesis document (from Phase 5)
  5. Completeness proof (from Phase 3)
  6. Audit summary with retrospective
- **Retrospective section** in audit summary: what worked, what didn't, what the SOP should change
- **SOP amendment protocol**: executor files amendment recommendations → SOP maintainer reviews and incorporates

Deliverables: All artifacts committed, retrospective filed

---

## New Appendices

| ID | Title | Content |
|----|-------|---------|
| F | Document Type Heuristics | Extraction signal tables per type: authored, transcript, reference, RFC/ADR, code, wiki |
| G | Multi-Repo Routing Guide | Routing table template, disabled-issues handling, cross-organ routing rules, label creation |
| H | Completeness Proof Methodology | Coverage calculation formula, gap classification scheme (S/R/P/A/L/N series), tension detection protocol, gate criteria |
| I | SYLLABUS Variants | Templates for academic, tooling, and mixed variants with section headers |
| J | Retrospective Template | What worked, what failed, timing accuracy, SOP amendment recommendations |

Appendices A-E unchanged (format conversion, issue template, agent guide, non-docs repos, governance cross-ref). Appendix B gains a "Tensions" section. Appendix C revised for density-aware agent allocation.

---

## Light Mode (Corpora ≤ 10 Documents)

For small corpora, phases collapse:
- Phase 0+1 merge into a single inventory step (10 min)
- Phase 2+3 can use the same agent if it re-reads adversarially with explicit "what did I miss?" pass (no separate agent needed)
- Phase 4+5 merge: dedup and synthesis happen in one pass
- Phase 6+7 remain separate (issue creation is mechanical, artifacts are structural)

Total: ~4 collapsed phases instead of 8. Same deliverables, lighter ceremony.

---

## Quick Reference Card

```
╔══════════════════════════════════════════════════════════════╗
║  DOCUMENT AUDIT & FEATURE EXTRACTION v2.0 — QUICK REF      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  PHASE 0: SCOPE & CLASSIFY                                   ║
║  □ Determine scope (single/multi-repo)                       ║
║  □ Classify document types → select heuristics               ║
║  □ Build routing table (if multi-repo)                       ║
║  □ Plan agent allocation (size × density)                    ║
║                                                              ║
║  PHASE 1: INVENTORY & TRIAGE                                 ║
║  □ List all files, classify format + readability             ║
║  □ Assign thematic cohorts OR folder order                   ║
║  □ Cluster shared-prompt/shared-topic docs                   ║
║  □ Flag high-density docs for double-read                    ║
║  □ Build MANIFEST.md                                         ║
║                                                              ║
║  PHASE 2: READ & EXTRACT                                     ║
║  □ Read EVERY document word-for-word                         ║
║  □ Use type-specific heuristics (Appendix F)                 ║
║  □ Double-read high-density flagged docs                     ║
║  □ Self-estimate coverage per document                       ║
║                                                              ║
║  ★ PHASE 3: COMPLETENESS PROOF (mandatory gate)              ║
║  □ Fresh agents re-read all docs adversarially               ║
║  □ Coverage table per document                               ║
║  □ Detect antagonistic tensions between docs                 ║
║  □ GATE: ≥80% overall, ≥50% per-doc, all tensions IDed      ║
║  □ If gate fails → return to Phase 2 for re-extraction       ║
║                                                              ║
║  PHASE 4: DEDUP & TENSION RESOLUTION                         ║
║  □ Cross-ref: backlog + issues + codebase                    ║
║  □ Merge source-cluster overlaps (30-50% expected)           ║
║  □ Classify: SKIP / ENHANCE / CREATE / TENSION               ║
║  □ Resolve each tension with classification                  ║
║                                                              ║
║  PHASE 5: SYNTHESIS                                          ║
║  □ Identify cross-cutting themes (3+ docs or 2+ repos)       ║
║  □ Map theme dependencies + execution order                  ║
║  □ Integrate tensions as a named theme                       ║
║  □ Compile risk data appendix (if applicable)                ║
║                                                              ║
║  PHASE 6: CREATE ISSUES                                      ║
║  □ Route by Phase 0 routing table                            ║
║  □ Sequential creation (≥2s delay)                           ║
║  □ Include tensions in issue body where relevant             ║
║  □ Batch by category, maintain running tally                 ║
║                                                              ║
║  PHASE 7: POST-AUDIT ARTIFACTS                               ║
║  □ MANIFEST.md, FEATURE-BACKLOG.md, SYLLABUS.md (variant)   ║
║  □ Synthesis document + completeness proof                   ║
║  □ Audit summary with retrospective                          ║
║  □ File SOP amendment recommendations                        ║
║  □ Commit + push                                             ║
║                                                              ║
║  GATE THRESHOLDS                                             ║
║  Overall coverage: ≥80%   Per-document floor: ≥50%           ║
║  All antagonistic tensions: identified + classified           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Implementation Plan

### Step 1: Archive v1
- Copy current SOP to `docs/operations/archive/2026-03/sop--document-audit-feature-extraction-v1.md`
- Create `archive/2026-03/` directory if it doesn't exist

### Step 2: Write v2 SOP
- Overwrite `sop--document-audit-feature-extraction.md` with v2 content
- Structure: Header + ToC + 8 phases (0-7) + 10 appendices (A-J) + Quick Reference Card
- Retain v1's prose quality — the v1 SOP reads well and the voice should be preserved
- Retain v1 content that is unchanged: Appendix A (format conversion), Appendix D (non-docs repos), Appendix E (governance cross-ref), the pre-audit checklist pattern, the `gh` command examples
- Port v1's issue body template (Appendix B) with new "Tensions" section added
- Revise v1's Appendix C (parallelization) with density-aware agent allocation
- Write 5 new appendices (F-J)

### Step 3: Update cross-references
- Update `key-workflows.md` workflow #7 to reference the 8-phase structure
- Update `concordance.md` if it references audit phase numbers
- Update the ORGAN-IV `research/audit-summary--2026-03-06.md` to note the SOP has been updated based on its recommendations

### Step 4: Commit
```bash
cd /Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm
git add docs/operations/sop--document-audit-feature-extraction.md
git add docs/operations/archive/
git commit -m "docs: SOP v2.0 — Document Audit & Feature Extraction (universal)

8-phase architecture with mandatory completeness proof gate.
Derived from ORGAN-III (Styx) and ORGAN-IV (Taxis) execution runs.

Key additions: source classification, completeness proof (Phase 3),
antagonistic tension detection, synthesis phase, multi-repo routing,
coverage thresholds (80%/50%), SYLLABUS variants, self-improvement loop.

New appendices F-J: document type heuristics, multi-repo routing,
completeness proof methodology, SYLLABUS variants, retrospective template."
```

### Step 5: Update ORGAN-IV audit summary
```bash
cd /Users/4jp/Workspace/organvm-iv-taxis
# Add note to audit-summary that SOP was updated based on its recommendations
git commit -m "docs: note SOP v2.0 update in audit summary"
```

---

## Verification

After writing the v2 SOP, verify:
- [ ] All 8 phases documented with inputs, activities, outputs
- [ ] All 10 appendices present (A-J)
- [ ] Quick reference card updated for v2
- [ ] Coverage gate criteria explicitly stated (80%/50%)
- [ ] Light mode guidance for ≤10 doc corpora
- [ ] Multi-repo routing table template included
- [ ] All 5 document type heuristic tables in Appendix F
- [ ] Retrospective template in Appendix J
- [ ] v1 archived (not deleted)
- [ ] Cross-references in key-workflows.md updated
- [ ] Colophon notes both execution runs (Styx + ORGAN-IV) as empirical basis

---

## Estimated Size

v1: 739 lines. v2 target: ~1,100-1,300 lines (3 new phases + 5 new appendices + light mode + expanded quick ref). The added length is justified by the completeness proof methodology and document type heuristics, which are the highest-value additions.
