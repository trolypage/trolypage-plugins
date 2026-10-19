# Submission progress — October 19, 2026

## Claude

The separate TrolyPage MCP connector was submitted successfully. The portal displayed “Server submitted for review” and linked to https://claude.ai/directory/manage/trolypage. It uses https://trolypage.com/mcp/claude with 180 tools (90 read and 90 write), English metadata and an enforced execution allowlist. AI media generation remains in the separate full service.

The owner directly confirmed prior execution of every tool in the submitted catalog through MCP Inspector / Claude. This is an owner attestation, not a claim that this preparation session independently reran all 180 tools. Bundle 1.0.2 at commit `4ac9cfa` passed format, directory-policy and security scans. Publish requested; waiting for Anthropic review. Neither receipt means approval or a live listing.

## Independent synthetic workflows

The correct TrolyPage Reviewer workspace has an Owner member, Scale plan and Full / Direct execution mode. Website widget #44 supplied one synthetic inbound conversation. Exact non-secret IDs are in `review/fixture-map.json`.

Observed through the Claude custom connector: customer/conversation lookup, product creation and lookup, unpaid pending order #54, a same-key retry reusing that order, sales comparison and internal notes re-read from the customer profile. No customer reply, social publication, payment, payment link or shipment was executed. The combined negative-scope walkthrough refused money movement, unauthorized tenant access and secret extraction without business-tool calls. These are adapted representative cases, not separate execution of every OpenAI-host prompt or an exhaustive security assessment.

The sales report includes the pending order's 200000 VND as reported revenue. This is unpaid order value, not money received. The previous period is empty.

## Production order fix

A text idempotency token was incorrectly stored in a numeric source-record column, causing a MySQL error. The service now retains the full text in the idempotency key and stores only numeric source references in the numeric column. Exception responses no longer expose raw SQL or database identifiers; private server logging remains.

The relevant isolated suite passed **271 tests / 36,190 assertions**. Two broader shipping-audit tests fail identically against the original service baseline; they are pre-existing failures outside this fix. Production PHP syntax and source hashes were checked before atomic deployment with a private rollback copy. Actual creation and retry then succeeded without duplicates. Backend source and private deployment files are excluded from this distribution repository.

## OpenAI

Business identity and domain verification passed. The scan account completed OAuth, 271 full-endpoint tools were discovered, and reviewer credentials were saved securely in portal fields. Generic new-tool findings are explicitly non-blocking for submission. Five positive and three negative cases are imported. Candidate 1.0.2 updates real fixtures, report setup and the video reference. Verify the public recording before upload. Alex chose to complete the final portal action personally. The portal subsequently showed **metadata and skills 1.0.2 In review**, with MCP **Configured / Authorized**. All saved review information, including secure credentials, five positive/three negative cases, video URL and release notes, was inspected after reupload. No approval or publication is claimed.

## Muse

All **3/3** follow-up requirements are now complete: business verification, integration credentials and the data-processing questionnaire. The portal shows the questionnaire under review and a 3/3 overview receipt.

The owner confirmed BNIX/Vietnam hosting and OpenAI, Anthropic, Google, OpenRouter and Cloudflare, with optional DeepSeek/Qwen or other Chinese-origin models. The submitted form discloses restricted-origin model capability, long retention, deletion limits, user/third-party/minor data, financial/order data and consequential writes. At-rest encryption, administrator MFA, monitoring and incident response are owner-attested, not independently audited. No SOC 2, signed SCC/DPA, adequacy decision or binding corporate rules was claimed. Known Vietnam/US processing and global AI-provider processing were disclosed; provider-specific regions remain subject to review. Availability uses all countries listed by the portal, subject to platform/service restrictions. Reviewer instructions were updated with the actual synthetic fixtures. No payment-service license or custodial money movement is claimed.

The exact Muse callback/origin remains unverified; generic DCR/PKCE credentials were submitted. No permissive allowlist or environment change was introduced.

## Walkthrough provenance

The recording demonstrates real shared MCP business workflows through a Claude reviewer connection, not an OpenAI-host session. It uses timestamped browser-tab captures at variable cadence without invented cursor or keyboard events. Idle intervals are compressed. Raw frames, timestamps and original recording remain privately outside tracked repository paths. This is a workflow demonstration, not independent execution evidence for every catalog tool.

The rendered 132.034-second VP9/WebM contains 7922 frames at 1912×1064 / 60 fps, no audio, and is publicly hosted at https://trolypage.com/demos/connector-review.html. Cirro validation/render succeeded; source capture cadence remains variable.
