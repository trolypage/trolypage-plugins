---
name: troly-workspace
description: Operate TrolyPage workspace channels, AI agents, internal notifications, and TrolyPage support tickets. Use for operational health checks, alert handling, agent diagnostics, or platform support.
---

# TrolyPage Workspace

Use only the `trolypage` MCP server. Read [tool-catalog.md](references/tool-catalog.md) for workspace operations and Integration Hub configuration.

## Workflow

1. Use `list-channels` or `list-agents` for fleet overview, then a status tool for the selected item.
2. Read a notification before acknowledging or resolving it; acknowledgement and resolution are different effects.
3. Search existing support tickets before creating a duplicate, and inspect ticket state before replying.
4. Report exactly which operational state changed and verify with a read tool.
5. For HTTP or webhook integration, save a draft, open setup_url for credentials in the app, re-read its revision, then check and enable. Track external effects through event/action logs.

Do not expose credentials from channel diagnostics, resolve alerts without understanding the requested action, or claim a support ticket reply fixed the underlying issue.
