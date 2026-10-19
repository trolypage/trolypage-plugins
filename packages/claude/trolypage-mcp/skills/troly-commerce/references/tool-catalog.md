# Current source tool reference

Source snapshot: 2026-10-19. Tools are filtered by the connected workspace. A listed capability is not proof of entitlement or successful execution.

| Tool | Module | Declared annotation(s) | Description |
| --- | --- | --- | --- |
| `list-orders` | commerce | readOnlyHint=true | Danh sách đơn hàng của workspace. Lọc theo trạng thái (status: pending, confirmed, completed, cancelled), approval_status (pending_review, approved, rejected) và khoảng ngày. |
| `get-order` | commerce | readOnlyHint=true | Chi tiết một đơn hàng: thông tin khách, sản phẩm (items), trạng thái, thanh toán và vận đơn. |
| `create-order` | commerce | destructiveHint=true, openWorldHint=true | Tạo đơn hàng mới cho khách. Đơn được tạo ở trạng thái chờ duyệt (pending_review) — chủ shop duyệt trong TrolyPage trước khi xác nhận. Giá sản phẩm và tồn kho luôn lấy từ catalog, không tin số tiền do AI gửi. |
| `cancel-order` | commerce | destructiveHint=true | Hủy/xóa một đơn hàng. Từ chối khi đơn đang có vận đơn hoạt động; tồn kho đã trừ sẽ được hoàn lại tự động. |
| `order-payment-qr` | commerce | destructiveHint=true | Tạo mã VietQR hoặc link thanh toán qua cổng đã kết nối cho một đơn hàng. Số tiền, tiền tệ và mã đối soát do hệ thống lấy từ đơn — AI không được tự đặt số tiền. |
| `check-payment` | commerce | readOnlyHint=true | Kiểm tra trạng thái thanh toán của đơn hàng theo dữ liệu backend đã xác nhận (webhook ngân hàng). Chỉ báo "đã nhận thanh toán" khi hệ thống đã chuyển trạng thái — không tự đánh dấu. |
| `search-products` | commerce | readOnlyHint=true | Tìm sản phẩm trong catalog theo tên/SKU/mô tả. Trả về giá, tồn kho, biến thể và trạng thái bán được. |
| `get-product` | commerce | readOnlyHint=true | Chi tiết một sản phẩm: giá, tồn kho, biến thể, trạng thái bán. |
| `quote-shipping` | commerce | readOnlyHint=true | Tính phí vận chuyển cho một đơn hàng. Hệ thống tự lấy địa chỉ người nhận, COD và cân nặng từ đơn — chỉ cần order_id. |
| `quote-ondemand-shipping` | commerce | readOnlyHint=true | Tính phí giao hỏa tốc (AhaMove, GrabExpress...) cho một đơn hàng. |
| `create-shipment` | commerce | destructiveHint=true | Tạo vận đơn thật cho đơn hàng sau khi khách chọn nhà xe (rate lấy từ quote-shipping). Đơn phải ở trạng thái confirmed và đã duyệt. |
| `create-ondemand-shipment` | commerce | destructiveHint=true | Tạo đơn giao hỏa tốc (AhaMove, GrabExpress...) cho một đơn hàng sau khi khách chọn dịch vụ. |
| `track-shipment` | commerce | readOnlyHint=true | Tra cứu trạng thái vận chuyển bằng mã vận đơn hoặc mã đơn. |
| `list-bookings` | commerce | readOnlyHint=true | Danh sách lịch hẹn của workspace, mới nhất trước. |
| `create-booking` | commerce | destructiveHint=true, openWorldHint=true | Tạo lịch hẹn cho khách. Hệ thống tự kiểm tra giờ làm việc, timezone và sức chứa của resource/nhân viên. |
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
