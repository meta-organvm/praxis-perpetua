# RELAY — Perplexity research pilot

- **State:** `wait_relay`
- **Owner receipt:** `organvm/praxis-perpetua#50` is merged with green checks.
- **Durable inputs:** four canonical requests and four zero-spend
  `ManualHandoff` packets are tracked in this capsule.
- **Human gate:** conduct each attended `pro_research` handoff and export its
  Markdown result to the declared private owner.
- **Executable truth:** run the owner-resolved command in
  [runtime.md](runtime.md); it remains `wait_relay` until all declared terminal
  report/receipt pairs exist.

Launch the bounded relay lane:

```bash
praxis_root="$(git rev-parse --show-toplevel)" && limen_root="${LIMEN_ROOT:-/Users/4jp/Workspace/limen}" && "$limen_root/scripts/start-worktree-session.sh" --autonomous --codex --prompt-file "$praxis_root/commissions/2026-07-17-perplexity-research-pilot/README.md" limen perplexity-research-pilot-relay-20260718
```

No pilot verdict, API activation, variable spend, or unattended outward action
is authorized by this relay.
