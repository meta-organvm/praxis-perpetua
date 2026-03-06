# ASCENSION Sprint — Production Quality Push

## Context

Post-CONSOLIDATION-II (2026-02-12), the system sits at 33 PRODUCTION + 30 PROTOTYPE = 63 repos with code (78%). But "PROTOTYPE" means skeleton modules with basic tests — not production-ready software. The 3 CRITICAL PROTOTYPE repos (`auto-revision-epistemic-engine`, `showcase-portfolio`, `case-studies-methodology`) are the ones grant reviewers and hiring managers will actually click into. If the code is stubs, the portfolio narrative collapses.

Additionally: 3 PRODUCTION repos have CI failures, 4 registry `ci_workflow` fields are wrong, 2 ORGAN-IV phantom entries inflate the count, 3 promotion obligations are PENDING, and the Jekyll site lacks navigation/about/tags pages.

**This sprint deepens quality across every dimension: fix what's broken, promote what's ready, build what's promised, polish what's visible.**

---

## Phase 0: Commit + Registry Accuracy (local only)

**Commit the 2 uncommitted files from CONSOLIDATION-II**, then fix registry accuracy:

| Fix | Detail |
|-----|--------|
| Commit local changes | `registry-v2.json` + `quarterly-sustainability-checklist.md` |
| Fix 4 ci_workflow fields | salon-archive, reading-group-curriculum, social-automation, distribution-strategy → `"ci-python.yml"` (verified: ci.yml deployed on GitHub) |
| Remove 2 ORGAN-IV phantoms | `system-governance-framework` and `cognitive-archaelogy-tribunal` (DESIGN_ONLY, "NOT_CREATED") — canonical repos exist in ORGAN-I |
| Update counts | `total_repos`: 81→79, ORGAN-IV `repository_count`: 9→7, `DESIGN_ONLY`: 15→13 |

**Critical file:** `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/registry-v2.json`

---

## Phase 1: CI Health Fix (3 PRODUCTION failures)

All 3 failures are from Dependabot/external PRs, not code bugs:

| Repo | Org | Failure | Fix |
|------|-----|---------|-----|
| system-governance-framework | organvm-i-theoria | "Enhanced PR Quality Checks" can't parse `@dependabot` author | Add early-exit for bot PRs in workflow |
| public-record-data-scrapper | organvm-iii-ergon | Dependabot npm update + Backend Tests | Investigate logs, fix lockfile or test |
| sovereign-ecosystem--real-estate-luxury | organvm-iii-ergon | devcontainers update | Close stale Dependabot PR or fix config |

**Per-fix recipe:** ~3-5 gh api calls (read workflow, read logs, deploy fix)

---

## Phase 2: PROTOTYPE → PRODUCTION Push (8 repos)

The core of the sprint. Each promotion means: **expand skeleton code to real functionality, comprehensive tests (15-25 per repo), CLI or API entry point works, CI green.**

### Tier 1: CRITICAL (3 repos — non-negotiable)

| # | Repo | Org | Current Modules | PRODUCTION Means |
|---|------|-----|----------------|-----------------|
| 1 | auto-revision-epistemic-engine | organvm-i-theoria | auto_revision_epistemic_engine/ (package) | 8-phase orchestration pipeline executable end-to-end, BLAKE3 audit chain produces verifiable hashes, mock review gates, CLI entry point, 30+ tests |
| 2 | showcase-portfolio | organvm-ii-poiesis | collector.py, gallery.py, renderer.py | Real entries for 8+ ORGAN-II artworks in data/, generates browsable portfolio index, CLI `python -m showcase generate`, 20+ tests |
| 3 | case-studies-methodology | organvm-ii-poiesis | parser.py, cross_reference.py, export.py | 3+ real case studies (Aetheria, metasystem-master, recursive-engine), parser extracts structured data, cross-ref links to repos/essays, 25+ tests |

### Tier 2: Highest-ROI HIGH repos (5 repos)

| # | Repo | Org | Why Prioritize | PRODUCTION Means |
|---|------|-----|---------------|-----------------|
| 4 | agent--claude-smith | organvm-iv-taxis | Claude SDK integration — directly relevant to AI eng roles | Multi-agent orchestration, state persistence, self-correction loop, demo scenario, 25+ tests |
| 5 | petasum-super-petasum | organvm-iv-taxis | Governance tooling — strengthens ORGAN-IV orchestration narrative | Policy evaluation engine, compliance checking, audit report generation, 20+ tests |
| 6 | reverse-engine-recursive-run | organvm-i-theoria | 7-script analysis pipeline — demonstrates systems thinking | All 7 scripts executable, risk scoring on sample codebase, drift detection, SBOM generation, 25+ tests |
| 7 | example-generative-music | organvm-ii-poiesis | Theory-to-art bridge — key I→II narrative | Audio/MIDI generation with recursive principles, browser or CLI demo, 20+ tests |
| 8 | salon-archive | organvm-vi-koinonia | Strongest ORGAN-VI repo — makes community organ substantive | Transcription pipeline, taxonomy tagging, session management, 20+ tests |

### Per-repo recipe (~10-15 gh api calls)
1. Read current src/ modules and tests to understand skeleton code
2. Expand each module: real classes with 5+ methods, proper error handling, type hints
3. Add CLI entry point (`__main__.py` or bin script)
4. Expand test suite to 20-30 tests covering core paths
5. Deploy via `gh api repos/ORG/REPO/contents/PATH --method PUT`
6. Verify CI green
7. Update registry: `implementation_status: "PRODUCTION"`

---

## Phase 3: Promotion Obligations (2 repos + 1 essay)

3 PENDING obligations from the state machine:

| # | Type | Target | Content |
|---|------|--------|---------|
| 1 | repo_creation | organvm-ii-poiesis/art-from--auto-revision-epistemic-engine | Interactive visualization of self-governing orchestration — governance as performance art |
| 2 | repo_creation | organvm-ii-poiesis/art-from--narratological-algorithmic-lenses | Interactive web experience exploring narrative structures via visual algorithmic lenses |
| 3 | essay | organvm-v-logos/public-process/_posts/ | "Why AI Function Calling Needs Ontological Grounding" (~4,000 words, Heideggerian/Aristotelian/Peircean frameworks) |

### Per-repo recipe (new repos, ~10 gh api calls each)
1. `gh api orgs/organvm-ii-poiesis/repos --method POST` — create repo
2. Deploy README (~2,500 words), LICENSE, pyproject.toml or package.json
3. Deploy src/ scaffold with 2-3 modules
4. Deploy tests/ with basic test suite
5. Deploy ci.yml (SHA-pinned)
6. Set GitHub topics
7. Add to registry as PROTOTYPE
8. Update source repo's promotion obligation status: PENDING → COMPLETE

### Essay recipe (~3 gh api calls)
1. Generate essay with Jekyll front matter (`layout: essay`, tags, etc.)
2. Deploy to `_posts/2026-02-13-why-ai-function-calling-needs-ontological-grounding.md`
3. Update registry essay count: 16→17

---

## Phase 4: Jekyll Site Enhancement

The public face needs polish. Currently: 16 essays render, RSS works, but no navigation, no about page, no tags page, inline CSS.

| Task | Files |
|------|-------|
| Fix index.md | Change `site.pages` filter to `site.posts` to properly list _posts content |
| Create about.md | Eight-organ system summary, org links, author bio, RSS link |
| Create tags.html | Groups essays by tag, enables tag-based navigation |
| Create _includes/header.html | Site navigation (Home, About, Tags, RSS) |
| Create _includes/footer.html | Copyright, meta links |
| Extract CSS to assets/css/style.css | Move inline styles from default.html to external stylesheet |
| Update _layouts/default.html | Include header/footer, link stylesheet |
| Update _layouts/essay.html | Add prev/next navigation between essays |

**~15 gh api calls total**

---

## Phase 5: Infrastructure Hardening

| Task | Scope | gh api calls |
|------|-------|-------------|
| Upgrade 2 remaining ci-minimal.yml repos | multi-camera--livestream--framework, virgil-training-overlay | ~6 |
| Deploy org-wide dependabot.yml | 8 orgs' .github repos (GitHub Actions weekly, packages monthly) | 8 |
| Set GitHub topics on all repos | `organvm` + `organ-N` + domain tags | ~79 |
| Remove old ci-minimal.yml from 4 repos | salon-archive, reading-group-curriculum, social-automation, distribution-strategy (if both ci.yml and ci-minimal.yml exist) | ~4 |

---

## Phase 6: Registry Finalization + Org Profile Updates

After all phases complete:

| Field | Before | After |
|-------|--------|-------|
| total_repos | 79 (after Phase 0 cleanup) | 81 (+2 new art-from repos) |
| PRODUCTION | 33 | 41 (+8) |
| PROTOTYPE | 30 (→28 after Phase 0) | 22 (-8 promoted, +2 new art-from repos) |
| DESIGN_ONLY | 13 (after Phase 0) | 13 |
| SKELETON | 3 | 3 |
| Essays | 16 | 17 |
| CI failures (PRODUCTION) | 3 | 0 |

Then update 8 org profile READMEs with new metrics (~16 gh api calls).

---

## Parallelism Map

```
Session 1:    [Phase 0: Commit + Registry accuracy]
                       |
              +--------+--------+--------+
              |        |        |        |
Session 2-3:  [Ph 1:   | Ph 3:  | Ph 4:  | Ph 5:
               CI fix  | Promos | Jekyll | Infra
               3 repos]| 2+1   | site   | topics]
              +--------+--------+--------+
                       |
Session 4-7:  [Phase 2: PRODUCTION Push]
              |-- Tier 1 (3 CRITICAL repos)    ← parallel agents
              |-- Tier 2 (5 HIGH repos)        ← parallel agents
                       |
Session 8:    [Phase 6: Registry final + org profiles]
```

**Phases 1, 3, 4, 5 are fully independent — run as concurrent agents.**
**Phase 2 can start as soon as Phase 0 completes (no dependency on Phases 1/3/4/5).**

---

## Budget

| Phase | gh api calls | Agent sessions |
|-------|-------------|---------------|
| Phase 0 | 0 | 0 (local edit + commit) |
| Phase 1 | ~15 | 1 agent |
| Phase 2 Tier 1 | ~45 | 1-2 parallel agents |
| Phase 2 Tier 2 | ~60 | 2-3 parallel agents |
| Phase 3 | ~25 | 1 agent |
| Phase 4 | ~15 | 1 agent |
| Phase 5 | ~97 | 1-2 agents |
| Phase 6 | ~16 | 1 agent |
| **Total** | **~273** | **~8-10 sessions** |

---

## Success Criteria

- [ ] 0 CI failures on PRODUCTION repos
- [ ] 41 PRODUCTION repos (up from 33)
- [ ] All 8 promoted repos have 20+ tests and CI green
- [ ] 0 PENDING promotion obligations
- [ ] 17 essays published, RSS feed shows 17 entries
- [ ] Jekyll site has About page, Tags page, proper navigation
- [ ] Registry `total_repos` matches actual GitHub count
- [ ] `implementation_status_distribution` matches per-repo counts
- [ ] All active repos off ci-minimal.yml
- [ ] GitHub topics set on all repos
- [ ] 8 org profiles updated with current metrics

## Verification

```bash
# 1. PRODUCTION CI health (all 41 should pass)
for ORG in organvm-i-theoria organvm-ii-poiesis organvm-iii-ergon organvm-iv-taxis organvm-v-logos; do
  gh repo list "$ORG" --json name --jq '.[].name' | while read REPO; do
    RESULT=$(gh run list --repo "$ORG/$REPO" --limit 1 --json conclusion --jq '.[0].conclusion' 2>/dev/null)
    [ "$RESULT" = "failure" ] && echo "FAIL: $ORG/$REPO"
  done
done

# 2. Essay count
gh api repos/organvm-v-logos/public-process/contents/_posts --jq 'length'
# Expected: 17

# 3. Registry validation
python3 scripts/v3-registry-reconciliation.py
python3 scripts/v4-dependency-validation.py
python3 scripts/v5-v6-constitution-organ-checks.py

# 4. Jekyll site
curl -sL https://organvm-v-logos.github.io/public-process/feed.xml | grep -c '<entry>'
# Expected: 17
curl -sL https://organvm-v-logos.github.io/public-process/about/ -o /dev/null -w "%{http_code}"
# Expected: 200
```

## What NOT to Do

- Do NOT add more repos beyond the 2 promotion obligations — focus on quality, not quantity
- Do NOT attempt framework extraction (deferred per D-06)
- Do NOT force PRODUCTION on repos where tests don't pass — PROTOTYPE is an honest state
- Do NOT write another evaluation document — Doc 11 is terminal
