# Reviewer access, tests and demo video

## Current status

The owner supplied reviewer credentials privately. Browser access was verified on October 19, 2026: workspace **TrolyPage Reviewer**, **Scale** plan, current member **Owner**. The owner completed Cloudflare verification during this sign-in; independent access by an external reviewer has not been established. No username or password is stored in the repository or archives.

The authenticated MCP page lists 11 included servers, 270 tools and 117 read tools. It shows no API keys, authorized OAuth applications or successful read-only tool call. The applied write mode is **Full / Direct execution**; it was observed without changing configuration. Browser access is not proof of successful OAuth or MCP tool calls.

The workspace has no products or orders and only the default support contact. `Review Customer A`, SKU `TLP-REVIEW-MUG` and comparison-period demo orders are absent. Business tests have not run; no real video or demo URL exists. `test-cases.json` is a specification and all results in `test-results.csv` remain Not run. Do not use the real support contact as a fixture or message it to create test data.

## Populate the dedicated workspace

1. Verify the workspace is isolated and the owner/admin account and plan cover the declared modules. Record the workspace name, login URL and actual timezone in fixture-map.json. Keep credentials out.
2. Create `Review Customer A` with a short synthetic conversation. Do not use real customer phone numbers or email addresses.
3. Create active product `Review Mug`, SKU `TLP-REVIEW-MUG`, proposed price 100000 VND and stock 20. Record actual server-assigned IDs. Prepare synthetic orders for both report comparison periods.
4. Record approval mode for every run. Check for fulfillment, notifications and workflows before creating test orders or notes. Do not connect a live bank or carrier for the core tests.
5. For social tests, use an owner-controlled test account. Save an unscheduled draft; do not publish. Provider-dependent tools require their own sandbox or fixture instructions.
6. Limit reviewer permissions to the demo workspace. Verify sign-in without relying on the owner's phone, mailbox or approval. Supply credentials only through each portal's secure review fields, never public Git, listing text or archives.

## Representative cases

`test-cases.json` contains five positive and three negative cases with setup, prompts, tools and pass conditions. Adapt the same scenarios to the actual Claude/Muse catalog. Positive cases cover customer context, product lookup, a pending shop-review order, sales comparison and an internal CRM note. Negative cases cover bank transfers, unauthorized workspace access and secret extraction.

Run writes under ordinary execution and under MCP approval. Only the demo operator approves queued actions. Record the host, package hash, timestamp, sanitized arguments, actual IDs/states and evidence in test-results.csv. Compare results with expected behavior before assigning Passed, Failed or Blocked.

## Additional coverage for the full catalog

| Module | Required coverage |
| --- | --- |
| Social | Resolve an account, save a draft and verify it remains unpublished. Schedule/publish only with a test provider and actual approvals |
| Marketing | Create a broadcast draft and preview the audience. pending_review does not mean sent |
| Knowledge | Search approved facts, import a sample document and verify ingestion. Proposed facts remain unapproved |
| Agents | Read setup, create an inactive draft and run preflight. A runtime check is not proof of external delivery |
| Assets | Transfer actual fixture bytes, poll verification and inspect the resulting asset. Do not provide a local path the server cannot read |
| Automation | Save a draft, validate, simulate and inspect returned states. Publication may start real work |
| Integrations | Use a dedicated test endpoint. Enter secrets in the app, inspect before enabling, and check execution before retry/replay |
| Commerce | Verify stock, idempotency, cancellation/status and quote expiry. Prevent duplicate shipments and payment requests |

`full-tool-test-ledger.csv` lists all 270 tools as Not run. Exclude AI media generation from the Claude catalog until policy and enforced scope are resolved.

## Real demo recording: approximately five minutes

| Suggested time | Actual action and visible result |
| --- | --- |
| 0:00–0:25 | Show the host, plugin 1.0.1, demo workspace, permissions and endpoint |
| 0:25–1:00 | P1: find the fixture customer and summarize the real synthetic conversation |
| 1:00–1:35 | P2: show the actual SKU, price and stock |
| 1:35–2:35 | P3: show any approval, then pending_review. Do not pay or create shipping |
| 2:35–3:15 | P4: show both date periods and server figures |
| 3:15–4:00 | P5: write/re-read an internal CRM note without sending a message |
| 4:00–4:30 | Show one negative case and the absence of an unauthorized action |
| 4:30–5:00 | Explain support, external payment and pending versus completed states |

Rehearse first. An existing development connection can be used; a submission upload is not required merely to begin recording. Capture actual screen activity rather than mockups or fabricated results. Hide passwords, tokens, mailbox content and unrelated workspaces. Review prompt/result legibility, scenario coverage and secret exposure. Host the video somewhere the reviewer can play it; verify access while signed out before adding its URL to the manifest. No hosting destination has been selected.

## Secure reviewer-access fields

Supply login URL, demo workspace name, username, password/sign-in method, permissions, plan, fixtures, expected approval steps and no-charge testing instructions only through secure dashboard fields. This is a checklist, not a place to store credentials. Keep the test account available during review and re-review.
