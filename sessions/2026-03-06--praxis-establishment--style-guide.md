# Style Guide: Reading & Writing Session Transcripts

**Companion to:** `2026-03-06--praxis-establishment--transcript-unabridged.md`
**Purpose:** Conventions for producing and auditing unabridged AI-conductor session transcripts

---

## Document Hierarchy

Every exported session produces up to three sibling files:

| File suffix | Purpose | Audience |
|-------------|---------|----------|
| `--transcript.md` | Conversation summary (text only, tool calls named) | Quick review, standup |
| `--transcript-unabridged.md` | Full audit trail (thinking, tool I/O, generated code) | Deep review, post-mortem |
| `--style-guide.md` | Reading conventions for the unabridged transcript | First-time auditors |

The structured review template (no suffix beyond the slug) is the actionable deliverable — the transcripts are its evidence base.

---

## Entry Anatomy

Every entry follows:

```
## [N] Role — HH:MM:SS
```

**Roles:**
- **Human** — User prompts. System reminders are stripped.
- **Assistant** — Agent responses. May contain multiple subsections.
- **System** — Environment context injected by the platform.

### Assistant Entry Subsections

Appear in execution order within a single turn:

#### `### Thinking`

Internal reasoning before the agent acts or speaks. Fenced in a code block.

**Audit value:** This is where decisions are made. When reviewing a bug or questionable choice, start here. The thinking block that preceded the action reveals whether the agent considered alternatives, identified risks, or missed something.

**Red flags to watch for:**
- Thinking that contradicts the subsequent action
- Absence of thinking before a complex decision
- Thinking that acknowledges a risk but takes no mitigating action

#### Free text (no header)

The agent's visible response to the user. This is what appeared in the terminal.

#### `### Tool: <ToolName>`

A tool invocation with its full input. Structure varies by tool:

| Tool | Key fields shown | What to audit |
|------|-----------------|---------------|
| **Read** | File path, offset, limit | Was the right file read before editing? |
| **Write** | File path, full content | Is the generated code correct and complete? |
| **Edit** | File path, old_string, new_string | Is the diff minimal and correct? |
| **Bash** | Command, description | Could this command cause damage? |
| **Glob** | Pattern, path | Was the search scope appropriate? |
| **Grep** | Pattern, path, mode | Was the search precise enough? |

**Tool results** appear in the next **Human** entry as `**Tool Result**` blocks (the platform returns tool output as user-role messages).

---

## Audit Playbook

### Tracing a generated file

To verify what was written to a file:

1. Search for `### Tool: Write` with the file path
2. The `**Content**` block is the exact bytes written
3. If the file was later edited, search for `### Tool: Edit` with the same path
4. Cross-reference with the commit SHA in the header to see the final committed state

### Tracing a decision

To understand why a choice was made:

1. Find the assistant entry where the choice appears in free text
2. Read the `### Thinking` block in that same entry (if present)
3. Read the preceding Human entry for the prompt that triggered it
4. Read tool results in the entries before the thinking block — that's what the agent was looking at

### Tracing a bug caught in review

To understand how a bug was introduced and caught:

1. Find the entry where the bug was introduced (usually a Write or Edit)
2. Check the Thinking block — did the agent consider this case?
3. Find the entry where the bug was caught (usually after a Human challenge)
4. Read the Thinking block that identified the root cause
5. Find the fix (the subsequent Edit or Write)

### Verifying completeness

An unabridged transcript should satisfy:

- [ ] Every Write/Edit has a preceding Read of the same file (or a newly created file)
- [ ] Every Bash command has a description field
- [ ] Every decision-bearing free text block has a preceding Thinking block
- [ ] Commit SHAs are referenced in the document header
- [ ] No `[REDACTED]` or `[TRUNCATED]` markers (if present, the transcript is not truly unabridged)

---

## Writing Conventions for Future Exports

When producing transcripts (manually or via tooling):

1. **Never strip thinking blocks.** They are the reasoning chain. Without them, the transcript is a conversation log, not an audit trail.
2. **Never summarize tool inputs.** `**Write** \`file.js\`` is useless to an auditor. The content is the artifact.
3. **Always include commit SHAs** in the document header. Tool results are recoverable from git; the SHAs are the bridge.
4. **Strip system reminders** from Human entries — they're platform noise, not user intent.
5. **Preserve entry ordering.** The sequence is causal. Reordering destroys the reasoning chain.
6. **Fence all code and tool output.** Unescaped code in markdown breaks rendering and makes the document unsearchable.
7. **Cap tool result output at 8,000 chars** per block. Beyond that, reference the file path and commit SHA instead. This is the one acceptable truncation — mark it with `[TRUNCATED — see <path> at <sha>]`.

---

## Relationship to Other SOPs

- **`sop--cicd-resilience.md`** Phase 5 (Post-mortem audit) should reference these transcripts as evidence
- **`GOVERNANCE-COUPLING.md`** coupling entries are derived from transcript analysis of failure chains
- **Structured review template** TODO sections should cite entry numbers from the unabridged transcript (e.g., "see entry [42] for the root cause analysis")
