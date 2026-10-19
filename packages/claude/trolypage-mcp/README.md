# TrolyPage MCP

![TrolyPage](assets/icon.png)

TrolyPage is AI customer support, CRM, social media scheduling and order management software for small businesses. It brings customer conversations, products, orders, scheduled content and follow-up work into one business workspace.

This integration connects your AI assistant to an existing TrolyPage workspace. Find customers and summarize conversations, update internal CRM notes, check product prices and stock, prepare orders for shop review, and compare sales reports. You can also manage social post drafts, marketing campaigns, approved knowledge, connected channels and existing or user-supplied assets when those modules are available to your account.

Sign in with OAuth and select the workspace you administer. Access requires an owner or administrator role and a plan with the requested MCP modules. Some text AI operations consume additional quota. Channel features, delivery services and payment methods vary by account, provider and region.

TrolyPage supplies the authoritative price, stock, total and payment status. Drafts, pending approvals, completed actions and delivery to an external service are distinct. Authorized writes can change records, send messages, publish posts or request services. Customers complete merchant payments outside the AI assistant; a payment QR or pending request does not prove that money was received.

[Explore product features](https://trolypage.com/features) Â· [MCP setup and troubleshooting](https://trolypage.com/mcp)

## Connection

The remote server is `https://trolypage.com/mcp/claude` and uses Streamable HTTP with OAuth authorization-code flow, PKCE S256 and scope `mcp:use`. Complete sign-in on TrolyPage and choose the workspace you administer. Never paste service credentials into a prompt. Read [MCP documentation](https://trolypage.com/mcp) and [troubleshooting](https://trolypage.com/mcp#errors).

## Examples

- Find Review Customer A and summarize their latest conversation, read only.
- Find product TLP-REVIEW-MUG and show its current price and stock.
- Prepare an order for shop review without confirming, charging or shipping it.
- Show sales for the last 30 days and compare with the previous period.
- Add an internal CRM note without messaging the customer.

These review examples require sample records in a dedicated test workspace. Production usage resolves the customer's own records; never invent fixture IDs.

## Data and execution

The package contains instruction files and a remote MCP connection. It has no local executable, install hook or bundled backend. Requested tool arguments go to TrolyPage; results return to the AI host. Authorized actions may involve customer/contact information, conversations, products, orders, reports, social content, approved knowledge, files or connected delivery providers. Third-party delivery and payment occur only in the applicable connected service. The installed server catalog is permission- and plan-dependent.

Respect the host's confirmations and workspace policy. A queued action is not a completed operation. Re-read affected state; do not duplicate a write after receiving an approval action. Disconnect through host connector settings and revoke the TrolyPage grant when access is no longer wanted.

## Support and terms

- [Website and MCP documentation](https://trolypage.com/mcp)
- [Support and troubleshooting](https://trolypage.com/mcp#errors); support@trolypage.com
- [Privacy policy](https://trolypage.com/privacy-policy)
- [Terms of service](https://trolypage.com/terms-of-service)
- [Data deletion](https://trolypage.com/data-deletion)

Public package candidate 1.0.2. Publication is subject to platform review and supported catalog configuration.

## Claude directory profile

Version 1.0.2 uses the dedicated `/mcp/claude` catalog with eight skills. The server enforces a 180-tool allowlist before workspace entitlement filtering; hidden tools cannot be called directly. It excludes AI image/video/audio generation, agent runtimes/configuration, Automation Hub and arbitrary Integration Hub operations. Text caption, hashtag and business-draft generation remain available. This profile exposes no MCP prompts or resources.

The full `/mcp/troly` endpoint remains available separately with Gen AI capabilities. This package does not silently switch to it when a directory tool is unavailable.

Backend regression validation passed 248 tests, with a further seven catalog and authorization tests after the final prose-copy fix. These checks do not replace authenticated business tests of every exposed tool or guarantee directory approval. The existing bundle submission is awaiting Anthropic review; this revision must be scanned by that submission before publication.

## License

Original plugin skills and documentation are licensed under [Apache-2.0](LICENSE). See NOTICE. The separately hosted application backend is outside this distribution.
