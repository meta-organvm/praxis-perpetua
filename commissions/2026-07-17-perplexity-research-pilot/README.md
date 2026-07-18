# Perplexity Research Pilot

Tracked continuation capsule for `INQ-2026-014`.

Read in order:

1. [intent.md](intent.md) — objective, authority, and prohibitions.
2. [runtime.md](runtime.md) — live routing probes and request selection.
3. `requests/01-jetsam-tuning.yaml` through
   `requests/04-public-claim-due-diligence.yaml` — canonical requests.
4. [status.md](status.md), `handoffs/`, and
   [execution-catalog-receipt.json](execution-catalog-receipt.json) — the
   terminal fail state plus the exact enabled catalog provenance for the
   preliminary handoffs.
5. [closeout.md](closeout.md) — aggregate pass/fail predicate and custody.
6. [RELAY.md](RELAY.md) — concise current relay and durable owner receipt.

Canonical contracts remain in:

- `schemas/research-request.schema.json`
- `schemas/source-verifier-attestation.schema.json`
- `schemas/output-sanitization-attestation.schema.json`
- `schemas/research-outcome.schema.json`
- `schemas/research-receipt.schema.json`
- `standards/SOP--research-backend-routing.md`
- `scripts/validate-research-backend.py`
- `scripts/evaluate-research-pilot.py`

From any working directory, start or resume the Limen execution lane after
setting `LIMEN_ROOT` to the intended Limen checkout:

```bash
commissions/2026-07-17-perplexity-research-pilot/launch-relay.sh
```

The commission-local launcher resolves this `README.md` from its own location,
uses refreshed `origin/main`, and never derives the Praxis prompt from the
caller's working directory. The current commission is terminal; use the
launcher only for a new authorized run. The evaluator never guesses owner
locations. Resolve Praxis from the current clone and provide absolute Limen and
Domus roots as shown in [runtime.md](runtime.md).

The live predicates settle this pilot `fail`: no attended browser session was
controllable, all four runs were rejected before submission, and variable
spend remained USD 0.
