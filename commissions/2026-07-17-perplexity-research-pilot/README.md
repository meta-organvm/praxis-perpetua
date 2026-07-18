# Perplexity Research Pilot

Tracked continuation capsule for `INQ-2026-014`.

Read in order:

1. [intent.md](intent.md) — objective, authority, and prohibitions.
2. [runtime.md](runtime.md) — live routing probes and request selection.
3. `requests/01-jetsam-tuning.yaml` through
   `requests/04-public-claim-due-diligence.yaml` — canonical requests.
4. [status.md](status.md) and `handoffs/` — four generated ManualHandoff
   outcomes, ready prompts, zero-spend `manual_pending` receipts, and the
   current resume boundary.
5. [closeout.md](closeout.md) — aggregate pass/fail predicate and custody.

Canonical contracts remain in:

- `schemas/research-request.schema.json`
- `schemas/source-verifier-attestation.schema.json`
- `schemas/output-sanitization-attestation.schema.json`
- `schemas/research-outcome.schema.json`
- `schemas/research-receipt.schema.json`
- `standards/SOP--research-backend-routing.md`
- `scripts/validate-research-backend.py`

From the root of any Praxis clone containing this merged capsule, start or
resume the Limen execution lane:

```bash
praxis_root="$(git rev-parse --show-toplevel)" &&
limen_root="${LIMEN_ROOT:-/Users/4jp/Workspace/limen}" &&
"$limen_root/scripts/start-worktree-session.sh" \
  --autonomous \
  --codex \
  --prompt-file \
  "$praxis_root/commissions/2026-07-17-perplexity-research-pilot/README.md" \
  limen \
  perplexity-research-backend-20260717
```

This capsule does not claim a pilot result. Live request, profile, receipt,
cost, and owner-repo predicates determine what happens next.
