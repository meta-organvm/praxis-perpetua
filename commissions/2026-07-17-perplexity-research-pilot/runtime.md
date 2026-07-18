# Runtime decision contract

## First probes

1. Validate all four request records against
   `schemas/research-request.schema.json`.
2. Read `governance/research-backend-profiles.yaml`.
3. Evaluate `pro_research.health.machine`; defer subscription,
   authentication, and Research-mode reachability to the `ManualHandoff`.
4. Confirm variable spend ceiling is USD 0 and no API or Computer path is
   active.
5. Confirm preservation and external-transmission compatibility and the
   prohibition on private connected sources.
6. Resolve each owner repository and output path.
7. Run `uv run --with-requirements requirements-validation.txt python3
   scripts/validate-research-backend.py`.
8. Inspect existing owner receipts before launching anything.

## Explicit owner resolution

From the Praxis repository root, query the live aggregate state without
writing an artifact:

```bash
praxis_root="$(git rev-parse --show-toplevel)" &&
limen_root="${LIMEN_ROOT:-/Users/4jp/Workspace/limen}" &&
domus_root="${DOMUS_ROOT:-/Users/4jp/Workspace/domus-genoma}" &&
uv run --with-requirements requirements-validation.txt \
  python3 scripts/evaluate-research-pilot.py \
  --owner-root "organvm/praxis-perpetua=$praxis_root" \
  --owner-root "organvm/limen=$limen_root" \
  --owner-root "organvm/domus-genoma=$domus_root"
```

The evaluator rejects missing, relative, duplicate, or unavailable owner-root
mappings. It resolves every declared report and receipt path beneath its
explicit owner and emits no local absolute path.

## Request selection

Process requests in numeric order unless an earlier request already has an
accepted owner receipt. Never rerun an accepted request. If a request is
blocked, write its typed receipt and continue every other reversible request.

For each pending request:

1. Render a `ManualHandoff` for `pro_research`.
2. Conduct the attended run in the **Limen Research** Project or Space.
3. Complete attended execution within the 3,600-second profile timeout.
4. Export the Session answer as Markdown to the declared owner.
5. Normalize the export and produce a canonical
   `SourceVerifierAttestation`.
6. Inspect and bind the exact Markdown plus tracked derivatives in
   `OutputSanitizationAttestation`.
7. Write the owner report and sanitized receipt.

## Live predicates

- `continue`: at least one request lacks a terminal owner receipt and a healthy
  zero-variable-spend profile can advance it.
- `wait_relay`: an attended export is the only missing input.
- `switch`: another bounded session is required; emit a successor capsule
  using this README.
- `settled`: every request has an accepted or rejected terminal receipt and
  the executable aggregate predicate in `closeout.md` has been evaluated.
- `invalid`: schema, preservation, transmission, custody, or spend constraints
  are violated; stop the affected request and write `BlockedReceipt`.

## Provider facts

Treat all provider capability, export, credit, and pricing observations as
dated external state. Refresh official documentation before enabling any
dormant profile.
