# ORGANVM Implementation Maturity Assessment Plan

## Objective
Assess implementation maturity of ORGAN-IV (Taxis), ORGAN-VI (Koinonia), and ORGAN-VII (Kerygma), with supplementary checks on ORGAN-I, II, III to determine highest-impact implementation targets.

## Methodology

### Phase 1: Explore Primary Organs (IV, VI, VII)
For each organ directory:
1. List all subdirectories (repos)
2. For each repo: check seed.yaml for metadata
3. Determine: real code vs scaffold-only
4. Read seed.yaml to extract produce/consume edges
5. Check for tests, CI workflows, data directories
6. Compile metrics per organ

### Phase 2: Supplementary Check (I, II, III)
1. List subdirectories
2. Quick scan for real working code presence

### Phase 3: Report
For each organ, output:
- Total repos count
- Repos with real code (count + list)
- Total declared produce edges (from seed.yaml)
- Fulfilled edges (count + status)
- Highest-impact repo to implement next

## Key Markers for Real Code
- `src/`, `lib/`, `scripts/` directories
- `.py`, `.ts`, `.js`, `.go`, `.rs` source files
- `pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`
- Test files: `tests/`, `spec/`, `__tests__`
- CI workflows: `.github/workflows/`

## Scaffold-Only Indicators
- Only `README.md`, `seed.yaml`, `CLAUDE.md`
- No source code directories
- No build/test configuration

## Implementation Plan Order
1. Start with ORGAN-IV (smallest, orchestrator role)
2. Then ORGAN-VI (community infrastructure)
3. Then ORGAN-VII (distribution/POSSE)
4. Quick scan of I, II, III for context

## Status Tracking
- [ ] ORGAN-IV fully explored
- [ ] ORGAN-VI fully explored
- [ ] ORGAN-VII fully explored
- [ ] ORGAN-I supplementary check
- [ ] ORGAN-II supplementary check
- [ ] ORGAN-III supplementary check
- [ ] Comprehensive report generated
