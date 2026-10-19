# Current source tool reference

Human-readable source descriptions have been translated into English. Tool identifiers and contracts are unchanged; live server wording may differ.

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `list-orders` | commerce | readOnlyHint=true | List workspace orders, filtered by status (pending, confirmed, completed, cancelled), approval_status (pending_review, approved, rejected) and date range. |
| `get-order` | commerce | readOnlyHint=true | Order details: customer, items, status, payment and shipment. |
| `create-order` | commerce | destructiveHint=true, openWorldHint=true | Create a customer order with pending_review approval status. The shop owner reviews it in TrolyPage before confirmation. Product prices and stock come from the catalog, not AI-supplied amounts. |
| `cancel-order` | commerce | destructiveHint=true | Cancel/delete an order. Refused when an active shipment exists; deducted stock is restored automatically. |
| `order-payment-qr` | commerce | destructiveHint=true | Create a VietQR code or payment link through a connected gateway. Amount, currency and reconciliation reference come from the order; the AI must not set the amount. |
| `check-payment` | commerce | readOnlyHint=true | Check payment status using backend-confirmed data (bank webhooks). Report payment received only after the system changes state; do not mark it manually. |
| `search-products` | commerce | readOnlyHint=true | Search products by name, SKU or description. Returns price, stock, variants and sellability. |
| `get-product` | commerce | readOnlyHint=true | Product details: price, stock, variants and sales status. |
| `quote-shipping` | commerce | readOnlyHint=true | Quote shipping for an order. Recipient address, COD and weight come from the order; only order_id is required. |
| `quote-ondemand-shipping` | commerce | readOnlyHint=true | Quote on-demand delivery (AhaMove, GrabExpress, etc.) for an order. |
| `create-shipment` | commerce | destructiveHint=true | Create a real shipment after the customer selects a carrier rate from quote-shipping. The order must be confirmed and approved. |
| `create-ondemand-shipment` | commerce | destructiveHint=true | Create an on-demand delivery order (AhaMove, GrabExpress, etc.) after the customer selects a service. |
| `track-shipment` | commerce | readOnlyHint=true | Look up shipment status by tracking number or internal order ID. |
| `list-bookings` | commerce | readOnlyHint=true | List workspace bookings, newest first. |
| `create-booking` | commerce | destructiveHint=true, openWorldHint=true | Create a customer booking. Checks working hours, timezone and resource/staff capacity. |
| `booking-resources` | commerce | readOnlyHint=true | Discover booking resources, real working hours, timezone, capacity and workspace staff IDs. Read before creating a booking; do not invent availability. |
| `cancel-booking` | commerce | destructiveHint=true | Mark a booking cancelled while retaining its history. |
| `create-product` | commerce | destructiveHint=true | Create product with prices, stock, images and variants. Use reusable media URLs from assets; prices and business facts must come from the user. |
| `delete-product` | commerce | destructiveHint=true | delete product |
| `duplicate-product` | commerce | destructiveHint=true | duplicate product |
| `restore-product` | commerce | destructiveHint=true | restore product |
| `update-booking` | commerce | destructiveHint=true | Reschedule or update a booking with conflict/capacity checks; retains its ID and history. Discover real resource/staff IDs first. Without a configured resource, provide verified working_hours and timezone for scheduling changes. |
| `update-order` | commerce | destructiveHint=true | Update recipient, address and order fields using the shop order workflow. |
| `update-product` | commerce | destructiveHint=true | update product |
| `get-booking` | commerce | readOnlyHint=true | Read booking details, duration, timezone, resource/staff assignment and status before editing or cancellation. |
| `list-products` | commerce | readOnlyHint=true | Browse full product catalog with pagination; search-products is a ranked shortlist, while this tool enumerates all matching records. |
| `get-product-import` | commerce | readOnlyHint=true | get product import |
| `update-product-import` | commerce | destructiveHint=true | update product import |
| `upload-product-import` | commerce | destructiveHint=true | Upload CSV/XLSX/JSON/ZIP product import bytes for parsing and review. Maximum 6 MiB decoded; approval queue limit 64 KiB arguments. This can invoke AI parsing. Inspect and correct the resulting import before shop approval; uploading does not create catalog products. |
| `update-customer-profile` | commerce | destructiveHint=true | Update verified customer contact/profile fields for an existing subscriber. Preserve unrelated data; do not invent phone numbers or shipping details. |
| `create-customer-address` | commerce | destructiveHint=true | Save a shipping address for an existing customer. Use shipping-locations for provider codes, then update-order with the returned address ID. Coordinate warnings mean location is not verified. |
| `update-customer-address` | commerce | destructiveHint=true | Update a customer address. Read the current address first; street is required. Only supply verification status backed by actual evidence. |
| `set-default-customer-address` | commerce | destructiveHint=true | Select the default shipping address from addresses owned by this customer. |
| `get-customer-addresses` | commerce | readOnlyHint=true | Read customer profile and saved shipping addresses for a subscriber without creating a customer record. Use returned address IDs to update an order. Empty addresses mean contact details still need to be collected. |
| `shipping-locations` | commerce | readOnlyHint=true | Look up Goship city/district/ward codes from the deployed location catalog. Select a city before districts and a district before wards; names alone are not provider codes. Returns catalog health and pagination. Missing catalog requires an operator to sync locations. |
| `check-booking-availability` | commerce | readOnlyHint=true | Check a proposed slot using the same working hours, timezone, customer/staff conflicts and capacity rules as create-booking. Returns alternatives on conflict. Does not reserve or create anything; availability can change before creation. Resolve resource and staff IDs using booking-resources first. |
| `cancel-shipment` | commerce | destructiveHint=true | Cancel an eligible Goship shipment through the carrier, then synchronize shipment and order state. Delivered/returning/cancelled shipments are rejected. Read the shipment ID from get-order/list-shipments; cancellation must succeed before cancelling its order. |
| `list-shipments` | commerce | readOnlyHint=true | List shipment IDs, tracking, status and settlement information with pagination. Resolve records before cancellation or checking delivery; local status is the most recent synchronized carrier state. |
| `send-booking-confirmation` | commerce | destructiveHint=true | Send a booking confirmation through a configured ManyChat flow. Requires a real flow_ns and connected account; returns an error when delivery is not confirmed. This does not enable an unconfigured channel. |
