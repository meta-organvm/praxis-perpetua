# Plan: Fix Claude Code CLI Hang on Startup

## Problem Analysis
The Claude Code CLI is failing to launch and "sits in the terminal" (hangs). 
Investigation of the debug logs (`~/.claude/debug/latest`) reveals a persistent error:
`[ERROR] Marketplace configuration file is corrupted: anthropic-agent-skills.source.source: Invalid input`.

The file `~/.claude/plugins/known_marketplaces.json` contains a local marketplace entry (`anthropic-agent-skills`) with `"source": "local"`. This value appears to be failing validation in the current version of Claude Code (2.1.44), preventing the plugin system from initializing correctly and stalling the startup process.

## Proposed Solution
We will remove the corrupted marketplace entry from `known_marketplaces.json` to allow the CLI to complete its initialization.

### Step 1: Backup Configuration
Before making any changes, we will back up the `known_marketplaces.json` file.

### Step 2: Fix Marketplace Configuration
We will edit `~/.claude/plugins/known_marketplaces.json` to remove the problematic `anthropic-agent-skills` entry.

### Step 3: Verify Fix
The user should then attempt to launch `claude` again.

## Implementation Details (Post-Approval)
Once I exit Plan Mode, I will use `run_shell_command` to perform the following:
1. `cp ~/.claude/plugins/known_marketplaces.json ~/.claude/plugins/known_marketplaces.json.bak`
2. Use a tool to remove the invalid JSON entry. (I will use `replace` or `write_file` depending on the state).

## Risks
- The local skills provided by `anthropic-agent-skills` will be temporarily unavailable until re-added with correct syntax.
- If other files are also corrupted, additional troubleshooting may be needed.
