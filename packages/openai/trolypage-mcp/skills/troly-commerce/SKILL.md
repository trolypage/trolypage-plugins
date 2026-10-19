---
name: troly-commerce
description: Operate TrolyPage products, orders, payments, shipping quotes, shipments, tracking, and bookings. Use for catalog lookup, sales operations, payment reconciliation, delivery, or appointment requests.
---

# TrolyPage Commerce

Use only the `trolypage` MCP server. Read [tool-catalog.md](references/tool-catalog.md) to select the tools available for this workflow.

## Workflow

1. Resolve customers, products, orders, and bookings with search/list/get tools.
2. Let TrolyPage remain authoritative for price, inventory, totals, payment status, addresses, COD, weight, and reconciliation codes.
3. Create an order before requesting its payment QR or shipping quote.
4. Create a shipment only from a returned quote and only when the order is confirmed and approved.
5. Report approval state and verify the order, payment, shipment, or booking after execution.

Never mark a payment as received from a screenshot or user assertion, reuse a stale shipping quote, or retry a create call after an approval response.
