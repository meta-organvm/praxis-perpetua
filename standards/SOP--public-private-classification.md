# SOP: Public/Private Classification

**Version:** 1.0.0 | **Date:** April 29, 2026 | **Status:** Active
**Scope:** Durable taxonomy and procedure for sorting artifacts into preservation tiers (essence-private, client-private, operational-internal, public-facing). Applied at every artifact-creation boundary, especially during session close-outs, untracked-file triage, and cross-client work hygiene.

---

## 1. Ontological Purpose

Artifact classification is a **preservation concern** disguised as a storage concern. The ORGANVM system produces three kinds of value that must not be confused:

- **Essence-IP** (the orchestration patterns, novel methodologies, internal scoring frameworks that make this system's output uniquely valuable) — if exposed, others can replicate the user's distinguishing capability.
- **Client confidentiality** (financial agreements, PII, single-engagement strategy) — co-owned artifacts where exposure breaks contract and trust.
- **Operational continuity** (session logs, drafts, planning artifacts) — must persist for next-session handoff but contain no IP value.

A naive "commit everything to GitHub" violates the first two. A naive "gitignore everything sensitive" violates the local:remote 1:1 axiom (artifacts at risk of disk failure with no remote backup). This SOP defines **a per-artifact classification + a per-tier durable destination** so that every file gets remote parity in a venue appropriate to its preservation tier.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster: Governance & Lifecycle)

The core risk: **untracked files that should be private get committed publicly, and untracked files that should be remote stay local-only and are lost.** Both failures are common in practice. This SOP makes the disposition decision explicit at the point of artifact creation rather than after damage is done.

---

## 2. Taxonomy (Four Tiers)

| Tier | Symbol | Definition | Example artifacts |
|------|--------|------------|-------------------|
| **Essence-private** | `E` | Unique IP that, if exposed, would let others replicate the user's distinguishing value. Cross-client patterns, novel methodologies, internal scoring frameworks. | Cross-client orchestration showcases, ORGANVM 8-organ system internals, magnetism-formula derivations, internal IRA panel rubrics |
| **Client-private** | `C` | Per-client confidential — financial agreements, PII, single-engagement strategy that the client owns or co-owns. | Revenue agreements, named case studies, per-client strategy documents, client communication archives |
| **Operational-internal** | `O` | Internal-but-not-load-bearing — session logs, drafts, WIP, planning artifacts that have no IP value but should persist for continuity. | `.claude/plans/`, `.conductor/active-handoff.md`, session export transcripts, fossil records, untracked drafts |
| **Public-facing** | `P` | Open, shareable — essays, code, finished deliverables ready for distribution. | Repo source code, published essays, public READMEs, completed pitch decks intended for distribution |

---

## 3. Decision Tree

Apply to any untracked file or any new artifact about to be created:

1. **Does this contain unique cross-client methodology, novel synthesis, or IP that defines the user's distinguishing value?** → `E`
2. **Does this contain client financial terms, client PII, or strategy specific to a single engagement?** → `C`
3. **Is this a draft, planning artifact, session log, or WIP that has no IP value but should persist?** → `O`
4. **Otherwise** → `P`

When uncertain between two tiers, prefer the more restrictive tier (E > C > O > P). It is easier to declassify later (move from E to P) than to remediate exposure (move from P to E after the file has been published).

---

## 4. Storage Rules (Per Tier)

| Tier | Destination | Rationale |
|------|-------------|-----------|
| `E` | Single private repo: `4jp/essence-vault` | Centralization protects against per-client repo sprawl; one access boundary to defend; cross-client methodology lives where it is naturally referenced from any engagement |
| `C` | Per-client private repo: `<client-engagement>--client-private` (e.g., `sovereign-systems--client-private`, future `hokage-chess--client-private`) | Per-client scope prevents accidental cross-client exposure; aligns with potential future client access (a client may be granted read access to *their* private repo without seeing other clients) |
| `O` (safe) | Same repo as the public artifact it relates to, IF it contains no PII / IP / secrets | Co-location preserves discoverability; planning artifacts naturally live with the code they plan |
| `O` (sensitive) | Gitignored locally + chezmoi-mirrored to `~/.local/share/<scope>/operational/` | When public-tracking is unsafe but the artifact must persist, chezmoi handles parity via the private dotfiles repo |
| `P` | Same repo (public) | Default; explicit |

### Determining `O` safety

Treat an `O` artifact as **safe** for public tracking if and only if all of the following hold:

- No client name appears (Maddie, Rob, Scott, etc.) — except in already-public contexts
- No financial figures, contract terms, or compensation discussion
- No PII (email, phone, address, billing info) for any third party
- No credentials, tokens, or secrets (even truncated)
- No unflattering characterization of any third party

Otherwise treat as **sensitive** and use the gitignored + chezmoi-mirrored path.

---

## 5. Discovery Mechanism

### 5.1 Manual procedure (current)

At any session close-out and after any significant work:

1. Run `git status --porcelain` in each repo touched.
2. For each untracked file, walk the decision tree from §3.
3. Apply the storage rule from §4. Either:
   - Move the file to its appropriate destination (private repo, chezmoi store, archive subdirectory), OR
   - Track in the current repo if `P` or `O`-safe, OR
   - Add the path/pattern to `.gitignore` if `O`-sensitive (then arrange chezmoi-mirroring).
4. If the file's tier is non-obvious, add a header comment to the file: `<!-- classification: E -->` (or `C` / `O` / `P`). This makes the disposition durable and auditable.

### 5.2 Automation (future enhancement)

A `classify-untracked.sh` script that:

- Runs the discovery on all repos in scope
- Applies rule-based classification heuristics (filename patterns, content scans)
- Prompts the user on ambiguous cases
- Emits a report of classified vs unclassified artifacts

A pre-commit hook that **refuses commits of any new file lacking a classification tag** in the front matter or filepath convention. This forces the decision at commit time rather than session-close time.

---

## 6. Operational Patterns

### 6.1 Session close-out propagation

At session close, classification is part of the close-out checklist:

1. List all untracked files (the discovery from §5.1).
2. Classify each per §3.
3. Apply the storage rule per §4.
4. Verify final state: `git status --porcelain` empty in the public repo (modulo gitignored ephemera).

### 6.2 Cross-client artifact handling

When working across multiple clients in one session, **never let cross-client artifacts land in any per-client repo** — they are `E`-tier by definition (the cross-client pattern is the IP). Examples: orchestration showcases that demonstrate "how I worked with both Maddie AND Rob simultaneously" go to `essence-vault`, not to either client's private repo.

### 6.3 Sanitization path

If a `C`-tier artifact has value to publish in some form (e.g., a case study could become marketing material), the sanitization path is:

1. Original lives in client-private repo with full fidelity (financial figures, PII, etc.)
2. Sanitized version lives in public repo with figures generalized, names redacted or anonymized to consenting role labels (e.g., "the founder", "the operator")
3. Both versions cross-reference each other in commit messages
4. Client consent documented in client-private repo before publishing

### 6.4 Tier reclassification

Tiers are not permanent. As work matures:

- `E` → `P`: the user may choose to publish a methodology (move from essence-vault to a public docs site)
- `C` → `P`: with client consent, a sanitized case study can become public marketing
- `O` → `P`: a draft becomes a finished essay
- `P` → `C` (rare): a publicly-discussed approach becomes proprietary as it matures

When reclassifying, document the reason in the moving commit. Never silently reclassify.

---

## 7. Repository Inventory (as of 2026-04-29)

| Repo | Visibility | Tier scope |
|------|------------|------------|
| `4jp/essence-vault` | Private | `E` only |
| `4jp/sovereign-systems--client-private` | Private | `C` for Maddie/sovereign-systems engagement |
| `<future>/hokage-chess--client-private` | Private | `C` for Rob/hokage-chess engagement (when needed) |
| `4jp/sovereign-systems--elevate-align` | Public | `O`-safe + `P` |
| `4jp/hokage-chess` | Public | `O`-safe + `P` |
| `4444J99/portfolio` | Public | `P` |
| `4444J99/domus-semper-palingenesis` | Public | `O`-safe + `P` (chezmoi dotfiles) |

This inventory grows as new client engagements begin. Each new client requires deciding: does this engagement need its own per-client private repo, or does it share with an existing one?

---

## 8. Anti-Patterns (Things This SOP Prevents)

- **"It's just a draft, I'll commit it later"** — drafts are `O`; track them in the same commit as the related work, or chezmoi-mirror immediately. Local-only drafts are at risk of disk loss.
- **"Just gitignore the sensitive doc"** — gitignoring without a parity destination violates the local:remote 1:1 axiom. Use the chezmoi store.
- **"This case study would be great marketing — I'll just commit it"** — `C`-tier content needs client consent and sanitization before becoming `P`. Commit to client-private first.
- **"The cross-client showcase belongs in Maddie's repo since it features her work"** — false. Cross-client content is `E`-tier; per-client repos must remain scope-clean.
- **"I'll classify these later"** — later doesn't come. Classify at the session-close gate, every time.

---

## 9. Reconciliation with Existing Artifacts

For artifacts already committed to the wrong tier:

- `E` content in a public repo → migrate to `essence-vault`, then `git rm` from public + commit. **This does NOT remove the file from git history.** Accept the history as a permanent record; the SOP's value is preventing future occurrences.
- `C` content in a public repo → same migration pattern + same caveat. Consider `git filter-repo` only with explicit user authorization and an understanding of the disruption to forks/clones.
- `P` content in a private repo → opportunity to publish. Document the decision and the reclassification path used.

---

## 10. Cross-References

- **First instance application:** Close-out session 2026-04-29 (`goal-dapper-wall` plan) applies this SOP to 3 sensitive untracked docs in `sovereign-systems--elevate-align` as the inaugural usage.
- **Related SOPs:** `SOP--cross-agent-handoff.md` (Cluster 3: Governance & Lifecycle) — applies during external-agent ingestion which often produces unclassified artifacts.
- **Plan persistence:** `/Users/4jp/.claude/plans/goal-dapper-wall.md` (Construct A documents the original design rationale).
- **Future enhancements tracked separately:** `classify-untracked.sh` automation, pre-commit hook enforcement.
