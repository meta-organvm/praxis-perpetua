# Testing State Audit Plan for organvm-iii-ergon

**Date**: 2026-02-27  
**Scope**: Comprehensive testing state analysis across 27 submodules in `/Users/4jp/Workspace/organvm-iii-ergon/`  
**Status**: PLANNING

## Objective

Systematically audit the testing infrastructure and coverage state across all active submodules in ORGAN-III (Commerce), generating a summary table showing:
- Repo name
- Test framework(s) detected
- Number of test files
- Number of actual test functions/cases
- Number of stubs/skips
- Assessment (full/partial/none/stubs-only)

## Methodology

### Phase 1: Directory & Configuration Scan
For each of the 27 submodules:

1. **Test Directory Detection**
   - Check for: `tests/`, `test/`, `__tests__/`, `spec/`, `__spec__/`
   - Record directory structure

2. **Framework Detection**
   - Parse `package.json` for test scripts and dependencies (vitest, jest, mocha, jasmine)
   - Parse `pyproject.toml` for test dependencies (pytest, unittest, nose2)
   - Parse `build.gradle` or `pom.xml` for Java test frameworks
   - Check for Swift test framework references
   - Identify test config files:
     - `vitest.config.ts`, `vitest.config.js`
     - `jest.config.js`, `jest.config.ts`
     - `pytest.ini`, `pyproject.toml`, `setup.cfg`, `conftest.py`
     - `karma.conf.js`, `mocha.opts`
     - `Makefile` or shell scripts with test targets

3. **Test Script Discovery**
   - Extract test commands from:
     - `package.json` → `"test"`, `"test:unit"`, `"test:e2e"`, `"spec"`
     - `pyproject.toml` → `[tool.pytest]` or `scripts`
     - `Makefile` → `test` targets
     - Shell scripts in root or scripts/ directory

### Phase 2: Test File Enumeration
For each test directory found:

1. **Count Test Files by Type**
   - Python: `test_*.py`, `*_test.py`, `conftest.py`
   - TypeScript/JavaScript: `*.test.ts`, `*.test.tsx`, `*.spec.ts`, `*.spec.tsx`, `*.test.js`, `*.spec.js`
   - Java: `*Test.java`, `*Tests.java`, `*TestCase.java`
   - Swift: `Tests.swift`, `*Tests.swift`
   - Go: `*_test.go`
   - Rust: `#[cfg(test)]` modules, `tests/` directory

2. **Empty/Stub Detection**
   - File size check (< 200 bytes likely stub)
   - Search for placeholder patterns:
     - Python: `pass`, `...`, `NotImplementedError`, `raise NotImplementedError`
     - TypeScript/JavaScript: `expect.todo()`, `describe.skip()`, `it.skip()`, `xit`, `xdescribe`
     - Java: `@Ignore`, `@Test(enabled=false)`, `@Disabled`
     - Empty test classes/functions

### Phase 3: Test Case Counting
For each test file:

1. **Function/Case Count**
   - Python: Count `def test_*` functions, classes inheriting from `TestCase`
   - TypeScript/JavaScript: Count `it(...)`, `test(...)`, `describe.each()` blocks
   - Java: Count methods with `@Test` annotation
   - Swift: Count XCTest methods

2. **Skip/Pending Detection**
   - Python: `@pytest.mark.skip`, `@unittest.skip`, `pytest.xfail()`
   - TypeScript/JavaScript: `it.skip()`, `xit()`, `it.todo()`, `xdescribe()`, `describe.skip()`
   - Java: `@Ignore`, `@Disabled`, `@Test(enabled=false)`
   - Swift: `XCTSkip()`
   - Comments with `TODO`, `FIXME`, `SKIP`, `PENDING`, `DISABLED`

### Phase 4: Source Code Coverage Check
For each repo:

1. **Identify Source Directories**
   - TypeScript/JavaScript: `src/`, `lib/`, `packages/*/src/`
   - Python: module root, `src/`, `lib/`
   - Java: `src/main/java/`
   - Swift: `Sources/`

2. **Find Untested Code**
   - Core business logic files with no corresponding test file
   - Utility modules, helpers without tests
   - API handlers/controllers without coverage

### Phase 5: Summary Generation
Create a markdown table with columns:
| Repo | Framework | Test Files | Test Cases | Stubs/Skips | Assessment |

**Assessment Scale**:
- **full**: >80% code coverage estimated, comprehensive test suite
- **partial**: 30-80% coverage, meaningful tests but gaps
- **minimal**: <30% coverage, few tests
- **stubs-only**: Test files exist but mostly empty/skipped
- **none**: No test infrastructure

## Tech Stack Breakdown

From CLAUDE.md, submodules use:
- **Node/TypeScript**: ~15 repos (vitest, jest, mocha)
- **Python**: ~4 repos (pytest, unittest)
- **Kotlin/Android**: 1 repo (JUnit, Espresso)
- **Swift/macOS**: 1 repo (XCTest)
- **Shell/Make**: 1 repo (no traditional unit tests)
- **Specification-only**: 4 repos (no code)

## Exclusion List

Skip scanning:
- `node_modules/`, `vendor/`, `.venv/`, `env/`
- `.git/`, `.github/`
- `build/`, `dist/`, `.next/`, `out/`
- `__pycache__/`, `*.pyc`
- `target/` (Maven/Gradle)
- `coverage/`, `.nyc_output/`
- `*.log`, `*.tmp`

## Execution Plan

1. Iterate through each of 27 subdirectories
2. For each repo:
   - Detect tech stack from config files
   - Locate test directories
   - Enumerate test files and count
   - Parse test files for function counts and skip markers
   - Identify source code without tests
   - Assign assessment rating
3. Aggregate results into summary table
4. Generate diagnostic notes for repos with gaps

## Output

**Final Deliverable**: Markdown table with 27 rows (one per repo) showing:
- Repo name (from directory)
- Test framework(s) (if detected)
- Count of test files
- Count of test functions/cases
- Count of stubs/skipped tests
- Assessment (full/partial/minimal/stubs-only/none)
- Notes (any interesting findings)

## Risk Mitigation

- Monorepos (life-my--midst--in, peer-audited--behavioral-blockchain, the-actual-news): Count all test files across workspaces
- Archived/design-only repos: Will have no or minimal tests (expected)
- Hybrid stacks: Some repos may have multiple test frameworks
- Specification repos: No code/tests (will be marked "specification-only")

---

## Implementation Notes

This plan is ready to execute. The scan will be systematic and read-only, examining only configuration files, test directories, and test source code to build an accurate inventory of the testing state across ORGAN-III.
