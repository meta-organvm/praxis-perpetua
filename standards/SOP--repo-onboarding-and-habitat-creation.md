# SOP: Repo Onboarding & Habitat Creation

## 1. Ontological Purpose

This SOP governs the creation and integration of new repositories into the ORGANVM system. Every repo is a habitat — a constructed environment where an idea germinates, roots, and grows. This procedure ensures that every new habitat has the soil conditions it needs from day one: correct naming, organ membership, registry integration, CI setup, and context file generation.

A repo created without this procedure is an unregistered organism — invisible to the system, missing from the dependency graph, excluded from pitch generation, and unknown to the dashboard. This SOP prevents that.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 3: Governance & Lifecycle)
**Cross-reference:** `SOP--the-membrane-protocol.md` (experimental Phase 0), `SOP--promotion-and-state-transitions.md` (new repos enter at LOCAL), Standard `12-habitat-governance-lifecycle.md` (governance artifacts per stage), Standard `10-repository-standards.md` (root hygiene)

---

## 2. Phase I: Naming & Identity

### Process

1. **Select the organ.** Determine which organ this idea belongs to by affinity:
   - Theory/epistemology/recursion -> ORGAN-I (`organvm-i-theoria`)
   - Art/generative/performance -> ORGAN-II (`organvm-ii-poiesis`)
   - Commerce/SaaS/products -> ORGAN-III (`organvm-iii-ergon`)
   - Orchestration/governance/agents -> ORGAN-IV (`organvm-iv-taxis`)
   - Public discourse/essays -> ORGAN-V (`organvm-v-logos`)
   - Community/learning -> ORGAN-VI (`organvm-vi-koinonia`)
   - Distribution/POSSE -> ORGAN-VII (`organvm-vii-kerygma`)
   - Cross-organ governance -> META-ORGANVM (`meta-organvm`)

2. **Choose the repo name.** Follow the double-hyphen naming convention:
   - Single hyphen separates words: `public-record`
   - Double hyphen separates function from descriptor: `sema-metra--alchemica-mundi`
   - Exceptions: short, self-descriptive names that don't need a descriptor (`portfolio`, `public-process`)

3. **Assign tier:**
   - `flagship` — portfolio-critical, highest investment
   - `standard` — normal development priority
   - `infrastructure` — supporting tooling, no pitch deck
   - `archive` — completed lifecycle

4. **Select visibility:** `public` (default) or `private` (for pre-launch products with sensitive IP)

### Starter Research Questions
- Which organ does this idea most naturally belong to?
- Is this idea distinct enough to warrant a new repo, or should it be a module in an existing repo?
- Does a repo with a similar scope already exist in the target organ?
- What tier is appropriate given the investment level?

---

## 3. Phase II: Repository Creation

### Process

1. **Create the GitHub repo:**
   ```bash
   gh repo create <org>/<repo-name> --public --description "One-line description"
   ```

2. **Initialize with README.md.** Every README is a portfolio piece — written for grant reviewers and hiring managers, not just developers. Target: 2,500+ words for portfolio-relevant repos. Use existing repos in the same organ as style reference.

   Required sections: What This Is, Problem, Solution, Key Features, Architecture.

3. **Add foundational files:**
   - `.gitignore` (language-appropriate)
   - `LICENSE` (MIT for code, CC BY-SA for creative works)

### Starter Research Questions
- Is the description concise and externally meaningful?
- Does the README follow the portfolio standard?
- Is the license appropriate for this organ's content type?
- Are there existing repos in this organ to use as README templates?

---

## 4. Phase III: seed.yaml Authoring

### Process

1. **Create `seed.yaml`** in the repo root:
   ```yaml
   schema_version: "1.0"
   organ: "ORGAN-II"
   org: "organvm-ii-poiesis"
   repo: "repo-name"
   tier: "standard"
   promotion_status: "INCUBATOR" # Default for experimental projects (Phase 0)
   last_validated: "2026-03-07"
   metadata:
     description: "What this repo does"
   ```
     - type: "creative-artifact"
       description: "What this repo produces"
   consumes:
     - type: "theory"
       from: "organvm-i-theoria/source-repo"
       description: "What it consumes and why"
   ```

2. **Declare produces/consumes edges** if the repo has inter-organ dependencies. All edges must comply with `governance-rules.json` — no back-edges in the I-II-III chain.

3. **For ORGAN-III products,** add community and distribution edges:
   ```yaml
   produces:
     - type: product
     - type: community_signal
       consumers: [organvm-vi-koinonia/community-hub]
     - type: distribution_signal
       consumers: [organvm-vii-kerygma/social-automation]
   ```

### Starter Research Questions
- What does this repo produce and who consumes it?
- What does this repo consume and from where?
- Do the declared edges comply with the dependency rules?
- Is this a cross-organ promotion requiring specific naming?

---

## 5. Phase IV: Registry Integration

### Process

1. **Add the repo entry to `registry-v2.json`** under the appropriate organ:
   ```json
   {
     "name": "repo-name",
     "org": "organvm-ii-poiesis",
     "implementation_status": "SKELETON",
     "documentation_status": "DEPLOYED",
     "promotion_status": "LOCAL",
     "public": true,
     "description": "What this repo does",
     "tier": "standard",
     "portfolio_relevance": "MEDIUM",
     "dependencies": []
   }
   ```
   ORGAN-III repos additionally need: `type`, `revenue_model`, `revenue_status`.

2. **Update aggregate counts:**
   - `total_repos` (top-level field)
   - Organ's `repository_count`
   - `implementation_status_distribution` if applicable

3. **Validate:**
   ```bash
   organvm registry validate
   ```

### Starter Research Questions
- Are all required fields populated for this organ?
- Are aggregate counts updated correctly?
- Does validation pass cleanly?
- Is the `portfolio_relevance` rating accurate?

---

## 6. Phase V: Infrastructure Setup

### Process

1. **Set GitHub topics:**
   ```bash
   gh api "repos/<org>/<repo>/topics" --method PUT \
     --input - <<EOF
   {"names": ["organvm", "organ-ii", "generative-art"]}
   EOF
   ```

2. **Add CI workflow** (if CANDIDATE or above):
   - Create `.github/workflows/ci.yml` with build + test + lint
   - Reference existing workflows in the same organ as templates

3. **Generate context files:**
   ```bash
   organvm context sync --dry-run
   organvm context sync
   ```
   This generates `CLAUDE.md`, `GEMINI.md`, `AGENTS.md` with system context.

4. **If meta-organvm submodule,** add to superproject:
   ```bash
   organvm git add-submodule --organ META --repo <name> --url <url>
   ```

### Starter Research Questions
- What topics are appropriate for this repo?
- Is there an existing CI workflow in this organ to copy?
- Does context sync produce correct output for this repo?
- Does this repo need to be a submodule of any superproject?

---

## 7. Phase VI: Habitat Validation

### Process

1. **Run full validation:**
   ```bash
   organvm registry validate
   organvm seed validate
   organvm governance check-deps
   ```

2. **Verify seed discovery finds the new repo:**
   ```bash
   organvm seed discover --workspace ~/Workspace
   ```

3. **Generate pitch deck** (if standard or flagship tier):
   ```bash
   organvm pitch generate --repo <name> --dry-run
   organvm pitch generate --repo <name>
   ```

4. **Commit all changes:**
   ```bash
   # In the new repo
   git add .
   git commit -m "feat: initialize repo with seed.yaml and README"
   git push origin main

   # In corpus (registry update)
   cd ~/Workspace/meta-organvm/organvm-corpvs-testamentvm
   git add registry-v2.json
   git commit -m "feat: add <repo-name> to <ORGAN>"
   git push origin main
   ```

### Starter Research Questions
- Do all validation commands pass?
- Does seed discovery find the new repo?
- Does the pitch deck generate correctly?
- Are all commits atomic and well-described?

---

## 8. Output Artifacts

- GitHub repository with README, .gitignore, LICENSE
- `seed.yaml` declaring organ membership and edges
- Updated `registry-v2.json` with new entry and correct counts
- GitHub topics set
- Context files generated (CLAUDE.md, GEMINI.md, AGENTS.md)
- Pitch deck generated (if applicable)
- CI workflow (if CANDIDATE or above)

---

## Appendix A: Naming Pattern Reference

| Pattern | Example | When |
|---------|---------|------|
| `word-word` | `public-process` | Simple, self-descriptive |
| `word-word--word-word` | `sema-metra--alchemica-mundi` | Function + descriptor |
| `art-from--<source>` | `art-from--recursive-engine` | Cross-organ: I->II |
| `essay-from--<source>` | `essay-from--styx` | Cross-organ: Any->V |

## Appendix B: seed.yaml Template

```yaml
schema_version: "1.0"
organ: "ORGAN-X"
org: "<github-org>"
repo: "<repo-name>"
tier: "standard"
promotion_status: "LOCAL"
last_validated: "YYYY-MM-DD"
metadata:
  description: ""
produces:
  - type: ""
    description: ""
consumes:
  - type: ""
    from: "<org>/<repo>"
    description: ""
```

## Appendix C: Tier Criteria

| Tier | Criteria | Pitch Deck | Typical Count |
|------|----------|------------|---------------|
| `flagship` | Portfolio-critical, 200+ tests or 50+ docs, revenue integration | Bespoke (Tier 3) | 2-3 per organ |
| `standard` | Normal development | Auto-generated (Tier 1-2) | Majority |
| `infrastructure` | Supporting tooling | None (Tier 0) | 1-2 per organ |
| `archive` | Completed lifecycle | Retained, excluded from sync | Variable |

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
