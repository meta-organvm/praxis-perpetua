#!/usr/bin/env bash
set -euo pipefail

commission_dir="$(
  cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
  pwd -P
)"
limen_root="${LIMEN_ROOT:-}"

if [[ -z "$limen_root" || ! -x "$limen_root/scripts/start-worktree-session.sh" ]]; then
  echo "LIMEN_ROOT must name a Limen checkout with scripts/start-worktree-session.sh" >&2
  exit 64
fi

relay_label="${LIMEN_RELAY_LABEL:-perplexity-research-pilot-relay-$(date -u +%Y%m%dT%H%M%SZ)}"

exec "$limen_root/scripts/start-worktree-session.sh" \
  --autonomous \
  --codex \
  --from origin/main \
  --prompt-file "$commission_dir/README.md" \
  limen \
  "$relay_label"
