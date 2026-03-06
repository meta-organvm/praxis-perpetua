# SOP: Structural Integrity Audit (The Floor You Eat From)

## 1. Ontological Purpose
This SOP defines the process for achieving verified structural integrity in any codebase, document corpus, or engineered system. It is not a linting pass. It is not a test count exercise. It is the systematic exposure of silent lies — logic that produces wrong data without raising errors, contracts that promise coverage but deliver hollow assertions, and structural assumptions that rot from within.

The standard is gravitational: the system must hold under its own weight without patchwork, bandaids, or swept debris. Every component must be verified against what it *claims* to do, not what its tests *claim* to check.

**Applicable to:** All ORGANVM projects, all codebases, all structured systems. Governed by `METADOC--research-standards.md`.

---

## 2. Phase I: Cartography (Mapping the Territory)
**Goal:** Establish a complete map of what exists before judging what's missing.

### Process
1. **Enumerate all production units** — modules, files, classes, functions, documents, schemas. Every unit that carries intent.
2. **Enumerate all verification units** — tests, validators, assertions, checks. Everything that claims to verify a production unit.
3. **Build the coverage matrix** — map each production unit to its verification units. Identify:
   - **Uncovered units**: production code with zero verification
   - **Orphaned tests**: verification targeting deleted or renamed production code
   - **Stub declarations**: functions/modules that exist syntactically but do nothing (`pass`, `raise NotImplementedError`, placeholder prints)

### Starter Research Questions
- *What does this system claim to do?* (Read its README, its CLI help, its API surface)
- *What are its public interfaces?* (Every function/class/endpoint a consumer can call)
- *Which modules have the highest fan-out?* (Most imports = most blast radius if wrong)
- *Where does data enter the system, and where does it exit?* (Boundaries are where bugs breed)
- *What is tested vs. what is exercised?* (A function called during a test is not the same as a function whose behavior is asserted)

---

## 3. Phase II: Coverage Saturation (Filling the Gaps)
**Goal:** Bring every production unit under at least one meaningful assertion. Not line coverage — behavioral coverage.

### Process
1. **Prioritize by risk**: Functions that write data > functions that transform data > functions that read data > pure utilities.
2. **Write tests that assert behavior, not implementation**: Test what the function *promises*, not how it achieves it.
3. **Implement stubs**: Any `NotImplementedError`, placeholder, or "Phase B" stub must either be implemented or explicitly marked as deferred with a tracking issue.
4. **Isolation discipline**: Every test must use `tmp_path`, mocks, or fixtures. Zero production filesystem access. Zero network calls. Zero shared mutable state.

### Starter Research Questions
- *If this function returned wrong data silently, what downstream system would break?*
- *What are the input boundaries?* (Empty list, None, negative numbers, Unicode, paths with spaces)
- *What external systems does this code touch?* (subprocess, filesystem, network, database — each must be mocked)
- *What does "success" look like for this function? What does "silent failure" look like?*
- *Can I write a test that would have caught the last bug filed against this module?*

---

## 4. Phase III: Adversarial Self-Review (The Mirror)
**Goal:** Re-read all work as if a hostile reviewer is trying to find reasons to reject it. Every flaw found is a step toward internal harmony.

### Process
1. **Re-read every file you created or modified** — not skimming, reading. Line by line.
2. **Check for these specific failure modes:**
   - Dead imports (imported but never used)
   - Dead parameters (accepted but never read)
   - Weak assertions (`>= 5` when the exact count is known and stable)
   - Side effects (tests that create real directories, write to production paths, or leave state)
   - Redundant work (in-method imports that belong at module level)
   - Missing test coverage for new production code you just wrote
3. **Fix immediately** — do not log for later. The cost of fixing now is near zero; the cost of fixing later includes rediscovery.

### Starter Research Questions
- *If I deleted this test, would any CI pipeline notice?*
- *Does this test actually fail when the production code is wrong, or does it pass vacuously?*
- *Am I testing the mock or the real code?*
- *Would a new contributor understand what this test verifies by reading its name alone?*
- *Did I introduce any side effects that survive beyond this test's scope?*

---

## 5. Phase IV: Deep Structural Audit (Reading the Marrow)
**Goal:** Read production source code — not tests — for logic errors, silent data corruption, broken contracts, and architectural lies. This is where the real bugs live.

### Process
1. **Read each production file completely.** Not grep. Not skim. Read.
2. **Hunt for these specific pathologies:**

   | Pathology | Description | Example |
   |-----------|-------------|---------|
   | **The Emptied Source** | Data migrated from location A to B, but a reader still reads from A | `compute_vitals` reading from `manual` after `write_metrics` moved fields to `computed` |
   | **The Lying Default** | `dict.get(key, default)` returns `None` when key exists with value `None`, not the intended default | `classification.get("target_repo", "unspecified")` returning `None` |
   | **The Incomplete Map** | Lookup table covers some cases but silently returns empty/zero for others | Organ map with 4 of 8 entries; unmapped organs get `target_organ: ""` |
   | **The Dead Conditional** | Both branches of if/else do identical work; code lies about its intent | Bookmark pruning that walks everything regardless |
   | **The Asymmetric Check** | Parallel code paths check for different things when they should be consistent | `"MET4" in rel_path or "MET4_Fuse" in file_path` |
   | **The Frozen Import** | Value computed at module load time, ignoring runtime environment changes | `DEFAULT_PATH = compute_path()` at module scope |
   | **The Invisible Edge** | Sentinel values (`-1`, `None`, `""`) that pass through comparison operators without triggering alerts | `stale_days=-1` making `-1 > 90` False, hiding never-validated repos |

3. **Trace data flow end-to-end**: Pick a datum (a repo name, a metric value, a classification status) and follow it from entry point to final output. Every transformation is a potential corruption site.
4. **Verify contracts at boundaries**: Where two modules exchange data, verify the producer's output matches the consumer's expectations. Type, nullability, key presence, value ranges.

### Starter Research Questions
- *If I changed this function to return garbage, which downstream consumer would notice first? Would ANY notice?*
- *Where does this module read data that another module writes? Are they using the same schema?*
- *What happens when the input is technically valid but semantically meaningless?* (Empty string, zero-length list, None where a dict is expected)
- *Are there any `dict.get()` calls where the key might exist with value `None`?*
- *Are there any lookup tables that could be missing entries for new/future cases?*
- *Is this value computed once at import time when it should be computed at call time?*
- *What does this comparison do when the value is -1, 0, None, or empty string?*

---

## 6. Phase V: Fix + Regression Lock (The Seal)
**Goal:** Every fix must be accompanied by a test that would have caught the original bug. The system must be harder to break tomorrow than it was today.

### Process
1. **Fix the production code** — minimal, targeted changes. Do not refactor surrounding code.
2. **Write a regression test** that exercises the exact failure mode. The test should FAIL against the old code and PASS against the new code.
3. **Run the full test suite** — every subproject, every test. A fix that breaks something else is not a fix.
4. **Run linters** — ensure no import errors, no style violations introduced by the fix.
5. **Verify the fix addresses the root cause, not the symptom.** If `dict.get()` returns `None`, don't add a null check downstream — fix the `.get()` call itself.

### Starter Research Questions
- *Can I write a test that fails without my fix and passes with it?*
- *Does my fix change behavior for any case that was previously correct?*
- *Did my fix create any new imports, and are all existing import sites still valid?*
- *Is there a second location in the codebase with the same pattern I just fixed?*

---

## 7. Derived Principles (Lessons from Practice)

These are not abstract ideals. Each was learned from a specific failure encountered during structural audits.

1. **`dict.get(key, default)` does not protect against `None`.** When the key exists with value `None`, the default is not used. The fix pattern is `dict.get(key) or default`. Know the difference between "key absent" and "value null."

2. **Dead conditionals are not harmless.** They lie about intent. The next person who reads `if X: do_thing() else: do_thing()` will assume the branches differ and "fix" one, introducing a real bug. Remove them or make them real.

3. **Data migration creates orphaned readers.** When you move a field from location A to location B, you must audit every reader of A. `grep` is not optional — it is mandatory. The writer knows about the move; the readers don't.

4. **Module-scope evaluation freezes runtime behavior.** `CONSTANT = expensive_function()` runs once at import. If the function depends on environment variables or filesystem state that can change, call it at use-time, not import-time.

5. **Incomplete lookup tables are silent bombs.** A map with 4 of 8 entries returns the zero value for the other 4 without raising an error. Every lookup table must either cover all cases or explicitly raise on the uncovered ones.

6. **Test coverage does not equal correctness.** 719 tests passed while 3 CRITICAL bugs silently corrupted data in production paths. Tests verify what you thought to check; audits verify what you didn't think to check.

7. **Sentinel values are invisible to comparison operators.** `-1 > 90` is `False`. `None > 0` raises `TypeError` in Python 3 but silently returns `False` in some contexts. Every sentinel must be handled before it reaches a comparison.

---

## 8. Execution Cadence

| Trigger | Action |
|---------|--------|
| New module added | Phase I (map) + Phase II (cover) |
| Feature branch merged | Phase III (self-review) |
| Major milestone (promotion, release) | Full Phase I-V |
| Bug reported in production | Phase V first (fix + lock), then Phase IV on the surrounding module |
| Quarterly | Full Phase IV on highest-risk modules (data writers, API boundaries, state machines) |

---

## 9. Completion Criteria

The audit is complete when:
- [ ] Every production module has at least one behavioral test
- [ ] Zero stubs (`NotImplementedError`, placeholder prints, "Phase B" deferred work)
- [ ] Full test suite passes (all subprojects, zero failures)
- [ ] Linter passes (zero violations in production code)
- [ ] Phase IV pathology checklist reviewed against every data-writing function
- [ ] Every fix has a regression test that would catch recurrence
- [ ] No test accesses production filesystem, network, or shared state

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
