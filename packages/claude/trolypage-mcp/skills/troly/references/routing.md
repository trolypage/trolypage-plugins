# TrolyPage routing

Use the smallest set of tools needed. Read `trolypage://mcp/guide` for connection behavior. The live workspace catalog controls availability; do not promise a fixed tool count.

| Domain | Focused skill | Tasks |
| --- | --- | --- |
| Support | troly-support | Customers, conversations, messages, CRM |
| Commerce | troly-commerce | Products, pending orders, payment status/QR, shipping, bookings |
| Analytics | troly-analytics | Metrics and comparisons; exports are queued writes |
| Social | troly-social | Connected accounts, drafts, publication, status |
| Marketing | troly-marketing | Strategies, campaigns, broadcasts, nurture, follow-up |
| Knowledge | troly-knowledge | Approved facts, knowledge trees, ingestion |
| Workspace / integrations | troly-workspace | Channels, notifications, support tickets, configured integrations |
| Agents / assets | troly-workspace | Agent setup/configuration and managed media; inspect available tools first |
| Automation | troly-automation | Templates, draft workflows, checks, simulations, publication and runs |

Resolve returned IDs before dependent writes. An unavailable tool is a plan, permission or platform-profile limitation; never imitate its effect through an unrelated tool. Draft, pending approval, executed, paid, published and delivered states must remain distinct.
