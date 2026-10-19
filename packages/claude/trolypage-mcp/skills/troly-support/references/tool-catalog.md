# Directory profile tool reference

Source snapshot: 2026-10-19. The server enforces this catalog at discovery and execution. Workspace permissions and plan may further restrict it. A listed capability is not proof of successful end-to-end testing. Annotation details are authoritative in the live MCP response.

| Tool | Module | Description |
| --- | --- | --- |
| `search-subscribers` | support | Search customers (subscribers) by name, phone, email, status or subscriber_id. Returns matching records. |
| `get-subscriber` | support | Detailed subscriber profile: information, tags, CRM notes, AI status and lead stage. |
| `get-conversation` | support | Retrieve a subscriber's conversation history, showing customer messages and AI replies in chronological order. |
| `list-conversations` | support | Recent conversations for a subscriber or the entire workspace. |
| `send-message` | support | Send a message through the subscriber's channel (Messenger, Zalo, Telegram, etc.). Respects the messaging window; force_override is required when blocked. |
| `forward-message` | support | Forward a conversation message to another recipient on channels that support forwarding. |
| `close-conversation` | support | Close a subscriber's conversation and mark it resolved. |
| `reopen-conversation` | support | Reopen a closed subscriber conversation. |
| `archive-conversation` | support | Archive a subscriber conversation, hiding it from the inbox. |
| `add-subscriber-tag` | support | Add one or more subscriber tags; may trigger configured automatic tag rules. |
| `remove-subscriber-tag` | support | Remove a subscriber tag. |
| `add-customer-note` | support | Add an internal, staff-only CRM note to a subscriber. |
| `set-lead-stage` | support | Set a subscriber's lead stage using the workspace's configured stages. |
| `update-subscriber-status` | support | Update subscriber status and enable/disable AI. Status: Active (AI support), Pause (awaiting technical support), Done (completed). |
| `create-customer-report` | support | Create a new customer report and send it to Telegram after collecting the customer's name, phone number and needs. |
| `support-lookups` | support | Returns paginated workspace tags and lead-stage records with their identifiers. |
