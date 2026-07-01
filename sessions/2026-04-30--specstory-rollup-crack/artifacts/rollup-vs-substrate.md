# Rollup ↔ Substrate Reconciliation Report (v2 — UUID-based)

- **Manifest:** `~/Workspace/.specstory/rollup-manifest.tsv`
- **Substrate root:** `~/Workspace/.specstory/history`

## Counts

- Rollup sessions: **109** (with UUID: 109, without: 0)
- Substrate files: **198** (unique UUIDs: 116, no-UUID parsed: 0)
- Substrate doubling factor: **1.71×** (local-TZ + UTC dual-write)
- BOTH (UUID matched): **107**
- EXPORT-ONLY (rollup UUID has no substrate file): **2**
- SUBSTRATE-ONLY (substrate UUID has no rollup session): **9** (9 by UUID + 0 no-UUID parsed)
- Same-timestamp clusters in rollup: **2**
- Rollup sessions WITHOUT UUID (likely TUI/non-Claude): **0**

## Rollup agent distribution

- **Claude Code**: 79
- **Gemini CLI**: 21
- **Codex CLI**: 9

## Same-timestamp clusters in rollup

### 2026-03-31 19:32:39-0400

| idx | line_start | line_end | uuid | first prompt |
|---|---|---|---|---|
| 2 | 2246 | 12071 | `16aa6e75…` | I'm attempting to get into a certain flow, an orchestrator flow, something that  |
| 3 | 12072 | 23309 | `300ecbd9…` | I'm attempting to get into a certain flow, an orchestrator flow, something that  |

### 2026-04-29 17:32:21-0400

| idx | line_start | line_end | uuid | first prompt |
|---|---|---|---|---|
| 29 | 293035 | 306701 | `862ddc2d…` | <command-name>/clear</command-name> |
| 30 | 306702 | 312757 | `a20be727…` | <command-name>/clear</command-name> |

## EXPORT-ONLY (2 sessions only in rollup)

These sessions exist in the rollup but no substrate file with a matching UUID was found. Candidates for recovery to `.specstory/history/`.

| idx | timestamp | agent | uuid | line range | first prompt |
|---|---|---|---|---|---|
| 3 | 2026-03-31 19:32:39-0400 | Claude Code | `300ecbd9-654…` | 12072-23309 | I'm attempting to get into a certain flow, an orchestrator flow, something that  |
| 30 | 2026-04-29 17:32:21-0400 | Claude Code | `a20be727-c85…` | 306702-312757 | <command-name>/clear</command-name> |

## ROLLUP WITHOUT UUID (0 sessions)

These rollup sessions have no recognizable session marker. Cannot be UUID-matched; we'd fall back to slug+date matching but skip for now.

## SUBSTRATE-ONLY (14 files)

(9 unique-UUID sessions + 0 unparseable files)

```
2025-12-28_17-18-08-0500.md
2025-12-28_22-18-08Z.md
2026-03-25_13-15-57-0400.md
2026-03-25_17-15-57Z.md
2026-03-28_00-07-33Z.md
2026-03-28_03-19-42Z-i-want-to-codify.md
2026-04-29_12-51-16-0400-first-peak-into-a.md
2026-04-29_12-51-16-0400-gemini-session.md
2026-04-29_13-35-36-0400-gemini-session.md
2026-04-29_16-12-44-0400-gemini-session.md
2026-04-29_16-42-53Z-gemini-session.md
2026-04-29_16-51-16Z-first-peak-into-a.md
2026-04-29_16-51-16Z-gemini-session.md
2026-04-29_21-16-20-0400-gemini-session.md
```

## BOTH (107 UUID-matched pairs — first 30 shown)

| idx | timestamp | agent | line range | substrate file(s) |
|---|---|---|---|---|
| 80 | 2026-02-18 11:43:16-0500 | Codex CLI | 597565-598900 | `2026-02-18_11-43-16-0500-generate-a-file-named.md`, `2026-02-18_16-43-16Z-generate-a-file-named.md` |
| 81 | 2026-03-31 04:05:46-0400 | Codex CLI | 598901-607273 | `2026-03-31_04-05-46-0400-users-[user]-workspace-organvm.md`, `2026-03-31_08-05-46Z-users-[user]-workspace-organvm.md` |
| 82 | 2026-04-01 19:18:22-0400 | Codex CLI | 607274-615900 | `2026-04-01_19-18-22-0400-investigation-complete-i-have.md`, `2026-04-01_23-18-22Z-investigation-complete-i-have.md` |
| 83 | 2026-04-02 11:08:21-0400 | Codex CLI | 615901-624454 | `2026-04-02_11-08-21-0400-other-session-hash-handoff.md`, `2026-04-02_15-08-21Z-other-session-hash-handoff.md` |
| 84 | 2026-04-02 12:56:38-0400 | Codex CLI | 624455-626557 | `2026-04-02_12-56-38-0400-data-referenced-scheduled-review.md`, `2026-04-02_16-56-38Z-data-referenced-scheduled-review.md` |
| 85 | 2026-04-02 14:17:43-0400 | Codex CLI | 626558-627935 | `2026-04-02_14-17-43-0400-to-create-a-better.md`, `2026-04-02_18-17-43Z-to-create-a-better.md` |
| 86 | 2026-04-27 23:39:28-0400 | Codex CLI | 627936-649563 | `2026-04-27_23-39-28-0400-continue-where-i-forced.md`, `2026-04-28_03-39-28Z-continue-where-i-forced.md` |
| 87 | 2026-04-29 12:08:52-0400 | Codex CLI | 649564-655391 | `2026-04-29_12-08-52-0400-below-is-your-workload.md`, `2026-04-29_16-08-52Z-below-is-your-workload.md` |
| 88 | 2026-04-29 12:23:13-0400 | Codex CLI | 655392-660364 | `2026-04-29_12-23-13-0400-review-method-anyone-who.md`, `2026-04-29_16-23-13Z-review-method-anyone-who.md` |
| 99 | 2026-04-06 18:16:34-0400 | Gemini CLI | 699061-701261 | `2026-04-06_18-13-17-0400-first-act-is-a.md`, `2026-04-06_22-13-17Z-first-act-is-a.md` |
| 31 | 2026-04-29 13:53:13-0400 | Claude Code | 312758-318854 | `2026-04-29_13-49-33-0400-1-gemini-gemini-cli.md` |
| 32 | 2026-04-29 11:28:56-0400 | Claude Code | 318855-318933 | `2026-04-29_11-28-44-0400-opencode-bug.md`, `2026-04-29_15-28-44Z-opencode-bug.md` |
| 10 | 2026-04-04 14:56:22-0400 | Claude Code | 95382-95997 | `2026-04-04_14-55-51-0400-a-series-of-github.md`, `2026-04-04_18-55-51Z-a-series-of-github.md` |
| 33 | 2026-04-29 19:53:16-0400 | Claude Code | 318934-319918 | `2026-04-29_19-51-44-0400-conversation-exported-to-users.md` |
| 9 | 2026-04-03 20:13:41-0400 | Claude Code | 91163-95381 | `2026-04-03_20-10-07-0400-providing-a-linear-brainstorm.md`, `2026-04-04_00-10-07Z-providing-a-linear-brainstorm.md` |
| 11 | 2026-04-04 15:58:56-0400 | Claude Code | 95998-111336 | `2026-04-04_15-57-10-0400-prompting-the-exit-interview.md`, `2026-04-04_19-57-10Z-prompting-the-exit-interview.md` |
| 34 | 2026-04-21 08:21:07-0400 | Claude Code | 319919-323112 | `2026-04-21_08-21-02-0400.md`, `2026-04-21_12-21-02Z.md` |
| 2 | 2026-03-31 19:32:39-0400 | Claude Code | 2246-12071 | `2026-03-31_19-29-07-0400-i-m-attempting-to.md`, `2026-03-31_23-29-07Z-i-m-attempting-to.md` |
| 101 | 2026-04-28 00:10:06-0400 | Gemini CLI | 704270-707534 | `2026-04-28_00-09-06-0400-verifying-what-s-actually.md`, `2026-04-28_04-09-06Z-verifying-what-s-actually.md` |
| 35 | 2026-04-30 02:56:06-0400 | Claude Code | 323113-323410 | `2026-04-30_02-55-49-0400-install-gitlens.md` |
| 36 | 2026-04-29 14:48:49-0400 | Claude Code | 323411-336335 | `2026-04-29_14-34-00-0400-opencode-run-cat-users.md` |
| 100 | 2026-04-07 11:22:56-0400 | Gemini CLI | 701262-704269 | `2026-04-06_19-54-23-0400-plugin-for-gemini-chat.md`, `2026-04-06_23-54-23Z-plugin-for-gemini-chat.md` |
| 1 | 2026-03-31 11:12:16-0400 | Claude Code | 3-2245 | `2026-03-31_11-12-00-0400-session-close-audit-final.md`, `2026-03-31_15-12-00Z-session-close-audit-final.md` |
| 37 | 2026-04-29 18:00:46-0400 | Claude Code | 336336-338878 | `2026-04-29_18-00-35-0400-pick-back-up-workspace.md` |
| 38 | 2026-04-29 14:59:39-0400 | Claude Code | 338879-345084 | `2026-04-29_14-59-39-0400.md` |
| 39 | 2026-04-29 23:04:29-0400 | Claude Code | 345085-356491 | `2026-04-29_23-01-49-0400.md` |
| 8 | 2026-04-03 19:59:52-0400 | Claude Code | 78510-91162 | `2026-04-03_19-58-44-0400-transcripts-from-a-previous.md`, `2026-04-03_23-58-44Z-transcripts-from-a-previous.md` |
| 91 | 2026-04-02 01:11:28-0400 | Gemini CLI | 668481-671179 | `2026-04-02_01-10-02-0400-who-requires-notice-ownership.md`, `2026-04-02_05-10-02Z-who-requires-notice-ownership.md` |
| 22 | 2026-04-21 09:52:49-0400 | Claude Code | 241596-251484 | `2026-04-21_09-52-49-0400.md`, `2026-04-21_13-52-49Z.md` |
| 21 | 2026-04-21 07:54:14-0400 | Claude Code | 241578-241595 | `2026-04-21_07-54-14-0400.md`, `2026-04-21_11-54-14Z.md` |

*(plus 77 more pairs not shown)*
