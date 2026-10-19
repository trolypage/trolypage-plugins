# Claude — MCP connector và plugin bundle

Theo lựa chọn của chủ tài khoản: chuẩn bị cả hai listing, dùng cùng tổ chức sở hữu. Repository public đã được chủ tài khoản chọn: https://github.com/trolypage/trolypage-plugins. Giấy phép bundle còn chờ lựa chọn.

## A. MCP connector

| Nội dung | Bản điền |
| --- | --- |
| Name | TrolyPage |
| Description | Dùng bản English ở 01-listing-and-copy.md, chỉ giữ các khả năng thực sự được catalog Claude expose |
| Server URL hiện có | https://trolypage.com/mcp/troly |
| Transport | Streamable HTTP |
| Authentication | OAuth authorization code + PKCE S256; public DCR client |
| Discovery | https://trolypage.com/.well-known/oauth-authorization-server |
| Scope | mcp:use |
| Publisher | Trolypage; kiểm tra tên tổ chức trong portal trước khi nộp |
| Contact person | Alex Nguyen |
| Contact email | support.mcp@trolypage.com |
| Support | support@trolypage.com; https://trolypage.com/mcp#errors |
| Website / privacy / terms | Theo 01-listing-and-copy.md; phải xử lý lỗi identity trong Privacy trước |
| Available countries | All platform-supported countries, subject to provider restrictions |
| Reviewer access | Chờ chủ tài khoản tạo workspace demo; nhập qua trường bảo mật |

### Chặn trước khi nộp endpoint chung

- Catalog hiện có `generate-social-image`; connector criteria hiện không nhận khả năng tạo ảnh/video/audio bằng AI. Phải giới hạn ở SERVER hoặc ở một profile OAuth có enforcement thật, rồi kiểm tra tools/list. Chỉ bỏ tên tool trong README hoặc prompt không làm tool biến mất.
- `execute-integration-operation` chỉ khai báo openWorldHint, thiếu phân loại read/write rõ ràng. Đọc cách operation có thể gọi HTTP method nào và tách công cụ đọc/ghi hoặc loại khỏi catalog Claude nếu cần. Không dùng một tool như lối đi vòng cho khả năng đã bị loại.
- Nếu chọn endpoint/profile khác, lấy URL thật từ bản triển khai đã kiểm tra; không tự đổi sang một path dự đoán trong manifest.
- Test từng tool thực sự expose, cả qua MCP Inspector và Claude custom connector. Ledger 270 tools hiện ở trạng thái Not run; bộ 5+3 là tập ca đại diện, chưa thay thế kiểm thử toàn catalog.

## B. Plugin bundle

Source ở `packages/claude/trolypage-mcp`, archive `archives/claude-trolypage-mcp-1.0.1-DRAFT.zip` để review local. Claude Directory lấy bundle từ GitHub, không nộp ZIP này như form OpenAI.

Bundle giữ 9 skills sẵn có của TrolyPage, làm mới catalog theo source và dùng `.claude-plugin/plugin.json` cùng `.mcp.json`. MCP connection vẫn trỏ endpoint thật hiện có và còn blocker ở phần A; không giả định đã có bộ lọc Claude.

Repository: https://github.com/trolypage/trolypage-plugins. Plugin path: `packages/claude/trolypage-mcp`; branch: `codex/submission-preparation`. Đây là repo gói phát hành và hồ sơ review. Chọn đúng branch/path và kiểm tra commit trong portal khi chuẩn bị submit.

Chủ tài khoản cần chọn license cho riêng nội dung bundle skills. Chưa có LICENSE hay giá trị license được tự ý gán; đây là blocker của bundle listing. Quyết định này không yêu cầu công khai backend ứng dụng.

Sau khi các blocker được giải quyết: vào https://claude.ai/directory/manage, gửi MCP connector và bundle dưới cùng tổ chức, validate repository và kiểm tra việc pair hai listing. Không tick các xác nhận đã test nếu chưa chạy thật.

## Nguồn

- https://claude.com/docs/directory/publish
- https://claude.com/docs/plugins/pre-submission-checklist
- https://claude.com/docs/connectors/building/review-criteria
- https://claude.com/docs/connectors/building/submission
