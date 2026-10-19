---
name: troly-support
description: Operate TrolyPage customer support, subscribers, conversations, CRM notes, tags, lead stages, messaging, AI-assisted replies, Telegram notifications, and customer reports. Use for inbox, CRM, or subscriber requests.
---

# TrolyPage Support

Use only the `trolypage` MCP server. Read [tool-catalog.md](references/tool-catalog.md) to select the tools available for this workflow.

## Workflow

1. Find the subscriber with `search-subscribers`, then confirm with `get-subscriber` when identity matters.
2. Read `get-conversation` or `list-conversations` before replying or changing conversation state.
3. Use the narrowest write tool for the requested effect.
4. Report approval state exactly and re-read the subscriber or conversation after execution when useful.

Never invent subscriber IDs, bypass a channel messaging window, expose internal CRM notes to customers, or claim a queued write has completed. `force_override` is exceptional and must follow an explicit authorized request.
