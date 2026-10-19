---
name: troly
description: Route and execute end-to-end work across the TrolyPage business directory catalog, or present the complete TrolyPage usage guide. Use when a request mentions TrolyPage, spans domains, is ambiguous about which tool to call, explicitly invokes $troly, or asks for help, getting started, usage, a menu, commands, or what TrolyPage can do, in any language.
---

# TrolyPage Router

Use the `trolypage` MCP server for all operations. It is one authenticated connection whose visible capabilities already reflect the workspace plan.

## Help mode

Before routing an operation, detect whether the text after the invocation is empty or primarily asks for help. Recognize help intent in any language, including requests for help, getting started, usage instructions, a menu, commands, available capabilities, or how to perform a task.

For general help, read [help.md](references/help.md) and render its complete guide in the user's language. Do not call a business tool. For scoped help such as `help commerce` or `help with social posting`, show the invocation syntax, the matching domain, safe workflow, available operations, and several copy-ready examples; read the focused skill's tool catalog when necessary.

Do not claim that `/troly` is universally registered. Explain the actual invocation supported by the current client: `$troly` in Codex, `@troly` on ChatGPT skill surfaces, and `/troly` only in hosts that provide a custom slash-command alias.

## Route the task

For non-help requests, read [routing.md](references/routing.md) and choose the smallest set of domains needed. For a cross-domain request, complete prerequisites before dependent writes; for example, resolve a subscriber and product before creating an order, then create shipping only after the order is confirmed.

## Operating contract

1. Consult the packaged help and https://trolypage.com/mcp for connection and approval behavior; this profile does not expose MCP resources or prompts.
2. Resolve real IDs with list, search, or get tools. Never invent an ID, status, price, inventory count, payment state, or delivery quote.
3. Summarize the intended target and effect before a high-impact write when the user's instruction did not already make them explicit.
4. Call the matching tool. If it returns an approval request, report its ID and state; do not retry the write or claim it already executed.
5. Re-read affected state when a verification tool exists.

Treat HTTP 402 as a plan/module limitation, 403 as a permission or workspace-boundary failure, 422 as invalid business input, and 429 as a signal to honor `Retry-After`. Never work around an unavailable module with an unrelated tool.

## Focused skills

Use these focused skills when the request stays in one domain: `$troly-support`, `$troly-commerce`, `$troly-analytics`, `$troly-social`, `$troly-marketing`, `$troly-knowledge`, `$troly-workspace`.
