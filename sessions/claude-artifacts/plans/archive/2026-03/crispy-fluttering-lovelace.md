# Ignition + Living Site Plan

## Context

The ORGAN-V autonomous pipeline (CI cascade across 5 repos) is architecturally complete — all workflows, source code, and tests exist — but has **never fired** because zero GitHub secrets are configured anywhere. Meanwhile, the Jekyll site at `public-process/` renders 42 essays but never surfaces its own data files (`essays-index.json`, `cross-references.json`, `publication-calendar.json`, `logs-index.json`). This plan has two phases: (1) wire the secrets so the pipeline ignites, (2) build data-driven Jekyll pages that render the JSON artifacts.

---

## Phase 1: Ignition (GitHub Secrets)

### Problem

All 5 repos (+ org-level) have **zero secrets**. The CI cascade requires:

| Secret | Used By | Purpose |
|--------|---------|---------|
| `CROSS_ORG_DISPATCH_TOKEN` | essay-pipeline, analytics-engine, reading-observatory, .github, public-process | GitHub PAT with `repo` scope for cross-org `repository_dispatch` |
| `GOATCOUNTER_SITE` | analytics-engine | GoatCounter site code (e.g., `organvm`) |
| `GOATCOUNTER_TOKEN` | analytics-engine | GoatCounter API token |
| `ANTHROPIC_API_KEY` | essay-pipeline | LLM for essay generation |
| `LLM_PROVIDER` | essay-pipeline | Provider selector (e.g., `anthropic`) |

### Approach

**Cannot automate secret values** — user must provide them. I will:

1. Create a shell script `ignition.sh` at the superproject root that uses `gh secret set` to configure all secrets across all repos from environment variables
2. The script will validate that `gh` is authenticated and that required env vars are set before proceeding
3. After secrets are set, trigger initial workflow runs via `gh workflow run` for each pipeline entry point

### Script: `ignition.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

# Required env vars (user sets before running):
#   CROSS_ORG_DISPATCH_TOKEN
#   GOATCOUNTER_SITE
#   GOATCOUNTER_TOKEN
#   ANTHROPIC_API_KEY (or other LLM key)
#   LLM_PROVIDER (default: anthropic)

# Sets secrets across all 5 repos + triggers first runs
```

**Repos to configure:**
- `organvm-v-logos/essay-pipeline` — CROSS_ORG_DISPATCH_TOKEN, ANTHROPIC_API_KEY, LLM_PROVIDER
- `organvm-v-logos/analytics-engine` — CROSS_ORG_DISPATCH_TOKEN, GOATCOUNTER_SITE, GOATCOUNTER_TOKEN
- `organvm-v-logos/reading-observatory` — CROSS_ORG_DISPATCH_TOKEN
- `organvm-v-logos/public-process` — CROSS_ORG_DISPATCH_TOKEN
- `organvm-v-logos/.github` — CROSS_ORG_DISPATCH_TOKEN

### First Triggers (after secrets are set)

1. `reading-observatory` weekly-feeds → dispatches `feeds-updated`
2. `analytics-engine` weekly-metrics → dispatches `metrics-updated`
3. `essay-pipeline` weekly-intelligence → consumes both events
4. `essay-pipeline` daily-log → generates captain's log PR

---

## Phase 2: Living Site (Data-Driven Pages)

### Problem

The Jekyll site has rich JSON data in `data/` but no pages render it. The homepage lists essays from `site.posts` (Liquid) but ignores `site.data.*`. There's no dashboard, no reading list, no cross-reference visualization.

### Pages to Create

#### 2a. `public-process/dashboard.md` — Corpus Dashboard

A stats page rendering `site.data.essays-index` and `site.data.publication-calendar`.

**Sections:**
1. **Stat grid** (reuse existing `.stat-grid`, `.stat-value`, `.stat-label` CSS classes at `style.css:420-449`):
   - Total essays, Total words, Categories count, Average word count
2. **Category breakdown** — horizontal bar chart via CSS `width` percentages from `site.data.essays-index.categories`
3. **Tag cloud** — top 20 tags from `site.data.essays-index.tag_frequency`, sized by frequency
4. **Publication timeline** — dates from `site.data.publication-calendar.essays`, CSS bar chart

**Data sources:** `site.data.essays-index`, `site.data.publication-calendar`
**Layout:** `default`

#### 2b. `public-process/reading.md` — Reading Observatory

Renders `site.data.surfaced` (from reading-observatory `feeds/surfaced.json`).

**Sections:**
1. **Surfaced articles** grouped by collection — title, source, date, excerpt
2. **Empty state** — "No articles surfaced yet. The reading observatory runs weekly." (surfaced.json is currently `[]`)

**Data source:** Will need to add `surfaced.json` to Jekyll's `data/` directory (symlink or copy from reading-observatory). For now, create the page with empty-state handling.
**Layout:** `default`

#### 2c. `public-process/connections.md` — Cross-Reference Map

Renders `site.data.cross-references` showing which essays reference which repos/organs.

**Sections:**
1. **Most-connected repos** — repos sorted by how many essays reference them (from `entries[*].related_repos`)
2. **Essay-to-repo table** — each essay with its linked repos as badges
3. **Organ heatmap** — count essays per organ (parse org name from repo prefix)

**Data source:** `site.data.cross-references`
**Layout:** `default`

### 2d. Homepage Enhancement — `public-process/index.md`

Add a corpus stats banner at the top, before the essay listing:

```html
<div class="stat-grid">
  <div class="stat">
    <div class="stat-value">{{ site.data.essays-index.total_essays }}</div>
    <div class="stat-label">Essays</div>
  </div>
  <div class="stat">
    <div class="stat-value">{{ site.data.essays-index.total_words | divided_by: 1000 }}k</div>
    <div class="stat-label">Words</div>
  </div>
  <div class="stat">
    <div class="stat-value">{{ site.data.essays-index.categories | size }}</div>
    <div class="stat-label">Categories</div>
  </div>
</div>
```

### 2e. Navigation Update — `public-process/_includes/header.html`

Add "Dashboard" link to nav bar between "Tags" and "Log":

```html
<a href="{{ site.baseurl }}/dashboard/">Dashboard</a>
```

### 2f. CSS Additions — `public-process/assets/css/style.css`

New styles appended (minimal additions, reusing existing design system variables):

- `.bar-chart` — horizontal bar chart for category breakdown
- `.bar-fill` — colored fill with percentage width
- `.bar-label` — label + count
- `.tag-cloud` — flexbox container for weighted tags
- `.tag-cloud .tag` — font-size scaled by frequency
- `.timeline` — vertical date list with bar widths
- `.connection-table` — styled table for cross-references
- `.empty-state` — centered muted text for no-data states
- `.organ-heatmap` — grid showing organ essay counts

### 2g. Data File: Copy `surfaced.json`

Copy `reading-observatory/feeds/surfaced.json` → `public-process/data/surfaced.json` so Jekyll can access it via `site.data.surfaced`. Currently empty `[]` so the reading page shows empty state.

---

## File Inventory

**New files (4):**
- `ignition.sh` (superproject root)
- `public-process/dashboard.md`
- `public-process/reading.md`
- `public-process/connections.md`

**Modified files (3):**
- `public-process/index.md` — add stat grid banner
- `public-process/_includes/header.html` — add Dashboard nav link
- `public-process/assets/css/style.css` — append data visualization styles

**Copied files (1):**
- `reading-observatory/feeds/surfaced.json` → `public-process/data/surfaced.json`

---

## Verification

1. `cd public-process && bundle exec jekyll build --strict_front_matter` — builds without errors
2. `bundle exec jekyll serve` — visual check of:
   - Homepage stat banner renders with correct numbers (42 essays, 134k words, 5 categories)
   - `/dashboard/` page shows category bars, tag cloud, publication timeline
   - `/connections/` page renders cross-reference table with repo badges
   - `/reading/` page shows empty state message
   - Dashboard link appears in header nav
3. Run `ignition.sh` (user provides env vars) — all `gh secret set` commands succeed
4. `gh workflow run` triggers — verify workflows start in GitHub Actions UI
