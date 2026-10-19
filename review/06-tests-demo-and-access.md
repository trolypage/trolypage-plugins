# Reviewer access, fixtures and walkthrough

The owner supplied reviewer access privately. The authenticated workspace is **TrolyPage Reviewer**, Scale plan, Owner role. Its existing mode is **Full / Direct execution**. Credentials belong only in secure platform fields and are excluded from this repository and archives.

## Verified synthetic fixtures

| Fixture | State |
| --- | --- |
| Customer | Review Customer A; one synthetic website-chat inquiry |
| Product | Review Mug, SKU TLP-REVIEW-MUG, ID 4642, 100000 VND, stored quantity 20; stock tracking disabled; no variants or shipping |
| Order | #54, two mugs, 200000 VND, pending_review, unpaid, not shipped |
| Retry | Same intent key returned #54 with idempotent_reuse; no duplicate |
| Notes | Exact requested fixture note and separate video-review note verified in profile |
| Providers | Website widget #44; no live social, carrier or bank integration added |

See `fixture-map.json`. No real customer, recipient or payment data was used. Report revenue includes pending unpaid order value and does not establish payment receipt. The previous period can legitimately be zero.

## Tests and limits

The owner confirmed prior execution of every submitted Claude directory tool through MCP Inspector / Claude on October 19, 2026. The directory ledger separates this attestation from independently observed calls. This session exercised customer/conversation lookup, product creation/lookup, order creation and retry, sales reporting and internal notes through the directory connection.

`test-results.csv` records five adapted positive scenarios and a combined three-request negative-scope walkthrough. Negative requests were refused without tool calls. These observations do not claim external provider delivery, all-tool re-execution, an exhaustive security audit or execution within OpenAI's host. Local tests, portal scans and business workflows have separate evidence.

The production order fix passed 271 relevant tests / 36,190 assertions. Two broader shipping-audit failures also reproduce against the original baseline. See `evidence/submission-progress-20261019.md`.

## Recording

The actual walkthrough uses Claude to demonstrate shared TrolyPage MCP workflows on synthetic data: customer/product context, pending order retry, actual report figures and a verified internal note, then refusals for money movement, unauthorized tenant access and secret extraction. It does not show OpenAI-host execution or AI media generation.

Capture uses timestamped browser-tab screenshots at variable cadence; idle intervals are compressed. No cursor/input events were fabricated. Original frames and metadata remain outside tracked paths. Verify the published video for legibility and absence of secrets before portal upload.

Keep the account and fixtures available during review. Independent sign-in from the platform reviewer's environment remains unverified; assist if Cloudflare or an account restriction blocks access. Do not weaken authorization boundaries.
