# Structural Patterns

Recurring structural issues and their fixes. Each pattern is generalized from specific session observations.

---

## SP1: The Silent Gitignore

**Pattern:** Superproject uses allowlist `.gitignore` (`*` then `!file`). New files are created but never tracked because they aren't in the allowlist.

**Symptom:** File exists on disk, agent claims it's committed, but `git status` doesn't show it.

**Fix:** Always verify with `git status` after file creation. Add to allowlist or (better) move files to a submodule where git tracks by default.

**First observed:** 2026-03-06 Gemini session (METADOC + SOP files)

---

## SP2: The Orphaned Reader

**Pattern:** Data is migrated from location A to location B. Code that reads from A continues to work but returns stale/empty data.

**Symptom:** No errors, no test failures. Output data is silently wrong.

**Fix:** When moving data, grep for all readers of the old location. The writer knows about the move; the readers don't.

**First observed:** 2026-03-06 structural audit (F1: compute_vitals reading emptied manual dict)

---

## SP3: The Destructive Rewrite

**Pattern:** Agent overwrites files with `open(path, "w")` instead of targeted edits. Multiple writes in a session lose all intermediate versions.

**Symptom:** Git log shows only one version (the last write). Revision history is irrecoverable.

**Fix:** Commit after each write cycle when using agents prone to this pattern. Use agents with targeted edit tools (Edit vs. Write) when possible.

**First observed:** 2026-03-06 Gemini session

---

## SP4: The Incomplete Lookup Table

**Pattern:** A dictionary/map covers some cases but returns zero values for uncovered ones without raising an error.

**Symptom:** Function produces correct output for mapped inputs, wrong output for unmapped ones. Tests only cover mapped inputs.

**Fix:** Exhaustive tables (cover all cases) or defensive tables (raise on unknown key).

**First observed:** 2026-03-06 structural audit (F3: organ_map with 4 of 8 entries)

---

## SP5: The Frozen Import

**Pattern:** Value computed at module load time (`CONSTANT = compute()`) ignores runtime changes to environment or filesystem.

**Symptom:** Works in tests (environment is stable). Fails in production when environment variables or paths differ from import-time state.

**Fix:** Replace module-scope computation with a function call at use-time.

**First observed:** 2026-03-06 structural audit (F6: DEFAULT_REGISTRY_PATH)

---

*Last updated: 2026-03-06 | Updated as patterns recur across sessions*
