# Nội dung đề xuất chỉnh policy / MCP guide — CHƯA XUẤT BẢN

Các đoạn dưới đây là draft biên tập và xác nhận dữ liệu, không phải cam kết pháp lý đã được chủ tài khoản duyệt. Không ghi đã tuân thủ mọi chính sách hoặc đã audit hệ thống chỉ từ source review.

## Publisher identity

Privacy section 13 hiện còn SkyNet Solution và địa chỉ Boulder, US; footer là TROLYPAGE COMPANY LIMITED ở Hà Nội. Mobile support cũng còn SkyNet Solution. Owner cần xác nhận SkyNet là pháp nhân/brand/service provider nào, hoặc thay block cũ bằng đúng publisher. Thông tin công khai hiện có để đối chiếu:

```text
TROLYPAGE COMPANY LIMITED (CÔNG TY TNHH TROLYPAGE)
Enterprise registration number: 0111551901
Registered office: No. 72, Alley 318 De La Thanh, O Cho Dua Ward, Hanoi, Vietnam
Support: support@trolypage.com
MCP submission contact: support.mcp@trolypage.com
```

Người gửi hồ sơ được chủ tài khoản xác nhận là Alex Nguyen. Giữ nguyên verified business identity Trolypage.

## MCP policy coverage — proposed wording to verify

When you connect an AI assistant to TrolyPage through MCP, the assistant sends the arguments for the tools you request and receives their results. Depending on the selected tools, those results can contain workspace customer information, conversations, internal notes, orders, products, reports, social content, knowledge, agent configuration or managed assets. Access is limited by the account, workspace role, plan and connection permissions.

Write tools may change internal records or request actions in connected services. Drafts and pending approvals are distinct from completed sends, publication, payment and delivery. You can disconnect the connector in the host and revoke the TrolyPage authorization to stop further access. Disconnecting does not remove data already returned to the AI host or content already sent to third-party services; consult each provider's controls and TrolyPage's published deletion instructions.

Payment associated with a merchant order takes place outside the assistant through the merchant's supported flow. TrolyPage may return a payment QR or payment status. A QR or submitted request does not itself establish receipt of money.

**Owner must verify before publication:** exact processors and AI-use conditions, retention/deletion of connector logs and results, international transfers, model-training/secondary-use restrictions, encrypted storage and incident contact. Không thêm thời hạn hay sự đảm bảo mới chưa xác nhận.

## Guide copy corrections

- Catalog heading: "One unified connection plus focused module endpoints. Available tools depend on workspace permissions and plan." Tránh số lượng hardcode.
- Analytics: "Metrics are read-only. Report exports queue a job and are write operations."
- Approval: "TrolyPage supports Auto, Hybrid and Strict modes. Some writes can execute directly in Auto/Hybrid; inspect the actual returned state. Strict queues writes. Shop order approval, broadcast approval and the AI host's confirmation rules are separate controls."

Chỉ sửa bản nguồn không đảm bảo production đã đổi, nhất là khi translation strings/cache có nội dung cũ. Mở lại URL public và kiểm tra đúng các block sau deploy.
