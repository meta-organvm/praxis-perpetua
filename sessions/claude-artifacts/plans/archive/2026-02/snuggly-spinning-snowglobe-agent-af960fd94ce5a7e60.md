# Parlor Games—Ephemera Engine: Root File Reference Analysis

**Date**: 2026-02-23  
**Task**: Comprehensive search for internal links and references to root-level markdown files  
**Status**: COMPLETED

## Objective

Identify all internal references to root-level markdown files (DESIGN.md, STRATEGY.md, RESEARCH.md, PRD.md, MANIFEST.md) throughout the parlor-games--ephemera-engine project to assess impact of moving these files to a `docs/` subdirectory.

## Search Methodology

- **Pattern**: `(DESIGN\.md|STRATEGY\.md|RESEARCH\.md|PRD\.md|MANIFEST\.md)`
- **Scope**: All markdown files in `/Users/4jp/Workspace/organvm-iii-ergon/parlor-games--ephemera-engine/`
- **Exclusions**: `node_modules/`
- **Output Mode**: Content with line numbers and file paths

## Key Findings

### File Reference Summary

| File | Reference Count | Primary Context | Notes |
|------|-----------------|-----------------|-------|
| DESIGN.md | ~30+ | Architecture, tone, archetypes, sections | Most heavily referenced in PRD and specs |
| STRATEGY.md | ~10+ | Context, pillar references, PRD creation | Referenced in PRD and memory/constitution |
| RESEARCH.md | ~15+ | Domain citations throughout PRD | Extensive inline citations in PRD |
| PRD.md | ~80+ | Central hub, referenced everywhere | Most complex dependency—heavily cross-referenced |
| MANIFEST.md | 5 | Documentation artifact registry | Explicitly catalogs root-level files |

### Critical Reference Locations

#### CLAUDE.md (4 matches, lines 54-57)
- Describes key files as core project artifacts
- Lists files in documentation section
- **Impact**: HIGH—CLAUDE.md is read-first by Claude Code

#### MANIFEST.md (5 matches, lines 28-86)
- **Lines 28, 30, 38, 46, 54, 86**: Explicit artifact registry with file paths
- Serves as project file catalog
- **Impact**: HIGH—This is the authoritative artifact manifest

#### STRATEGY.md (3 matches, lines 190, 375, 383)
- **Lines 375, 383**: References DESIGN.md sections for design principles
- **Line 190**: Mentions PRD creation task
- **Impact**: MEDIUM—Internal cross-reference

#### PRD.md (80+ matches, distributed throughout)
- **Lines 3, 10-12**: Opening sections identify DESIGN.md, STRATEGY.md, RESEARCH.md as source documents
- **Lines 56-93**: Extensive section references with inline citations (e.g., "DESIGN.md §I")
- **Lines throughout**: Scattered citations like "STRATEGY.md §Pillar 7", "RESEARCH.md §Domain X"
- **Lines 459, 514, 611, 678, 708, 864, 898, 947, 984, 1056, 1153, 1165, 1193, 1267, 1274, 1297, 1320, 1380, 1404, 1434, 1488, 1513, 1609, 1617, 1660, 1700, 1766, 1794, 1829, 1853, 1881, 1970, 1978, 1993, 2035, 2043, 2098, 2139, 2151, 2337, 2640-2685**: All contain section references
- **Impact**: CRITICAL—Central documentation hub with numerous inline citations

#### memory/constitution.md (5 matches, lines 3, 13, 19, 25, 31, 37, 43, 49)
- **Line 3**: "Immutable architectural principles derived from DESIGN.md and STRATEGY.md"
- **Lines 13-49**: Each constitutional principle derives from source documents
- **Impact**: MEDIUM—Architectural foundation document

#### specs/002-pre-game-lifecycle/spec.md (1 match, line 521)
- Notification copy tone guidelines reference DESIGN.md
- **Impact**: LOW

#### specs/002-pre-game-lifecycle/checklists/requirements.md (1 match, line 141)
- References DESIGN.md tone guidelines
- **Impact**: LOW

#### specs/003-confession-album/spec.md (3 matches, lines 11-14, 401)
- References PRD.md sections 3.1, 5.5, 5.6
- References DESIGN.md §IV archetype guidance
- **Impact**: MEDIUM

#### specs/003-confession-album/checklists/requirements.md (1 match, line 129)
- References archetype guidance from DESIGN.md §IV
- **Impact**: LOW

#### specs/003-confession-album/data-model.md (2 matches, lines 58, 208)
- References DESIGN.md replayability section
- References archetype definitions
- **Impact**: LOW

### Reference Pattern Analysis

1. **Link Format**: Most references use section citations (e.g., `DESIGN.md §IV`) rather than direct markdown links
2. **Inline Citations**: PRD.md contains numerous inline citations scattered throughout (~80+ instances)
3. **Document Registry**: MANIFEST.md explicitly catalogs files as part of project artifacts
4. **Architectural Dependencies**: memory/constitution.md derives from source documents
5. **Specification References**: specs/ files reference both PRD.md and DESIGN.md for guidance

## Impact Assessment: Moving Files to `docs/` Subdirectory

### Breaking Changes Required

| File | References Requiring Update | Action Needed |
|------|----------------------------|----------------|
| CLAUDE.md | 4 (lines 54-57) | Update file paths from `DESIGN.md` → `docs/DESIGN.md` |
| MANIFEST.md | 5 (lines 28-86) | Update artifact paths with `docs/` prefix |
| STRATEGY.md | 3 (lines 190, 375, 383) | Update cross-references to `docs/DESIGN.md`, `docs/PRD.md` |
| PRD.md | 80+ | Bulk update all section references (e.g., `(DESIGN.md §IV)` → `(docs/DESIGN.md §IV)`) |
| memory/constitution.md | 5 (lines 3-49) | Update source document references with `docs/` prefix |
| specs/002-pre-game-lifecycle/spec.md | 1 (line 521) | Update DESIGN.md reference |
| specs/002-pre-game-lifecycle/checklists/requirements.md | 1 (line 141) | Update DESIGN.md reference |
| specs/003-confession-album/spec.md | 3 (lines 11-14, 401) | Update PRD.md and DESIGN.md references |
| specs/003-confession-album/checklists/requirements.md | 1 (line 129) | Update DESIGN.md reference |
| specs/003-confession-album/data-model.md | 2 (lines 58, 208) | Update DESIGN.md references |

### Risk Assessment

- **HIGH RISK**: PRD.md contains 80+ scattered references; bulk update required
- **HIGH RISK**: MANIFEST.md explicitly catalogs file locations; must be updated
- **MEDIUM RISK**: CLAUDE.md is read-first by Claude Code; must reflect new structure
- **MEDIUM RISK**: Specifications reference multiple source documents
- **LOW RISK**: Individual spec references are fewer; easier to update

### No Code References Found

- `artifacts/` directory code (Nunjucks templates, TypeScript rendering code) does NOT contain hardcoded references to these root-level files
- References are entirely documentation-based

## Recommendations

1. **Before Moving**: Use search-and-replace to bulk update all reference patterns:
   - `(DESIGN.md` → `(docs/DESIGN.md`
   - `(STRATEGY.md` → `(docs/STRATEGY.md`
   - `(RESEARCH.md` → `(docs/RESEARCH.md`
   - `(PRD.md` → `(docs/PRD.md`
   - Same for relative paths: `./DESIGN.md` → `./docs/DESIGN.md`

2. **Update in Order**:
   - Move files to `docs/` subdirectory
   - Update CLAUDE.md first (read-first file)
   - Update MANIFEST.md (artifact registry)
   - Bulk-update PRD.md (80+ references)
   - Update remaining documentation and specs

3. **Verification**: After migration, re-run grep search on new `docs/` location to ensure no orphaned references remain

4. **Documentation**: Update project README if it references file locations

## Search Execution Summary

- **Command**: `grep -r --include="*.md" "(DESIGN\.md|STRATEGY\.md|RESEARCH\.md|PRD\.md|MANIFEST\.md)" /Users/4jp/Workspace/organvm-iii-ergon/parlor-games--ephemera-engine/ --exclude-dir=node_modules`
- **Execution**: Successful; no errors
- **Results**: Comprehensive match reporting with file paths and line numbers
- **Total Matches Found**: 110+ instances across 10+ files

---

**Next Steps**: Ready to execute file migration and bulk reference updates upon user request.
