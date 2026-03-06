# ORGANVM-VI Code Quality Analysis Plan

## Objective
Conduct comprehensive code quality and consistency analysis of organvm-vi-koinonia (6-repo superproject) across 5 focus areas, with specific filenames and line numbers.

## Project Structure
- **Superproject**: `/Users/4jp/Workspace/organvm-vi-koinonia/`
- **Submodules**: koinonia-db, salon-archive, reading-group-curriculum, adaptive-personal-syllabus, community-hub, .github
- **Stack**: Python 3.11+, SQLAlchemy 2.0+, PostgreSQL, FastAPI, Click, pytest, ruff

## Focus Areas & Tasks

### 1. Code Consistency Across Repos
**Goal**: Compare patterns in key files (config.py, repository.py, __main__.py) between salon-archive and reading-group-curriculum

**Files to examine**:
- `salon-archive/src/config.py`
- `salon-archive/src/repository.py`
- `salon-archive/src/__main__.py`
- `reading-group-curriculum/src/config.py`
- `reading-group-curriculum/src/repository.py`
- `reading-group-curriculum/src/__main__.py`

**What to look for**:
- Naming conventions (SalonSessionRow vs ReadingSessionRow vs model names)
- Settings class patterns
- Database connection handling
- CLI argument parsing patterns
- Error handling structure

**Status**: PENDING

---

### 2. Test Coverage Gaps
**Goal**: Read all test files in each repo, identify what IS tested vs what is NOT

**Files to examine**:
- `salon-archive/tests/` (all .py files)
- `reading-group-curriculum/tests/` (all .py files)
- `adaptive-personal-syllabus/tests/` (all .py files)
- `community-hub/tests/` (all .py files)
- `koinonia-db/tests/` (all .py files)

**What to look for**:
- Test file count and organization
- What modules have test coverage
- Untested edge cases or modules
- Repositories with minimal tests
- Patterns in test structure and naming

**Status**: PENDING

---

### 3. Error Handling Patterns
**Goal**: Examine CLI error handling across repos and verify consistency

**Files to examine**:
- `salon-archive/src/__main__.py`
- `reading-group-curriculum/src/__main__.py`
- `adaptive-personal-syllabus/src/__main__.py` (if exists)
- All Click command files with error handlers

**What to look for**:
- Try/except patterns and scope
- Custom exception definitions
- Error messages and logging
- Graceful degradation patterns
- Exit codes and error reporting

**Status**: PENDING

---

### 4. Import Organization
**Goal**: Verify imports follow consistent patterns across repos

**Files to examine**:
- All `__init__.py` files in each repo's src/
- All module files in each repo's src/

**What to look for**:
- From/import ordering (stdlib, third-party, local)
- Relative vs absolute imports
- __all__ declarations
- Type hint imports (TYPE_CHECKING, etc.)
- Circular import patterns

**Status**: PENDING

---

### 5. Code Duplication
**Goal**: Find and document duplicated patterns

**Specific items to search for**:
- `Settings.require_db()` method definition and usage
- `DATABASE_URL` conversion logic (postgresql:// to postgresql+psycopg://)
- In-memory vs database-backed implementation patterns
- Common repository base classes or mixins
- Repeated utility functions

**Files to examine**:
- All `config.py` files (Settings patterns)
- All `repository.py` files (database patterns)
- All `engine.py` or database initialization files
- All utility modules

**Status**: PENDING

---

## Execution Strategy

1. **Phase 1**: Systematically read config.py files (salon-archive, reading-group-curriculum, community-hub, koinonia-db)
2. **Phase 2**: Systematically read repository.py files across repos with database code
3. **Phase 3**: Read CLI entry points (__main__.py files)
4. **Phase 4**: Enumerate test files and assess coverage
5. **Phase 5**: Search for duplicated code patterns (require_db, DATABASE_URL conversion, etc.)
6. **Phase 6**: Verify import organization patterns
7. **Phase 7**: Compile comprehensive report with filenames and line numbers

## Deliverables

- Comprehensive report with specific examples (filenames + line numbers)
- Consistency findings with recommendations
- Test coverage assessment with gap identification
- Error handling pattern documentation
- Import organization recommendations
- Code duplication inventory with locations

## Notes
- This is READ-ONLY exploration (no file modifications)
- Focus on finding and documenting patterns, not fixing them
- All code references must include exact filenames and line numbers
- Compare patterns across repos to identify inconsistencies
