# Current source tool reference

Human-readable source descriptions have been translated into English. Tool identifiers and contracts are unchanged; live server wording may differ.

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `search-subscribers` | support | readOnlyHint=true | Search customers (subscribers) by name, phone, email, status or subscriber_id. Returns matching records. |
| `get-subscriber` | support | readOnlyHint=true | Detailed subscriber profile: information, tags, CRM notes, AI status and lead stage. |
| `get-conversation` | support | readOnlyHint=true | Retrieve a subscriber's conversation history, showing customer messages and AI replies in chronological order. |
| `list-conversations` | support | readOnlyHint=true | Recent conversations for a subscriber or the entire workspace. |
| `send-message` | support | destructiveHint=true, openWorldHint=true | Send a message through the subscriber's channel (Messenger, Zalo, Telegram, etc.). Respects the messaging window; force_override is required when blocked. |
| `forward-message` | support | destructiveHint=true, openWorldHint=true | Forward a conversation message to another recipient on channels that support forwarding. |
| `close-conversation` | support | destructiveHint=true, idempotentHint=true | Close a subscriber's conversation and mark it resolved. |
| `reopen-conversation` | support | destructiveHint=true | Reopen a closed subscriber conversation. |
| `archive-conversation` | support | destructiveHint=true | Archive a subscriber conversation, hiding it from the inbox. |
| `add-subscriber-tag` | support | destructiveHint=true, idempotentHint=true | Add one or more subscriber tags; may trigger configured automatic tag rules. |
| `remove-subscriber-tag` | support | destructiveHint=true | Remove a subscriber tag. |
| `add-customer-note` | support | destructiveHint=true | Add an internal, staff-only CRM note to a subscriber. |
| `set-lead-stage` | support | destructiveHint=true, idempotentHint=true | Set a subscriber's lead stage using the workspace's configured stages. |
| `send-telegram-notification` | support | openWorldHint=true, destructiveHint=true | Send a notification to the support team's Telegram group for new customers, technical requests or completed flows. |
| `update-subscriber-status` | support | destructiveHint=true, idempotentHint=true | Update subscriber status and enable/disable AI. Status: Active (AI support), Pause (awaiting technical support), Done (completed). |
| `chat-with-ai` | support | openWorldHint=true, destructiveHint=true | Send a message through an AI Agent and receive a reply. Uses the real runtime, consumes AI quota, records the conversation and may execute business tools. Not a sandbox or proof of channel delivery. Uses the selected agent's system prompt and knowledge base. |
| `create-customer-report` | support | openWorldHint=true, destructiveHint=true | Create a new customer report and send it to Telegram after collecting the customer's name, phone number and needs. |
| `support-lookups` | support | readOnlyHint=true | Discover workspace tag and lead-stage IDs before tagging customers or changing their stage. Returns full paginated lookup records. |
