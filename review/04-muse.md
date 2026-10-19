# Muse submission form draft

Portal: https://platform.muse.ai/submission. Only the Overview form and payment choices have been inspected. No form data has been entered or saved, and no submission has been sent.

## Overview: observed form fields

| Field | Draft value |
| --- | --- |
| Connector name | TrolyPage |
| Company or developer | TROLYPAGE COMPANY LIMITED |
| Product website | https://trolypage.com/mcp |
| Connector icon | assets/trolypage-mobile-icon-512.png |
| Your name | Alex Nguyen |
| Work email | support.mcp@trolypage.com |
| Support email or URL | support@trolypage.com |
| Privacy policy | https://trolypage.com/privacy-policy — correct stale publisher details first |
| Terms of service | https://trolypage.com/terms-of-service |

### Example prompts

```text
Find a customer and summarize their latest conversation without sending a message.
Find a product by SKU and show its current price and stock.
Prepare an order for shop review without confirming it, taking payment or creating shipping.
Compare sales for the last 30 days with the previous period.
Add an internal CRM note without contacting the customer.
```

### Payments

The observed choices are `My connector accepts payments` and `My connector does not accept payments`. Because the catalog includes commerce, payment QR and payment-status tools, do not select the latter solely because payment occurs externally. The owner must check the portal definition. If external merchant payment is included, select the former and use the disclosure below. If Muse requires completing payment inside Muse, clarify the external-payment scope before claiming support.

TrolyPage supports merchant product lookup, order preparation and management, payment QR generation/status checks, shipping and bookings. Customers complete payment outside the assistant using the merchant's supported payment method. This integration does not directly debit bank accounts or transfer financial assets. A generated QR, unpaid order or pending approval is not a completed payment. Merchant/provider/region restrictions apply.

### Additional information: draft

TrolyPage is a first-party business-operations connector for workspace owners and administrators. It provides authenticated customer context, catalog/order operations and reporting rather than a list of public links. We intend availability in all Muse-supported countries; connected merchant/provider services may be region-specific. Payment is completed through the merchant's external payment flow. Reviewers will receive a dedicated populated test workspace through secure review fields. No live charge or customer communication is required for the core review cases. The current candidate still requires the readiness items in the accompanying review pack to be completed.

## Technical specifications

This material is prepared from documentation; the layout of step 2 has not been verified. Transport: Streamable HTTP. Production endpoint: https://trolypage.com/mcp/troly. OAuth discovery: https://trolypage.com/.well-known/oauth-authorization-server. Public DCR client, PKCE S256, scope `mcp:use`; no client secret in a public archive. See 05-technical-and-data.md, tool-inventory.csv and tool-contracts.json for contracts, proposed classifications and inspection limits.

Muse sensitive writes require the host's per-action approval. TrolyPage Auto/Hybrid modes do not replace it. Read-only OAuth has not been established: the inspected source filters `mcp:read` for PersonalAccessToken, while discovery advertises only `mcp:use`. Resolve this gap before declaring support.

## Review

Use the shared processing, test and reviewer-access materials. Confirm retention, processors and security contact with the operator. Only an authorized person may accept developer terms. No submission has been sent.

Source: https://platform.muse.ai/docs
