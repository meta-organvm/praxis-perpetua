# Evaluation-to-Growth: ORGAN-V (organvm-v-logos) Full Project Review

## Context

ORGAN-V (Logos) is the public discourse layer of the ORGANVM eight-organ system. It's a git superproject with 6 submodules. After initial setup sprints and a CLAUDE.md rewrite, the project is at a natural inflection point. This evaluation applies the Evaluation-to-Growth framework across the full project to surface what's working, what's broken, what's risky, and where to grow — producing actionable implementation tasks.

**Output format**: Markdown report with implementation plan
**Mode**: Autonomous (full analysis, then concrete tasks)

---

## Phase 1: Evaluation

### 1.1 Critique — Strengths and Weaknesses

**Strengths:**
- **essay-pipeline is well-built**: Clean separation (validator.py, indexer.py, schema_loader.py), good test coverage (22 tests across 5 fixture files), proper pyproject.toml, functional CI that cross-checks editorial-standards
- **Editorial standards are rigorous**: frontmatter-schema.yaml is precise and machine-enforceable. quality-rubric.yaml is thoughtful (100-point scale across 5 dimensions). Category taxonomy includes migration map for deprecated categories. Tag governance is curated from actual usage
- **Essay content is genuinely strong**: 42 essays, ~134K words. The writing is specific, honest, and substantive — the "Building in Public" essay alone contains concrete metrics (170 replacements, 34 files, 208K words). The Aetheria post-mortem is a real case study with real numbers. The Solo Auteur Method draws genuine creative lineage (Eno, Reznor, Prince, Wilson, Malick)
- **CI is functional where it matters**: public-process CI validates frontmatter AND checks for data drift. essay-pipeline CI runs real tests against the schema. editorial-standards CI validates both YAML schemas and template frontmatter
- **Jekyll site is clean**: Minimal, well-structured layouts. GoatCounter analytics (privacy-first). RSS feed. Mermaid diagram support. Category/tag pages
- **Data artifacts are well-structured**: essays-index.json is comprehensive (42 essays, category counts, tag frequency, per-essay metadata)

**Weaknesses:**
- **2 of 6 repos are empty scaffolds with aspirational READMEs**: analytics-engine (21K-word README, zero source code) and reading-observatory (19K-word README, zero source code). Their READMEs describe complete architectures (goatcounter.py, aggregator.py, dashboard.py, feed-aggregator.py) that don't exist
- **seed.yaml contracts overclaim**: analytics-engine declares `weekly-metrics` agent workflow that doesn't exist. Essay-pipeline declares `sprint-narrative-draft` and `system-activity` consumption that aren't implemented. The `produces` and `consumes` edges describe aspirational data flows, not actual ones
- **Promotion statuses are inconsistent**: public-process seed says `PRODUCTION` + `PUBLIC_PROCESS`, but essay-pipeline and editorial-standards say `PROTOTYPE` + `LOCAL` despite having working code and CI. Analytics-engine says `SKELETON` which is accurate
- **No CSS file exists**: `default.html` references `/assets/css/style.css` but there's only an `assets/` directory — need to verify this file exists
- **The `essays/` collection and `_posts/` coexist without documentation**: `essays/` contains 16 long-form flagship essays (30-50KB each) organized by category. `_posts/` contains 42 shorter blog-format essays. Both are valid but the distinction isn't documented anywhere
- **Tag enforcement is advisory only**: tag-governance.yaml defines a `pattern` field but the validator doesn't actually check tags against the preferred list or the pattern
- **No Gemfile.lock committed**: public-process has a Gemfile but no lock file, making builds non-reproducible

### 1.2 Logic Check — Internal Consistency

**Contradictions found:**
1. **README vs. reality for scaffold repos**: analytics-engine README describes 3 Python modules, JSON schemas, data directories, a dashboard generator — none of which exist. The README's architecture diagram references `goatcounter.py`, `aggregator.py`, `dashboard.py` as implemented components
2. **seed.yaml `implementation_status` vs. actual state**: essay-pipeline is `PROTOTYPE` but has working code, tests, and CI. editorial-standards is `PROTOTYPE` but has production schemas actively consumed by essay-pipeline and public-process CI. These should be `PRODUCTION`
3. **Superproject auto-generated section shows only 2 repos** but there are 6 submodules
4. **CLAUDE.md (pre-rewrite) listed build commands for analytics-engine and reading-observatory** that referenced nonexistent files — this was fixed in the recent rewrite

**Reasoning gaps:**
1. No documented decision for why `public-process/data/engagement-metrics.json` exists as an empty/placeholder when analytics-engine has no code to produce it
2. No ADR for the dual `essays/` collection + `_posts/` directory pattern in Jekyll config

**Unsupported claims:**
1. analytics-engine seed.yaml declares 3 `produces` edges (engagement-metrics, system-engagement-report, analytics-dashboard) — none are produced
2. reading-observatory seed.yaml declares 2 `produces` edges (curated-reading-lists, relevant-articles) — none are produced

### 1.3 Logos Review — Rational Appeal

**Argument clarity**: HIGH. The system's architecture is clearly articulated — the data flow from editorial-standards → essay-pipeline → public-process is clean and demonstrable. The frontmatter schema is precise and enforceable.

**Evidence quality**: MIXED. The working repos (essay-pipeline, editorial-standards, public-process) have strong evidence — real code, real tests, real CI, real published essays. The scaffold repos have zero evidence backing their claims.

**Persuasive strength**: STRONG for the core pipeline, WEAK for the full organ. A reviewer examining the actual repository contents would see a working essay publication system with good tooling, undermined by two repos that are pure README with no implementation.

### 1.4 Pathos Review — Emotional Resonance

**Current tone**: The essay content is remarkably honest and self-aware. The Solo Auteur Method essay is emotionally compelling. The Aetheria post-mortem opens with "this is a post-mortem in the traditional sense... with the obligation of honesty." The Building in Public essay frames transparency as methodology, not marketing.

**Audience connection**: STRONG for someone evaluating creative-technical work. The essays read as genuine intellectual engagement, not marketing copy.

**Risk**: The gap between aspirational scaffolds and working code could undermine the honesty brand. If the project claims radical transparency, empty repos with detailed READMEs feel like the opposite.

### 1.5 Ethos Review — Credibility

**Perceived expertise**: HIGH in the working components. The validator code is clean. The schema design is thoughtful. The CI cross-checkout pattern shows real engineering.

**Trustworthiness signals present**: MIT license, CONTRIBUTING.md, SECURITY.md, ADRs, CHANGELOG, seed.yaml contracts, conventional commits

**Trustworthiness signals undermined**: Scaffold repos with `SKELETON` status but 20K-word READMEs describing complete systems. CI badges on repos that can only pass a "does README exist?" check. `implementation_status: SKELETON` is honest in the seed.yaml but invisible to casual observers who see the README

---

## Phase 2: Reinforcement — Synthesis

**Core contradiction to resolve**: The project's editorial standard demands honesty (quality-rubric scores it 0-20), but two repos present aspirational architectures as current reality. This is the single most important thing to fix.

**Coherence improvements needed:**
1. Align seed.yaml `implementation_status` with reality across all repos
2. Either implement the scaffold repos or clearly mark their READMEs as design documents
3. Ensure the auto-generated CLAUDE.md organ map reflects all 6 repos, not just 2
4. Resolve the `essays/` vs `_posts/` dual-directory ambiguity

---

## Phase 3: Risk Analysis

### 3.1 Blind Spots

- **Tag drift**: 80+ tags across 42 essays with only advisory governance. No enforcement means the vocabulary will continue to sprawl
- **No quality gate on essays**: quality-rubric.yaml exists but is never invoked programmatically. Any essay that passes frontmatter validation gets published regardless of content quality
- **Data staleness**: essays-index.json was last generated 2026-02-17. If essays are added without re-running the indexer, the data files drift
- **Gemfile.lock absence**: Jekyll builds are non-reproducible; `github-pages` gem version could shift

### 3.2 Shatter Points

| Vulnerability | Severity | Impact |
|---|---|---|
| Scaffold READMEs masquerading as documentation | HIGH | Credibility loss if a reviewer digs into the repos and finds no code |
| ~~No CSS file~~ (verified: style.css exists, 9KB) | RESOLVED | N/A |
| Dependabot PR for actions/setup-python-6 unmerged | LOW | CI could break if v5 is deprecated |
| Tag pattern not enforced by validator | LOW | Gradually eroding controlled vocabulary |

---

## Phase 4: Growth — Implementation Plan

### 4.1 Bloom (Emergent Insights)

- The essay-pipeline validator could be extended to enforce tag patterns and check against preferred tags — the schema already defines `tag-governance.yaml` with a `pattern` field
- A simple `make` or shell script at the superproject level could run validation across all repos in one command
- The quality rubric could be semi-automated: word count, frontmatter completeness, and structure (heading count) are all machine-checkable

### 4.2 Evolve — Concrete Implementation Tasks

#### Task 1: Fix scaffold README honesty (HIGH priority)
**Files**: `analytics-engine/README.md`, `reading-observatory/README.md`
**Action**: Add a prominent "Status: Design Document" banner at the top of each README. Move the architecture descriptions under a "## Planned Architecture" heading. Add a "## Current State" section that honestly states what exists (seed.yaml, ADRs, CI scaffold, no source code).

#### Task 2: Correct seed.yaml implementation_status (HIGH priority)
**Files**: `essay-pipeline/seed.yaml`, `editorial-standards/seed.yaml`
**Action**: Update `implementation_status` from `PROTOTYPE` to `PRODUCTION` for both repos. Update `promotion_status` from `LOCAL` to `PUBLIC_PROCESS` for essay-pipeline (it's actively used in public-process CI).

#### Task 3: Add tag pattern enforcement to validator (MEDIUM priority)
**Files**: `essay-pipeline/src/validator.py`, `essay-pipeline/tests/test_validator.py`
**Action**: Add a check that validates each tag against the pattern `^[a-z0-9]+(-[a-z0-9]+)*$` from tag-governance.yaml. Add test cases for valid/invalid tag formats. This reuses the existing `validate_field` pattern — add `item_pattern` to the tags spec in the schema, or hardcode the pattern from tag-governance.

#### Task 4: Clarify essays/ vs _posts/ dual-directory pattern (LOW priority)
**Files**: `public-process/_config.yml`
**Context**: `assets/css/style.css` exists (9KB — confirmed). The `essays/` directory contains 16 longer-form essays (30-50KB each) organized into `meta-system/` and `subsidiary/` subdirs. These are the Jekyll collection items. `_posts/` contains 42 shorter blog-format essays (~3KB each). Both are active — this is intentional (collection for flagship essays, posts for the full feed).
**Action**: Add a brief comment in `_config.yml` or a note in CLAUDE.md explaining the dual-directory pattern: `essays/` = flagship long-form collection, `_posts/` = all essays for blog feed. No code change needed — just documentation clarity.

#### Task 5: Add superproject-level validation script (LOW priority)
**File**: New `validate.sh` at superproject root
**Action**: A simple script that runs `git submodule foreach` to check each submodule's CI-equivalent locally: YAML validation for editorial-standards, pytest for essay-pipeline, frontmatter validation for public-process.

---

## Verification

After implementation:
1. `cd essay-pipeline && pytest tests/ -v` — all tests pass including new tag pattern tests
2. `cd essay-pipeline && python -m src.validator --posts-dir ../public-process/_posts/ --schema ../editorial-standards/schemas/frontmatter-schema.yaml` — all 42 essays pass
3. Manually inspect analytics-engine/README.md and reading-observatory/README.md for honest status banners
4. Check seed.yaml `implementation_status` values match reality
5. `bundle exec jekyll build --strict_front_matter` in public-process to verify site builds cleanly

## Critical Files

| File | Role |
|---|---|
| `essay-pipeline/src/validator.py` | Modify: add tag pattern enforcement |
| `essay-pipeline/tests/test_validator.py` | Modify: add tag pattern test cases |
| `essay-pipeline/seed.yaml` | Modify: status PROTOTYPE → PRODUCTION |
| `editorial-standards/seed.yaml` | Modify: status PROTOTYPE → PRODUCTION |
| `analytics-engine/README.md` | Modify: add design-document banner |
| `reading-observatory/README.md` | Modify: add design-document banner |
| `editorial-standards/schemas/tag-governance.yaml` | Reference: tag pattern `^[a-z0-9]+(-[a-z0-9]+)*$` |
| `editorial-standards/schemas/frontmatter-schema.yaml` | Reference: field specs |
| `public-process/assets/css/style.css` | Verified: exists (9KB) |
