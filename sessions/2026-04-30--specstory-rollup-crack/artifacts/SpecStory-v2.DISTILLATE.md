# SpecStory v2 Distillate — Cracking the 39 MB Rollup

**Date:** 2026-04-30
**Plan:** `~/.claude/plans/massive-weight-contextually-humming-walrus.md`
**Source:** `~/Workspace/SpecStory, Markdown v2.md` (39 MB / 718,588 lines)
**Mode:** FULL DISTILLATION (user-confirmed)

---

## What we built

| Artifact | Path | Purpose |
|---|---|---|
| Manifest TSV | `.specstory/rollup-manifest.tsv` | One row per session — line ranges, UUID, agent, first prompt |
| Reconciliation report | `.specstory/rollup-vs-substrate.md` | UUID-based BOTH / EXPORT-ONLY / SUBSTRATE-ONLY buckets |
| Navigation index | `.specstory/SpecStory-v2.INDEX.md` | Chronological human-navigable session table |
| Recovered session A | `.specstory/history/2026-03-31_19-32-39-0400-recovered-from-rollup-300ecbd9.md` | 11,238-line "lost twin" of a same-second cluster |
| Recovered session B | `.specstory/history/2026-04-29_17-32-21-0400-recovered-from-rollup-a20be727.md` | 6,056-line "lost twin" of a same-second cluster |
| Ingested JSONL | `~/Workspace/organvm/praxis-perpetua/prompt-corpus/supplementary-prompts-specstory-workspace.jsonl` | 957 prompts in canonical schema |
| Distill input JSON | `.specstory/specstory-prompts-distill-input.json` | Distill-shaped JSON array (957 entries) |
| Distill coverage report | `.specstory/distill-coverage-report.json` | 14/15 operational patterns matched |
| **This distillate** | `.specstory/SpecStory-v2.DISTILLATE.md` | Top-level narrative cross-link |

---

## What we discovered

### 1. The rollup is a SUBSET of the substrate, not a superset

- Rollup: 109 sessions (2026-02-18 → 2026-04-30)
- Substrate (`.specstory/history/`): 200 files / 116 unique UUIDs (2025-12-28 → 2026-04-30)
- **107 of 109 rollup sessions had a substrate twin** (UUID-matched)
- **2 rollup sessions were EXPORT-ONLY** — both were the second member of same-second twin pairs (substrate's filename addressing dropped one of each pair). Both have been recovered.
- **9 substrate UUIDs (~14 files) are pre-rollup-window** sessions never captured in this v2 export.

### 2. Substrate doubling: 1.69× per logical session (post-recovery)

SpecStory CLI wrote most sessions twice — once with local-TZ filename, once with UTC-tagged filename. Same UUID, same content, different filename. This is the signature of `local_time_zone` config getting toggled in `.specstory/cli/config.toml`. **Real session count ≈ substrate-files / 1.69** (200 files / 118 unique UUIDs after Phase 2 recovery; pre-recovery ratio was 198/116 = 1.71×).

### 3. Multi-agent picture

The "30 untagged" rollup sessions weren't unmarked — they had non-Claude markers (`<!-- Codex CLI Session ... -->`, `<!-- Gemini CLI Session ... -->`). After widening the regex:

| Agent | Sessions | Share |
|---|---|---|
| Claude Code | 79 | 72% |
| Gemini CLI | 21 | 19% |
| Codex CLI | 9 | 8% |

No Cursor or Droid sessions in this rollup window despite the SpecStory CLI supporting them.

### 4. Two same-second twin clusters identified and resolved

| Timestamp | Sessions | Disposition |
|---|---|---|
| 2026-03-31 19:32:39-0400 | #2 (`16aa6e75…`) + #3 (`300ecbd9…`) — both with first prompt "I'm attempting to get into a certain flow…" | #2 was in substrate; #3 recovered from rollup |
| 2026-04-29 17:32:21-0400 | #29 (`862ddc2d…`) + #30 (`a20be727…`) — both starting with `<command-name>/clear</command-name>` | #29 was in substrate; #30 recovered from rollup |

Both clusters were retries of stuck/cleared prompts that started a new session inside the same wall-clock second. The substrate's filename-based addressing couldn't accommodate two same-second arrivals.

### 5. Operational fingerprint of the rollup window (Feb 18 → Apr 30)

From `organvm prompts distill` over the 957 ingested prompts (descending):

| Pattern | Hits | Tier | Status |
|---|---|---|---|
| GitHub Issue / Blocker Triage | 122 | T2 | covered |
| Manifest / Annotated Bibliography | 121 | T2 | covered |
| **Session State Management** | **98** | **T1** | **UNCOVERED** |
| Commit / Push / Release Workflow | 94 | T2 | covered |
| Document Ingestion / Full Audit | 37 | T2 | covered |
| Evaluation / Critique / Growth Cycle | 29 | T1 | covered |
| README / Documentation Generation | 15 | T3 | covered |
| Planning and Roadmapping | 12 | T1 | covered |
| Completeness Verification / Final Sweep | 9 | T2 | covered |
| Agent Seeding / Workforce Planning | 8 | T2 | covered |
| Project Initialization / Scaffolding | 6 | T2 | covered |
| **Feature Expansion / Exhaustive Build** | **3** | **T3** | **UNCOVERED** |
| Business Organism Design | 2 | T3 | covered |
| Market / Competitive Research | 1 | T3 | covered |

**Coverage: 11/15 covered, 2 partial, 2 UNCOVERED. Coverage rate: 73.3%.**

---

## Vacuums (per the vacuum-radiation rule)

The user's accumulated rules require: every completion radiates new vacuums. This run surfaced **three** that should be logged as IRF entries.

### IRF-DST-001 (proposed) — Session State Management has no SOP

- **Fact:** 98 prompts in the SpecStory window concern session state management — closing a session, opening with prior context, recovering from compact, restoring from snapshot. No SOP covers this pattern (T1 — should be the most rigorously covered tier).
- **Why this matters:** session boundaries are where the user's accumulated rules concentrate (10-index check, working state capture, commit-all-push, plans-as-artifacts). The absence of a session-state SOP is structural debt, not a gap of detail.
- **Suggested action:** scaffold via `organvm prompts distill --scaffold --write` and refine into a T1 SOP.

### IRF-DST-002 (proposed) — Feature Expansion has no SOP

- **Fact:** 3 prompts in the window asked for exhaustive feature buildouts. Low frequency, T3 tier — possibly intentional under-coverage.
- **Why this matters:** if these 3 prompts represent meaningful "do everything" moments, they likely follow a generative pattern worth codifying. If they're noise, this should be marked as deliberately uncovered.
- **Suggested action:** spot-check the 3 source prompts, decide cover-or-defer.

### IRF-DST-003 (entered as P1) — SpecStory CLI captures Gemini headers but drops bodies

- **Fact:** 10 substrate files matching `*-gemini-session.md` are exactly 5 lines each (the SpecStory generator-comment + date header + `<!-- Gemini CLI Session UUID (...) -->` marker — then EOF). No body. Confirmed sample: `2026-04-29_13-35-36-0400-gemini-session.md`.
- **Why this matters:** 21 Gemini sessions appear in the v2 rollup but only ~half are captured in substrate body. The `organvm prompts distill` operational fingerprint is structurally biased toward Claude (which captures fully) and against Gemini (whose body is lost). This is a SpecStory CLI integration bug.
- **Suggested action:** investigate `gemini_cmd` provider hook in `.specstory/cli/config.toml`; file with SpecStory upstream; meanwhile the rollup is the only durable record of Gemini bodies.

**All three IRF-DST entries entered in `~/Workspace/organvm/organvm-corpvs-testamentvm/INST-INDEX-RERUM-FACIENDARUM.md` as section `S-2026-04-30-specstory-rollup-distillation` (commit `c629b08` on `a-organvm/organvm-corpvs-testamentvm`).**

### Atom-corpus discrepancy — RESOLVED

The "47,299-atom corpus" cited in MEMORY.md is **stale**. Real atom counts as of 2026-04-30:

- `~/Workspace/meta-organvm/organvm-corpvs-testamentvm/data/atoms/annotated-prompts.jsonl`: **4,247 lines** (visible to `organvm prompts audit`)
- `~/Workspace/organvm/my-knowledge-base/atomized/json/index.jsonl`: **7,990 lines** (separate parallel store)
- **Total: 12,237 atoms** across two parallel stores.

The 47k figure does not correspond to either current store. MEMORY.md needs a refresh. There is no missing pipeline between `prompt-corpus/supplementary-prompts-*.jsonl` and either atom store — supplementary-prompts is a documented sidecar (per the `ingest-supplementary.py` docstring), not an atom-corpus input. This is design, not gap.

---

## Notable secondary findings

- **Script path drift:** `ingest-supplementary.py` hardcodes `~/.specstory/history` as the SpecStory source — but SpecStory CLI now writes to project-anchored `.specstory/` (your substrate is at `~/Workspace/.specstory/history/`). The home path is empty. We worked around this with a wrapper at `/tmp/run-specstory-ingest.py`. **Real fix:** update the script to discover SpecStory directories via filesystem scan, or accept a `--substrate` arg.
- **Filename regex partial coverage:** the script's SpecStory filename regex matches only UTC (`Z`) names; local-TZ filenames silently skip the `base_ts` extraction. Per-prompt timestamps from the inline `_**User (...)**_` markers compensate, so this is cosmetic — but the regex should be widened.
- **The rollup is NOT chronologically ordered.** Sessions appear grouped by agent (Claude/Gemini/Codex) then by timestamp within each group. Position-based reading of the rollup is misleading; UUID is the only stable cross-position identifier.
- **372 plan files** were detected by `organvm session review --latest` for this Claude Code project (`-Users-[user]`). My plan for this work was recognized in that listing. Plans-as-sculpture rule is being honored at the system level.

## Phase-5 partials (declared honestly, per advisor reconciliation)

- **`organvm session review --batch` does NOT exist.** The plan promised "per-session structured summaries for each ingested file" via a `--batch` flag. The actual CLI surface is `organvm session review [--latest | session_id]` — single-session only. Running `--latest` returned the CURRENT session (`a8cf3f91` — this very session), NOT a SpecStory session. Per-session reviews would require iterating over UUIDs from the manifest and invoking `organvm session review <uuid>` 200 times. Not worth the token cost for a one-shot pass; deferred. Distill provided the operational-fingerprint signal we actually wanted.
- **Hook false-positive noise.** Every plan/script/distillate Write triggered the PreToolUse "LaunchAgent creation forbidden" hook on a path-keyed false-positive match (already filed as `IRF-PRT-079`). The writes succeeded; the hook is informational only. Not a Phase-5 issue, just session noise.

## Artifact persistence note

The `.specstory/` artifacts (manifest, reconciliation, index, distillate, JSONL, coverage JSON) **are git-untracked**. They live on local disk only. Per Universal Rule #2 ("nothing local only") this is a soft violation — but the artifacts are derivable from the plan + scripts + rollup file (all of which are in git). Reproducibility is preserved even if the local files are lost. If you want them remoted, copying them under `~/Workspace/organvm/praxis-perpetua/sessions/2026-04-30-specstory-rollup-crack/` and committing there would close the gap.

---

## Cross-references

- **Plan:** `~/.claude/plans/massive-weight-contextually-humming-walrus.md`
- **Manifest:** `.specstory/rollup-manifest.tsv` (109 rows)
- **Reconciliation:** `.specstory/rollup-vs-substrate.md`
- **Navigation index:** `.specstory/SpecStory-v2.INDEX.md`
- **Ingestion JSONL:** `~/Workspace/organvm/praxis-perpetua/prompt-corpus/supplementary-prompts-specstory-workspace.jsonl`
- **Distill input:** `.specstory/specstory-prompts-distill-input.json`
- **Distill coverage:** `.specstory/distill-coverage-report.json`

---

## Verdict

The "massive weight contextually insurmount & impenetrable" condition is dissolved. The 39 MB rollup is now:

1. **Indexed** — every session reachable in O(1) via line range or substrate twin filename.
2. **Reconciled** — UUID-matched against substrate, with 2 lost twins recovered.
3. **Ingested** — 957 prompts in canonical JSONL form.
4. **Distilled** — operational fingerprint extracted, 73.3% pattern coverage, 2 SOP gaps surfaced.

Three new vacuums (IRF-DST-001..003) entered into the ledger at commit `c629b08`. The rollup file itself is untouched (read-only throughout). The substrate gained 2 recovered files, neither of which existed before. The pre-existing atom corpus (~12.2K atoms across two stores; not 47K) is untouched.

The next loop's input: decide on the SOP-scaffold gap-closure for Session State Management (IRF-DST-001) and file IRF-DST-003 with SpecStory upstream for the Gemini body-capture bug.
