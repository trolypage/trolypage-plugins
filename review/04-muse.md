# Muse — nội dung form để copy sau khi review

Portal: https://platform.muse.ai/submission. Mới đọc Overview và danh sách Payments; chưa điền, lưu draft, chuyển bước bằng dữ liệu thật hay submit.

## Overview — trường đã nhìn thấy trên form

| Field | Draft value |
| --- | --- |
| Connector name | TrolyPage |
| Company or developer | TROLYPAGE COMPANY LIMITED |
| Product website | https://trolypage.com/mcp |
| Connector icon | assets/trolypage-mobile-icon-512.png |
| Your name | Alex Nguyen |
| Work email | support.mcp@trolypage.com |
| Support email or URL | support@trolypage.com |
| Your privacy policy | https://trolypage.com/privacy-policy — correct stale publisher details before submission |
| Your terms of service | https://trolypage.com/terms-of-service |

### Example prompts

```text
Find a customer and summarize their latest conversation without sending a message.
Find a product by SKU and show its current price and stock.
Prepare an order for shop review without confirming it, taking payment or creating shipping.
Compare sales for the last 30 days with the previous period.
Add an internal CRM note without contacting the customer.
```

### Payments

Form hiện có hai nhãn: `My connector accepts payments` và `My connector does not accept payments`. Vì có commerce, payment QR và check-payment, không nên tự chọn "does not accept payments" chỉ vì tiền được trả bên ngoài. Chủ tài khoản cần xem định nghĩa của portal; nếu bao gồm external merchant payment, chọn `My connector accepts payments` và dùng phần giải thích dưới đây. Nếu Muse yêu cầu hoàn tất payment ngay trong Muse, phạm vi external-payment-only cần được làm rõ với reviewer trước khi khai hoàn tất giao dịch.

TrolyPage supports merchant product lookup, order preparation and management, payment QR generation/status checks, shipping and bookings. Customers complete payment outside the assistant using the merchant's supported payment method. This integration does not directly debit bank accounts or transfer financial assets. A generated QR, unpaid order or pending approval is not a completed payment. Merchant/provider/region restrictions apply.

### Anything else — draft

TrolyPage is a first-party business-operations connector for workspace owners and administrators. It provides authenticated customer context, catalog/order operations and reporting rather than a list of public links. We intend availability in all Muse-supported countries; connected merchant/provider services may be region-specific. Payment is completed through the merchant's external payment flow. Reviewers will receive a dedicated populated test workspace through secure review fields. No live charge or customer communication is required for the core review cases. The current candidate still requires the readiness items in the accompanying review pack to be completed.

## Technical specs — nội dung chuẩn bị từ tài liệu, chưa xác minh layout của bước 2

Transport Streamable HTTP; production endpoint https://trolypage.com/mcp/troly; OAuth discovery https://trolypage.com/.well-known/oauth-authorization-server; public DCR client; PKCE S256; scope mcp:use; no client secret in a public archive. Xem 05-technical-and-data.md, tool-inventory.csv và tool-contracts.json để có inputs/outputs, phân loại đề xuất và giới hạn kiểm tra.

Muse phân loại sensitive write và yêu cầu approval của host mỗi lần; TrolyPage Auto/Hybrid không thay thế approval của Muse. Khả năng Read Only qua OAuth chưa được source hiện tại chứng minh: mã hiện chỉ lọc mcp:read cho PersonalAccessToken, còn OAuth discovery chỉ công bố mcp:use. Đây là gap cần quyết định, không khai là đã hỗ trợ.

## Review

Điền dữ liệu xử lý, kiểm thử và reviewer access theo hồ sơ chung; xác nhận các phần retention, nhà cung cấp và security contact với người vận hành. Chỉ người có thẩm quyền mới chấp nhận developer terms. Mục này chưa được submit.

Nguồn: https://platform.muse.ai/docs
