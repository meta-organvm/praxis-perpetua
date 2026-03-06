# Application Pipeline Memory

## User Preferences
- When listing pipeline entries (batch lists, top entries, etc.), **always include the application URL** from `target.application_url`
- Resume batches go to `materials/resumes/batch-NN/`; current batch is `batch-03`
- PDF build via `python scripts/build_resumes.py` (headless Chrome); all resumes must be exactly 1 page
- Wire resumes to pipeline YAML via `python scripts/tailor_resume.py --target <id> --wire`

## Market Intelligence System (added 2026-03-01)
- `strategy/market-intelligence-2026.json` — master data artifact; 112 sources; review by 2026-06-01
- `strategy/market-research-corpus.md` — annotated bibliography (126 sources across 7 categories)
- `scripts/market_intel.py` — CLI; flags: `--track`, `--calendar`, `--salary`, `--skills`, `--channels`, `--sources`, `--staleness`
- Quick command: `python scripts/run.py market`
- `standup.py --section market` — shows conditions + hot skills + upcoming grant deadlines
- `score.py` loads portal friction scores + strategic base from JSON at runtime (via `get_portal_scores()` / `get_strategic_base()`)
- `followup.py` loads PROTOCOL timing from JSON via `load_protocol_from_market_intel()`
- `standup.py` loads stale thresholds from JSON via `_get_stale_threshold()`
- All scripts fallback to hardcoded defaults if JSON missing — no breaking changes

## Key 2026 Market Data Points (Precision-Over-Volume Era)
- Tech layoffs YTD: 51,330 (856/day); cold app viability: LOW
- Referral multiplier: 8x; tailored cover letter: +53% callback; follow-up: +68% offers
- **Precision mode**: max 1-2 apps/week, min score 9.0, network_proximity >= 5 preferred
- Daily split: 2hr research, 2hr relationships, 1hr application work
- Max 10 active entries; max 1 per org (COMPANY_CAP=1)
- AI content rejection: 62% (generic), 80% (robotic)
- Hot skills: go (+41%), kubernetes, terraform, platform-engineering, mcp, agentic-workflows
- Urgent deadlines: S+T+ARTS Prize closes 2026-03-04; Creative Capital opens 2026-04-02

## Block Metrics Hygiene (updated 2026-03-01)
- Canonical values: 103 repos, ~810K words, 42 essays, 2,349 tests, 33 sprints
- `python scripts/check_metrics.py` validates 168 files; run before any submission batch
- Common false positives to watch: per-organ test counts ("1,254 automated tests" for ORGAN-I),
  subset repo refs ("70 repositories" when meaning "70 of 103"), document paths ("10-repository-standards"),
  table cell values with "Meta" prefix
- Fix pattern: reword to use "of N" subset notation or replace "automated tests" with "test cases"
- `blocks/identity/5min.md` — core identity block; watch test_count (canonical 2,349)
- `blocks/framings/independent-engineer.md` — jobs framing; watch total_repos phrase form

## Follow-up System State (updated 2026-03-01)
- `followup.py --init --yes` was run 2026-03-01; hydrated 10 new entries (10 already had data)
- 19 overdue LinkedIn connects (Days 4-5 past submission); next DMs due 2026-03-03 to 2026-03-05
- Protocol: connect Day 1-3, DM Day 7, final follow-up Day 14

## Job Entry Patterns (updated 2026-03-01)
- Auto-sourced job entries often get `resumes/independent-engineer-resume.html` as a dangling reference
  when `tailor_resume.py --wire` appends batch-03 resume without removing old reference
- Fix: remove dangling line from YAML `submission.materials_attached` list
- Cohere Applied AI (Korea/Singapore) batch-03 resumes built 2026-03-01 (1-page, agentic-workflows focus)
