# Closeout

## Per-run predicate

A run is accepted only when:

- every material claim has a resolvable supporting citation;
- all cited sources retain retrieval dates and source metadata;
- the report and receipt exist in the declared owner repository;
- the request, SourceVerifierAttestation, OutputSanitizationAttestation,
  outcome, and receipt pass `uv run --with-requirements
  requirements-validation.txt python3 scripts/validate-research-backend.py`;
- at least one novel actionable finding is recorded;
- operator handling is no more than 20 minutes;
- variable Perplexity spend is USD 0.

Reject a run with broken citations, unsupported material claims, missing
retrieval dates, lost source metadata, incompatible preservation or
transmission, invalid custody, or excess handling/spend.

## Aggregate predicate

The pilot passes only when:

- at least three of four packets are accepted;
- 100 percent of material claims in accepted packets have resolvable
  citations;
- at least 80 percent of all accepted-packet citations are primary sources;
- all four runs have durable owner-repo reports and receipts;
- each accepted packet contains at least one novel actionable finding;
- every run stays within the 20-minute operator-handling ceiling;
- total variable Perplexity spend is USD 0.

Resolve all three owner repositories explicitly and write the deterministic
terminal evaluation only when all inputs exist:

```bash
praxis_root="$(git rev-parse --show-toplevel)" &&
limen_root="${LIMEN_ROOT:-/Users/4jp/Workspace/limen}" &&
domus_root="${DOMUS_ROOT:-/Users/4jp/Workspace/domus-genoma}" &&
uv run --with-requirements requirements-validation.txt \
  python3 scripts/evaluate-research-pilot.py \
  --owner-root "organvm/praxis-perpetua=$praxis_root" \
  --owner-root "organvm/limen=$limen_root" \
  --owner-root "organvm/domus-genoma=$domus_root" \
  --output \
  commissions/2026-07-17-perplexity-research-pilot/aggregate-evaluation.json \
  --require-settled
```

Exit `3` means the truthful state remains `wait_relay`; exit `2` means an
owner input is invalid. A settled pass or fail exits `0` because both are
terminal classifications. `--require-pass` is available only when a caller
specifically requires the pass effect.

Preliminary and terminal run receipts bind the execution-time catalog through
`execution-catalog-receipt.json`. The aggregate's `catalog_hash` separately
binds the current registry after terminal effects are applied. Never rewrite a
historical handoff receipt to impersonate the later disabled registry.

## Terminal effects

- **Pass:** keep `pro_research` enabled. API activation remains a separate
  future decision requiring credentials, credits, refreshed pricing, and an
  accepted spend case.
- **Fail:** disable `pro_research` and forbid API spending until a new value
  case is accepted.

After the command exits `0`, update `status.md` to `settled`, set
`aggregate_evaluation_ref` to the tracked aggregate path, and copy its verdict
and observed variable spend into the status fields and visible summary. The
owner validator rejects any divergence. Run it twice; the second run must make
no changes. Link every owner receipt and owner-route any residual before
terminal classification.
