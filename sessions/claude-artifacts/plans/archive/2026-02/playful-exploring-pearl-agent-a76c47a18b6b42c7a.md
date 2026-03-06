# Koinonia-DB Exploration Plan

## Objective
Thoroughly analyze the koinonia-db submodule to document:
1. Current state of database models, migrations, and seed data
2. Implemented vs stubbed/TODO functionality
3. Completeness of syllabus_service.py
4. Engine.py async setup details
5. Any TODOs, FIXMEs, or incomplete areas
6. Alembic migration history coverage
7. Seed data population status
8. Test coverage

## Exploration Strategy

### Phase 1: Project Configuration & Metadata
- [ ] Read `pyproject.toml` - dependencies, versions, entry points
- [ ] Read `seed.yaml` - organ/repo metadata, promotion status
- [ ] Read any README files in root
- [ ] Check for `.github/` documentation

### Phase 2: Database Models & Schema
- [ ] Examine `src/koinonia_db/models/__init__.py` - model exports
- [ ] Review all model files in `src/koinonia_db/models/` directory:
  - [ ] salons schema models
  - [ ] reading schema models
  - [ ] community schema models
  - [ ] syllabus schema models
- [ ] Document all model classes, fields, relationships
- [ ] Note any TODOs or incomplete fields

### Phase 3: Database Engine & Connection
- [ ] Read `src/koinonia_db/engine.py` - async engine setup
- [ ] Read any config/settings files
- [ ] Understand async initialization and engine factory

### Phase 4: Service Layer
- [ ] Read `src/koinonia_db/syllabus_service.py` - implementation completeness
- [ ] Check for any other service files
- [ ] Document all exported functions and TODOs

### Phase 5: Migrations
- [ ] List all files in `alembic/` directory
- [ ] Read `alembic/versions/` to see migration history
- [ ] Review `alembic.ini` configuration
- [ ] Document migration progression and schema coverage

### Phase 6: Seed Data
- [ ] List contents of `seed/` directory
- [ ] Examine each JSON fixture file
- [ ] Document what data exists and what's missing
- [ ] Review `load_seed.py` implementation

### Phase 7: Testing
- [ ] List all test files in `tests/` directory
- [ ] Review test coverage by schema
- [ ] Note gaps in test coverage

### Phase 8: Documentation Review
- [ ] Check for any `.md` files or documentation
- [ ] Review docstrings in key modules

## Expected Output
A comprehensive analysis document detailing:
- Project metadata and configuration
- Complete ORM model inventory across all 4 schemas
- Async engine setup details
- Syllabus service functionality assessment
- Migration history and coverage
- Seed data inventory
- Test coverage gaps
- List of all TODOs/FIXMEs with locations
