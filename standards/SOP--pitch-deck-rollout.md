# SOP: Pitch Deck Generation & Rollout

## 1. Ontological Purpose

This SOP governs the creation, deployment, and maintenance of pitch decks for every eligible repository across the ORGANVM ecosystem. A pitch deck is a **single-page web artifact** (hosted via GitHub Pages) that presents a project's purpose, problem space, solution, and positioning within the organ system.

The ecosystem uses a **two-track system**:
- **Auto-generated** — the `organvm-engine` pitch CLI produces single-file HTML decks from structured data (README, seed.yaml, registry, pitch.yaml), themed per-organ.
- **Bespoke** — hand-crafted SPAs with custom code, animations, and narrative for repos that warrant the investment.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 4: Operations & Delivery)
**Cross-reference:** `SOP--repo-onboarding-and-habitat-creation.md` (pitch generation is part of onboarding Phase V)

---

**Created:** 2026-03-04
**Author:** @4444j99 (AI-conductor model: human directs, AI generates, human reviews)
**Status:** ACTIVE — Living document, updated as process evolves
**Canonical location:** `praxis-perpetua/standards/SOP--pitch-deck-rollout.md`
**Companions:** [`key-workflows.md`](../../organvm-corpvs-testamentvm/docs/operations/key-workflows.md) (procedures), [`operational-cadence.md`](../../organvm-corpvs-testamentvm/docs/operations/operational-cadence.md) (rhythm), [`minimum-viable-operations.md`](../../organvm-corpvs-testamentvm/docs/operations/minimum-viable-operations.md) (maintenance)
**Precedent:** `organvm-iii-ergon/peer-audited--behavioral-blockchain` — first bespoke implementation
**Toolchain:** `organvm-engine` pitch CLI (`meta-organvm/organvm-engine/src/organvm_engine/pitchdeck/`)

---

## 2. Trigger Conditions

| Trigger | Description |
|---------|-------------|
| **New repo onboarding** | When a repo is added to the registry and has at least a README |
| **Promotion to PUBLIC_PROCESS** | When a repo's promotion status advances — it now faces external audiences |
| **Pre-launch / Pre-fundraise** | Before public launch or investor outreach for commercial products |
| **Quarterly sync** | Part of the monthly review cycle |
| **README major edit** | When a repo's Problem/Solution/Features sections are substantially rewritten |
| **Organ aesthetic update** | When `organ-aesthetic.yaml` or `themes.py` palettes change |

---

## 3. Phase I: Pitch Deck Tiers

Every repo is classified into one of four tiers:

### Tier 0: Excluded (No Pitch Deck)
**Criteria:** `infrastructure` tier, `ARCHIVED` promotion status, governance-only repos, `.github` org config repos.
**Action:** Skipped during sync.

### Tier 1: Auto-Generated (Default)
**Criteria:** Any `standard` or `flagship` tier repo with at least a description.
**Expected volume:** ~70% of eligible repos.
**Tooling:** `organvm pitch generate <repo>`
**Output:** Single-file HTML at `docs/pitch/index.html` (~60-80KB)

### Tier 2: Enhanced Auto-Generated (pitch.yaml Override)
**Criteria:** Repos needing richer content than README alone.
**Expected volume:** ~15-20% of eligible repos.
**Tooling:** Same CLI; reads `pitch.yaml` for content overrides.

### Tier 3: Bespoke (Custom Application)
**Criteria:** Flagship with active fundraising, interactive product demo, narrative complexity > 7 sections, or external audience.
**Expected volume:** 3-5 repos ecosystem-wide.
**Tooling:** Custom build pipeline per repo (Vite/React, Next.js static export, etc.)

---

## 4. Phase II: Readiness Audit

### Process

1. **Verify registry entry:** Target repo(s) have entry in `registry-v2.json` with `tier`, `org`, `tech_stack` populated. ORGAN-III repos need `revenue_model` and `revenue_status`.
2. **Verify seed.yaml:** Exists in repo root with `organ`, `tier`, `promotion_status`. Produces/consumes edges declared if applicable.
3. **Verify organ-aesthetic.yaml:** Organ directory has `.github/organ-aesthetic.yaml`. Palette exists in `themes.py` (`ORGAN_PALETTES` dict).
4. **Engine health check:**
   ```bash
   organvm pitch generate --repo <target-repo> --dry-run
   ```
5. **GitHub Pages eligibility:** Repo has (or can create) `docs/` directory. No existing `docs/pitch/index.html` that would be unintentionally clobbered.

### Starter Research Questions
- Does this repo have enough content for a meaningful pitch?
- Is the README structured with standard sections (Problem, Solution, Features, Architecture)?
- Does the organ palette exist in themes.py?
- Will GitHub Pages work for this repo's org?

---

## 5. Phase III: README Section Standardization

### Process

1. **Audit required sections:** What This Is, Problem, Solution, Key Features, Architecture. Parser recognizes aliases (e.g., "Motivation" = "Problem").
2. **Apply section writing guidelines:**
   - Problem: Lead with quantified pain point, 3 cards max, bold title + em-dash pattern
   - Solution: First sentence = elevator pitch
   - Features: 4-6 items, action-oriented titles
   - Architecture: Lead with tech stack keywords
3. **Run audit script:**
   ```bash
   organvm pitch audit-readmes [--organ III] [--fix-suggestions]
   ```

### Starter Research Questions
- Which sections are missing vs. thin vs. adequate?
- Is the README written for the pitch audience (stakeholders, grant reviewers)?
- Does the problem section quantify the pain?
- Does the solution section close the narrative loop?

---

## 6. Phase IV: pitch.yaml Authoring (Tier 2 Only)

### Process

1. **Create `pitch.yaml`** in repo root for repos needing richer content than README provides.
2. **Data assembly priority:** `pitch.yaml > seed.yaml > registry > README` — each fills only empty fields.
3. **Validate:**
   ```bash
   organvm pitch validate <repo>
   ```

Schema includes: `display_name`, `tagline`, `description`, `problem[]`, `solution`, `features[]`, `architecture`, `tech_stack[]`, market fields (ORGAN-III only), link fields, and bespoke configuration.

---

## 7. Phase V: Auto-Generation

### Process

1. **Dry run first:**
   ```bash
   organvm pitch sync --organ ORGAN-III --dry-run
   ```
2. **Review dry run output:** Verify generated count, bespoke list, skipped list, error count.
3. **Single-repo test:** Test one repo per organ before batch generation.
4. **Batch generation by organ:**
   ```bash
   organvm pitch sync --organ ORGAN-I
   organvm pitch sync --organ ORGAN-II
   # ... etc.
   ```
5. **Post-generation verification:** Count generated files, verify PITCH_MARKER, check file sizes (40-80KB each).

### Starter Research Questions
- Does the dry run report match expectations?
- Are all bespoke repos correctly excluded?
- Do CTA links resolve?
- Is the deck responsive at 375px, 768px, 1024px?

---

## 8. Phase VI: Bespoke Deck Development

For repos qualifying for Tier 3 (flagship with fundraising, interactive demo, complex narrative, external audience).

### Process

1. **Bespoke narrative structure:** Hero, Problem, Solution, Differentiation, Risk Mitigation, Market (ORGAN-III), Competitive Landscape (ORGAN-III), Business Model (ORGAN-III), Platform Economics (ORGAN-III), Technical Stack, Team/Capability, CTA.
2. **Technical patterns:** React 18 + Vite + TypeScript strict mode, Tailwind CSS, p5.js for procedural animations, single `slides.ts` data file.
3. **Registration:** Add to `BESPOKE_REPOS` in `sync.py`, add `pitch.type: bespoke` to `seed.yaml`.
4. **Verify** output does NOT contain `PITCH_MARKER`.

---

## 9. Phase VII: Deployment & Hosting

### Process

1. **GitHub Pages configuration:** Repo Settings > Pages, Source: branch `main`, directory `/docs`.
2. **Output path:** `docs/pitch/index.html` (default) or `docs/index.html` (bespoke root).
3. **Deployment verification:** URL loads, assets load, navigation works, responsive, `prefers-reduced-motion` respected, Lighthouse a11y > 90.

---

## 10. Phase VIII: CI/CD Integration

### Process

1. **Per-repo CI (auto-generated):** GitHub Actions step to generate, verify marker, commit if changed with `[skip ci]`.
2. **Per-repo CI (bespoke):** Build step only — output managed manually.
3. **Ecosystem-wide sync:** Weekly Monday 6 AM UTC via scheduled workflow in meta-organvm.

---

## 11. Phase IX: Quality Gates & Review

### Auto-generated checks
HTML validity, link integrity, Lighthouse >= 90, content completeness, file size < 100KB, marker present, organ palette correct.

### Bespoke checks (additional)
Build succeeds, TypeScript passes, bundle < 500KB gzipped, narrative coherence, 60 FPS animation, mobile responsive, reduced motion, constants accuracy.

---

## 12. Phase X: External Submission Pipeline

Pitch deck (internal) -> Submission Script (external) -> Target Platform. Conversion adapts tone to VC/press/accelerator audience, strips internal terminology, adds platform-specific formatting.

---

## 13. Organ-Specific Guidelines

Each organ has distinct palette, typography, and tone. Auto-generator applies via `themes.py`; bespoke decks conform manually. See organ palette table in the original SOP for full color/font mapping.

---

## 14. Maintenance & Sync Cadence

| Event | Action |
|-------|--------|
| Weekly (Monday 6AM UTC) | `pitch sync` via CI |
| seed.yaml/README/pitch.yaml change | `pitch generate <repo>` via CI |
| Registry update | `pitch sync` affected repos |
| Organ aesthetic change | `pitch sync --organ <N>` |
| Repo archived | Retain deck, exclude from syncs |

---

## 15. Output Artifacts

- `docs/pitch/index.html` per eligible repo
- `pitch.yaml` (Tier 2 repos)
- Bespoke SPA source (Tier 3 repos)
- PPTX export (bespoke, for offline sharing)

---

## Appendix A: Decision Trees

### Does this repo get a pitch deck?
`infrastructure`/`archive` tier? -> No. Has description? -> Yes, gets a deck. No? -> Write README first.

### Auto-generated or bespoke?
Flagship with fundraising, interactive demo, > 7 sections, or external audience? -> Bespoke. Otherwise -> Auto (Tier 1 or 2 depending on README richness).

## Appendix B: CLI Quick Reference

```bash
organvm pitch generate --repo <name> [--dry-run]
organvm pitch sync --organ ORGAN-III [--dry-run]
organvm pitch sync [--dry-run]
organvm pitch audit-readmes [--organ III]
organvm pitch validate <repo>
```

## Appendix C: Data Assembly Priority Chain

```
pitch.yaml > seed.yaml > registry-v2.json > README.md
```

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
