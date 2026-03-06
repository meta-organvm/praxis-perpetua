# ORGAN-IV Memory

## GitHub Org Name Mapping
- ORGAN-I: `organvm-i-theoria` (GitHub) / `ivviiviivvi` (old) / `organvm-i-theoria/` (local dir)
- ORGAN-II: `omni-dromenon-machina` (GitHub) / `organvm-ii-poiesis/` (local dir)
- ORGAN-III: `organvm-iii-ergon` (GitHub, NOT `labores-profani-crux`) / `organvm-iii-ergon/` (local dir)
- ORGAN-IV: `organvm-iv-taxis` (GitHub) / `organvm-iv-taxis/` (local dir)
- ORGAN-VI: `organvm-vi-koinonia` (GitHub)
- ORGAN-VII: `organvm-vii-kerygma` (GitHub)
- META: `meta-organvm` (GitHub)

## PHASE-C CI Green Wave (2026-02-24)
See [phase-c-results.md](phase-c-results.md) for details.

**Result**: Fixed 11 repos, 17 promoted to CANDIDATE+, soak test green.
**Blocker**: 11 ORGAN-I repos blocked by `organvm-i-theoria` billing lock on GitHub Actions.

## PHASE-D Soak Hardening + CI Provisioning (2026-02-24)

**Changes made:**
1. Soak test monitor: billing-locked orgs classified separately (not counted as failures)
2. Deployed ci-minimal.yml to 9 repos (6 .github org repos + krypto-velamen, alchemical-synthesizer, select-or-left-or-right-or)
3. Updated ci_workflow for 10 repos, promoted 6 repos LOCAL → CANDIDATE
4. Registry: 72 CANDIDATE, 12 PUBLIC_PROCESS, 4 GRADUATED, 6 LOCAL, 9 ARCHIVED

**Soak test results (post-PHASE-D):** 89 checked, 66 passing, 6 failing, 2 unknown, 15 billing-locked

**Remaining 6 failing repos:** fetch-familiar-friends, public-record-data-scrapper, life-my--midst--in, a-i--skills, community-hub, system-dashboard
**Remaining LOCAL (6):** 2 billing-locked (ORGAN-I), chthon-oneiros + ivi374ivi027-05 (CI failing), render-second-amendment (CI failing), organvm-mcp-server (no push CI runs)

## ORGAN-III → VI/VII Wiring (2026-02-27)
All 23 active ORGAN-III products wired into ORGAN-VI (Community) and ORGAN-VII (Distribution):
- 23 kerygma profile YAMLs created in `organvm-vii-kerygma/kerygma-profiles/profiles/`
- Community seed data (23 events + 23 taxonomy nodes) added to `organvm-vi-koinonia/koinonia-db/seed/`
- All 23 ORGAN-III seed.yaml files now declare `produces` (community_signal, distribution_signal) and `subscriptions` (community.event_created, distribution.dispatched)
- `product.release` and `product.milestone` added to pipeline `EVENT_TEMPLATE_MAP`
- New event types available for orchestration dispatch: `product.release`, `product.milestone`

## Research Corpus Audit (2026-03-06)
See [research-audit.md](research-audit.md) for full details.

**Scope**: 16 AI chat transcripts in `organvm-iv-taxis/research/` → 83 issues across 4 repos
**SOP v2.0**: Rewrote Document Audit SOP from 5-phase/739-line to 8-phase/1,533-line universal version

**Issue totals**: 83 issues + 17 amendment comments
- orchestration-start-here: 37 issues (#82–#118)
- agentic-titan: 26 issues (#8–#33)
- petasum-super-petasum: 19 issues (#119–#137)
- agent--claude-smith: 3 issues (#14–#16)

**Key artifacts** (all in `organvm-iv-taxis/research/`):
- MANIFEST.md, FEATURE-BACKLOG.md (F-01–F-83), SYLLABUS.md
- synthesis--cross-cutting-themes.md (6 themes + risk data appendix)
- audit-completeness-proof--2026-03-06.md, audit-summary--2026-03-06.md

**SOP v2.0 key additions**: Phase 0 (source classification), Phase 3 (completeness proof gate: 80%/50%), Phase 5 (synthesis), multi-repo routing, antagonistic tension detection, document type heuristics, SYLLABUS variants, retrospective protocol.

## Key Patterns Discovered
- Many ORGAN-III repos exist under GitHub org `organvm-iii-ergon` (not `labores-profani-crux` as listed in some docs)
- ORGAN-I billing lock affects all CI — even CodeQL scheduled scans. Pages builds use different infra and also fail separately.
- `.nojekyll` file fixes Jekyll build errors for non-Jekyll repos with GitHub Pages enabled
- Cross-repo Python imports (e.g., `kerygma_social` in `distribution-strategy`) should be inlined if the dep isn't published to PyPI
- Turborepo requires `"packageManager"` field in root `package.json`
- GitHub API returns 502 under rapid-fire issue creation — use >=2s delay between `gh issue create` calls
- AI chat transcripts need different extraction heuristics than authored docs (numbered lists, named tools, "strategic gap" signals)
- Completeness proof (adversarial re-read by fresh agent) catches ~30% of missed content — mandatory for any audit
- Source clustering (docs sharing same prompt) enables 30-50% dedup within clusters
- `gh issue comment` via Bash is more reliable than `mcp__github__add_issue_comment` (401 auth issues with MCP)
