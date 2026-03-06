# IGNITION Sprint — Implementation Plan

## Context

**Previous sprint:** PROPULSION (2026-02-12) promoted 17 PROTOTYPE repos to PRODUCTION, fixed all stale numbers across 15+ application files, and deployed everything to remote. Current state: **64 PRODUCTION, 1 PROTOTYPE, 3 SKELETON, 13 DESIGN_ONLY** (81 total, 17 essays published, ~320K words).

**Problem:** The system is internally strong but externally underexposed. The portfolio website (`4444J99/portfolio`) still shows "78 repositories" and "~289K words". Zero applications have been submitted despite all materials being ready. 11 planned essays remain unwritten. Dependabot PRs are accumulating across 81 repos. The Google Creative Fellowship deadline is **March 18, 2026** (34 days).

**Goal:** Maximum external visibility — fix the public-facing portfolio site, write high-impact essays that strengthen applications, triage infrastructure debt, and position the user to begin submitting applications immediately.

---

## Phase 0: Portfolio Site — Fix Public-Facing Numbers (~30 min)

The portfolio site at `4444J99/portfolio` (Astro-based, GitHub Pages) is the most visible external asset and contains stale numbers.

### 0A. Fix `about.astro`
**File:** `4444J99/portfolio/src/pages/about.astro`
- "across 78 repositories" → "across 81 repositories"
- Any other stale references (289K, 10 essays, etc.) — full audit on read

### 0B. Fix `resume.astro`
**File:** `4444J99/portfolio/src/pages/resume.astro`
- "coordinating 78 repositories" → "coordinating 81 repositories"
- "~289K words" → "~320K words"
- Any references to essay counts, PRODUCTION counts, CI coverage

### 0C. Audit remaining portfolio pages
- `src/pages/index.astro` — check for stale numbers
- `src/pages/projects/` — check project descriptions reference current counts
- Deploy via `gh api repos/4444J99/portfolio/contents/<path> --method PUT`

**Verification:** After deploy, wait for GitHub Pages rebuild, then check live site for updated numbers.

---

## Phase 1: Essay Blitz — 3 High-Impact Essays (~2-3 hours)

### Rationale
17 essays → 20 essays crosses a psychological threshold ("20+ published essays"). Each essay adds ~4,000-5,000 words to the corpus (~320K → ~335K). More importantly, specific essays directly strengthen pending applications.

### Essay Selection (from public-process-map-v2.md backlog)

**Essay 18 (already scheduled Feb 13):** "Why AI Function Calling Needs Ontological Grounding"
- Already written and deployed as `2026-02-13-why-ai-function-calling-needs-ontological-grounding.md`
- Will auto-publish on Feb 13 — no action needed, but count will become 18

**Essay 19: "The Meta-System as Portfolio Asset"**
- **Why now:** This essay directly addresses how the 8-organ system functions as a portfolio for AI roles, grants, and residencies. It's the essay most likely to be linked in applications.
- **Audience:** Hiring managers, grant reviewers
- **Organs touched:** IV (orchestration), V (public process), Meta
- **Deploy to:** `organvm-v-logos/public-process/_posts/2026-02-12-the-meta-system-as-portfolio-asset.md`

**Essay 20: "Building in Public: Why Transparency Is an Engineering Decision"**
- **Why now:** Developer advocacy roles (HuggingFace, Together AI) value "building in public" as a practice. This essay makes the case that ORGAN-V's transparency is deliberate engineering, not performance.
- **Audience:** DevRel hiring managers, open-source community
- **Organs touched:** V (public process), IV (governance)
- **Deploy to:** `organvm-v-logos/public-process/_posts/2026-02-13-building-in-public-why-transparency-is-an-engineering-decision.md`

**Essay 21: "Recursive Engines at Scale: What 1,254 Tests Taught Me About Symbolic Systems"**
- **Why now:** The flagship ORGAN-I repo has the strongest test suite numbers in the entire system. This essay converts raw test metrics into a narrative about engineering rigor and recursive design.
- **Audience:** AI engineering hiring managers (Anthropic, OpenAI)
- **Organs touched:** I (theory), IV (orchestration)
- **Deploy to:** `organvm-v-logos/public-process/_posts/2026-02-14-recursive-engines-at-scale.md`

### Essay Generation Workflow (per essay)
1. Read the outline from `public-process-map-v2.md`
2. Read relevant repo READMEs and code for evidence
3. Generate 4,000-5,000 word essay with Jekyll front matter
4. Deploy to `organvm-v-logos/public-process/_posts/` via `gh api`
5. Update registry-v2.json: `meta_system_essays` count, `total_essay_words`

### Post-Essay Updates
- `registry-v2.json`: `meta_system_essays: 17` → `21`, `total_essay_words: 70000` → `90000`
- `00-portfolio-brief.md`: "17 published (~70K words)" → "21 published (~90K words)"
- All application materials: batch replace "17 meta-system essays" → "21 meta-system essays"
- Deploy updated files to remote

---

## Phase 2: Application QA — Evidence URL Audit + Google Fellowship Prep (~45 min)

### 2A. Evidence URL Audit
Every cover letter contains evidence links (GitHub repos, portfolio URLs). Verify each link resolves:
- Use `gh api repos/ORG/REPO` to verify each referenced repo exists and is public
- Check portfolio URL responds
- Flag any broken or private repos

**Files to audit:**
- `docs/applications/cover-letters/anthropic-fde-custom-agents.md`
- `docs/applications/cover-letters/anthropic-se-claude-code.md`
- `docs/applications/cover-letters/openai-se-applied-evals.md`
- `docs/applications/cover-letters/together-ai-lead-dx-documentation.md`
- `docs/applications/cover-letters/huggingface-dev-advocate-hub-enterprise.md`
- `docs/applications/cover-letters/cohere-applied-ai-agentic-workflows.md`
- `docs/applications/cover-letters/runway-mts-research-tooling.md`

### 2B. Google Creative Fellowship Prep
- Read `docs/applications/05-google-creative-lab-five-responses.md` for current state
- Check if responses are complete or need additional drafting
- Deadline: March 18, 2026 — flag any incomplete sections
- Output: list of TODO items for user to finalize before submission

### 2C. Application Tracker Update
- Update `docs/applications/04-application-tracker.md` with post-IGNITION status
- Mark materials as "READY TO SUBMIT" where applicable
- Deploy updated tracker to remote

---

## Phase 3: Infrastructure Hygiene — Stale Workflows + Dependabot Triage (~1-2 hours)

### 3A. Stale Workflow Cleanup
During PROPULSION, we found `a-recursive-root` had a stale `main.yml` (Node.js CI) alongside its real `ci.yml`. This pattern likely exists in other repos.

**Approach:**
1. Script to check all 81 repos for multiple workflow files: `gh api repos/ORG/REPO/contents/.github/workflows`
2. Identify repos with both `main.yml` (stale) and `ci-*.yml` (real) — delete stale ones
3. Identify repos with failing CI from stale workflows (not from real CI)
4. Delete stale workflows via `gh api --method DELETE`

### 3B. Dependabot PR Triage
Dependabot was deployed to all repos during ASCENSION. PRs are now accumulating.

**Approach:**
1. Enumerate open dependabot PRs across all 8 orgs
2. For each PR: check if CI passes → auto-merge via `gh api repos/ORG/REPO/pulls/N/merge --method PUT`
3. For failing PRs: triage (close if minor, flag if security-critical)
4. Target: merge 80%+ of passing dependabot PRs

### 3C. CI Coverage Push
Current: 67/81 repos (83%) have CI. Remaining 14 are mostly DESIGN_ONLY (.github profile repos) and ARCHIVED.

**Approach:**
1. Identify any non-DESIGN_ONLY, non-ARCHIVED repos without CI
2. Deploy `ci-minimal.yml` to any that qualify
3. Target: push CI count from 67 → 70+ (if eligible repos exist)

### 3D. Elevate nexus--babel-alexandria-
`organvm-i-theoria/nexus--babel-alexandria-` is HIGH relevance, DESIGN_ONLY — the only meaningfully elevatable non-PRODUCTION repo.

**Approach:**
1. Check current repo state (README exists? Code exists?)
2. If README-only: deploy a minimal Python package + `ci-python.yml`
3. Promote DESIGN_ONLY → SKELETON → PROTOTYPE (or straight to PRODUCTION if CI passes)
4. Update registry

---

## Phase 4: Post-Sprint Housekeeping (~15 min)

- Run validation scripts: `scripts/calculate-metrics.py`, `scripts/v4-dependency-validation.py`
- Update `CLAUDE.md` with post-IGNITION counts
- Update `MEMORY.md` with post-IGNITION state
- Git commit all local changes
- Deploy registry + CLAUDE.md to remote

---

## Execution Summary

| Phase | Effort | Deliverables | External Impact |
|-------|--------|-------------|----------------|
| 0: Portfolio site fix | 30 min | 3-5 files updated on live site | Public-facing numbers become accurate |
| 1: Essay blitz | 2-3 hrs | 3 new essays (→ 21 total, ~90K words) | Crosses "20+ essays" threshold |
| 2: Application QA | 45 min | All evidence URLs verified, tracker updated | Applications unblocked for submission |
| 3: Infrastructure | 1-2 hrs | Stale workflows removed, dependabot merged, CI ↑ | System health, security posture |
| 4: Housekeeping | 15 min | Validation green, docs current | Internal consistency |

**Total session scope:** ~5-6 hours of Claude work
**Human action items post-sprint:** Submit 7 AI role applications + Google Creative Lab Five

---

## Execution Order & Dependencies

```
Phase 0 (portfolio site)     ─┐
Phase 3A (stale workflows)    │──→ can run in parallel
Phase 3B (dependabot triage)  │
Phase 3C (CI push)           ─┘
         │
         ▼
Phase 1 (essay blitz)         ──→ sequential (essays reference up-to-date system state)
         │
         ▼
Phase 2 (application QA)      ──→ sequential (audits post-essay materials)
         │
         ▼
Phase 3D (nexus elevation)    ──→ can be interleaved
         │
         ▼
Phase 4 (housekeeping)        ──→ always last
```

Phase 0 and Phase 3A-C are independent and can run in parallel. Phase 1 should follow Phase 0 so essays reference accurate portfolio state. Phase 2 must follow Phase 1 so the evidence audit catches essay-updated materials.

---

## Verification

- After Phase 0: Live portfolio site shows "81 repositories", "~320K words"
- After Phase 1: `gh api repos/organvm-v-logos/public-process/contents/_posts` shows 21 essay files
- After Phase 1: `registry-v2.json` shows `meta_system_essays: 21`
- After Phase 2: All evidence URLs return HTTP 200 / valid `gh api` responses
- After Phase 3: `gh search prs --author dependabot --state open` count decreases by 80%+
- After Phase 3: CI coverage ≥ 70/81 repos
- After Phase 4: `python3 scripts/calculate-metrics.py` and `python3 scripts/v4-dependency-validation.py` both pass
