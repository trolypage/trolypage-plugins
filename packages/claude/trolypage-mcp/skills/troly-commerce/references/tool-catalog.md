# Directory profile tool reference

Source snapshot: 2026-10-19. The server enforces this catalog at discovery and execution. Workspace permissions and plan may further restrict it. A listed capability is not proof of successful end-to-end testing. Annotation details are authoritative in the live MCP response.

| Tool | Module | Description |
| --- | --- | --- |
| `list-orders` | commerce | List workspace orders, filtered by status (pending, confirmed, completed, cancelled), approval_status (pending_review, approved, rejected) and date range. |
| `get-order` | commerce | Order details: customer, items, status, payment and shipment. |
| `create-order` | commerce | Create a customer order with pending_review approval status. The shop owner reviews it in TrolyPage before confirmation. Product prices and stock come from the catalog, not AI-supplied amounts. |
| `cancel-order` | commerce | Cancel/delete an order. Refused when an active shipment exists; deducted stock is restored automatically. |
| `order-payment-qr` | commerce | Creates a VietQR code or payment link through a connected gateway. Amount, currency and reconciliation reference are taken from the order. It does not debit an account or establish payment receipt. |
| `check-payment` | commerce | Returns the order payment state confirmed by the backend, including bank-webhook reconciliation; it does not change the payment state. |
| `search-products` | commerce | Search products by name, SKU or description. Returns price, stock, variants and sellability. |
| `get-product` | commerce | Product details: price, stock, variants and sales status. |
| `quote-shipping` | commerce | Quote shipping for an order. Recipient address, COD and weight come from the order; only order_id is required. |
| `quote-ondemand-shipping` | commerce | Quote on-demand delivery (AhaMove, GrabExpress, etc.) for an order. |
| `create-shipment` | commerce | Creates a real carrier shipment for an approved, confirmed order using a selected quoted carrier rate. |
| `create-ondemand-shipment` | commerce | Create an on-demand delivery order (AhaMove, GrabExpress, etc.) after the customer selects a service. |
| `track-shipment` | commerce | Look up shipment status by tracking number or internal order ID. |
| `list-bookings` | commerce | List workspace bookings, newest first. |
| `create-booking` | commerce | Create a customer booking. Checks working hours, timezone and resource/staff capacity. |
| `booking-resources` | commerce | Returns booking resources, working hours, timezone, capacity and workspace staff identifiers. |
| `cancel-booking` | commerce | Mark a booking cancelled while retaining its history. |
| `create-product` | commerce | Creates a catalog product with supplied prices, stock, image URLs and variants. This changes the workspace catalog. |
| `delete-product` | commerce | Removes a workspace product through its deletion workflow. |
| `duplicate-product` | commerce | Creates a copy of an existing workspace product. |
| `restore-product` | commerce | Restores an eligible workspace product. |
| `update-booking` | commerce | Reschedules or updates a booking while checking working hours, timezone, customer/staff conflicts and capacity. The booking identifier and history are retained. Verified working_hours and timezone are required when no resource is configured. |
| `update-order` | commerce | Update recipient, address and order fields using the shop order workflow. |
| `update-product` | commerce | Updates supplied fields of an existing workspace product. |
| `get-booking` | commerce | Returns booking details, duration, timezone, assigned resource/staff and current state. |
| `list-products` | commerce | Returns paginated workspace catalog products matching the supplied filters. |
| `get-product-import` | commerce | Returns workspace product import details. |
| `update-product-import` | commerce | Updates supplied fields of an existing workspace product import. |
| `upload-product-import` | commerce | Uploads CSV/XLSX/JSON/ZIP bytes for parsing and review; this can consume AI text-parsing quota. Limit: 6 MiB decoded, or 64 KiB arguments when queued for approval. Uploading alone does not create catalog products. |
| `update-customer-profile` | commerce | Updates contact and profile fields of an existing workspace subscriber. Only supplied fields are changed. |
| `create-customer-address` | commerce | Saves a shipping address for an existing customer and returns its identifier. Provider location codes and supplied verification state are validated; coordinate warnings indicate that the location is not verified. |
| `update-customer-address` | commerce | Updates an existing customer address. Street is required; verification state represents evidence supplied for that address. |
| `set-default-customer-address` | commerce | Select the default shipping address from addresses owned by this customer. |
| `get-customer-addresses` | commerce | Returns an existing customer profile and saved shipping addresses without creating a customer record. An empty address list indicates that no saved address is available. |
| `shipping-locations` | commerce | Returns the deployed Goship city/district/ward catalog with provider identifiers, pagination and catalog health. District and ward lookups require their parent identifiers. An unavailable catalog requires operator synchronization. |
| `check-booking-availability` | commerce | Checks a proposed slot against working hours, timezone, customer/staff conflicts and resource capacity; returns alternatives on conflict. It does not create a booking or reserve a slot. Availability can change before booking creation. |
| `cancel-shipment` | commerce | Cancels an eligible Goship shipment through the carrier and synchronizes shipment/order state. Delivered, returning and already-cancelled shipments are rejected. Shipment cancellation must complete before order cancellation. |
| `list-shipments` | commerce | Returns paginated shipment identifiers, tracking, status and settlement information. Local status reflects the most recent carrier synchronization. |
| `send-booking-confirmation` | commerce | Send a booking confirmation through a configured ManyChat flow. Requires a real flow_ns and connected account; returns an error when delivery is not confirmed. This does not enable an unconfigured channel. |
