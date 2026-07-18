# RELAY — Perplexity research pilot

- **State:** `settled/fail`
- **Prior owner receipt:** `organvm/praxis-perpetua#50` is merged with green
  checks.
- **Terminal inputs:** four canonical requests and four zero-spend rejected
  owner receipts.
- **Executable truth:** [aggregate-evaluation.json](aggregate-evaluation.json)
  records 0 accepted packets, 4 durable owner outputs, and USD 0 variable
  spend.
- **Effect:** `pro_research` is disabled; APIs and Computer remain unavailable
  to this commission.

The commission-local launcher is retained as the portable successor mechanism.
It must only be used for a new authorized run:

```bash
commissions/2026-07-17-perplexity-research-pilot/launch-relay.sh
```

No API activation, variable spend, or unattended outward action is authorized
by this terminal relay.
