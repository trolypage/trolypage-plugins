"""Apply the owner's contact name and revise local review copy; does not edit the live site."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
description='''TrolyPage is AI customer support, CRM, social media scheduling and order management software for small businesses. It brings customer conversations, products, orders, scheduled content and follow-up work into one business workspace.

This integration connects your AI assistant to an existing TrolyPage workspace. Find customers and summarize conversations, update internal CRM notes, check product prices and stock, prepare orders for shop review, and compare sales reports. You can also manage social post drafts, marketing campaigns, approved knowledge, connected channels, agents, assets, workflows and configured integrations when those modules are available to your account.

Sign in with OAuth and select the workspace you administer. Access requires an owner or administrator role and a plan with the requested MCP modules. Some AI and media actions consume additional quota. Channel features, delivery services and payment methods vary by account, provider and region.

TrolyPage supplies the authoritative price, stock, total and payment status. Drafts, pending approvals, completed actions and delivery to an external service are distinct. Authorized writes can change records, send messages, publish posts or request services. Customers complete merchant payments outside the AI assistant; a payment QR or pending request does not prove that money was received.'''
vi_description='''TrolyPage là phần mềm AI chăm sóc khách hàng, quản lý CRM, lên lịch bài đăng mạng xã hội và xử lý đơn hàng cho doanh nghiệp nhỏ. Hội thoại, sản phẩm, đơn hàng, nội dung và công việc chăm sóc lại khách được quản lý trong một workspace.

Bản tích hợp kết nối trợ lý AI với workspace TrolyPage sẵn có: tìm khách và tóm tắt hội thoại, cập nhật ghi chú CRM nội bộ, kiểm tra giá và tồn kho, tạo đơn chờ shop duyệt, so sánh báo cáo bán hàng. Các module được cấp quyền còn hỗ trợ bài nháp, chiến dịch, tri thức, kênh, AI Agent, tài nguyên, workflow và tích hợp.

Đăng nhập OAuth, chọn workspace bạn quản trị và dùng gói có quyền MCP tương ứng. Một số tác vụ AI/media tiêu hao quota; khả năng kênh, vận chuyển và thanh toán tùy tài khoản, nhà cung cấp và khu vực. Giá, tồn kho, tổng tiền và trạng thái thanh toán do TrolyPage xác nhận. Phân biệt bản nháp, chờ duyệt, đã thực thi và giao ra kênh. Thanh toán diễn ra bên ngoài trợ lý AI; có QR hoặc yêu cầu chờ xử lý chưa có nghĩa đã nhận tiền.'''
subtitle='AI support, CRM & social posts'
vi_subtitle='AI chăm khách, CRM & đăng bài'
prompts=[
 'Summarize a customer conversation and draft a reply for me to review.',
 'Find a product by SKU and prepare an order for shop review.',
 'Compare sales for the last 30 days with the previous period.'
]

def save(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest_path=ROOT/'packages/openai/trolypage-mcp/plugin.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
ext=manifest['extensions']['com.openai'];interface=ext['interface']
old_description=interface['longDescription']
old_vi=ext['publication']['translations']['vi-VN']['description']
old_subtitle=interface['shortDescription'];old_vi_subtitle=ext['publication']['translations']['vi-VN']['subtitle']
old_prompts=interface['defaultPrompt']
interface.update({'shortDescription':subtitle,'longDescription':description,'defaultPrompt':prompts})
ext['publication']['translations']['vi-VN']={'subtitle':vi_subtitle,'description':vi_description}
ext['publication']['release_notes']+=' Clarify customer support, CRM, social scheduling and order-management use cases for people unfamiliar with TrolyPage; confirm submission contact Alex Nguyen.'
save(manifest_path,manifest)
owner_path=ROOT/'review/owner-decisions.json'
owner=json.loads(owner_path.read_text(encoding='utf-8'));owner['contact_person_name']='Alex Nguyen';save(owner_path,owner)

for p in (ROOT/'review').glob('*.md'):
    s=p.read_text(encoding='utf-8')
    replacements={
     'Chưa được chủ tài khoản xác nhận; không tự dùng tên đại diện pháp luật':'Alex Nguyen — chủ tài khoản xác nhận',
     "Owner to confirm the submitter's full name":'Alex Nguyen',
     'tên người gửi vẫn chờ xác nhận':'người phụ trách: Alex Nguyen',
     'Xác nhận tên/URL workspace, tên người gửi, repo/license và nơi host demo':'Người phụ trách đã xác nhận là Alex Nguyen. Xác nhận tên/URL workspace, repo/license và nơi host demo',
     'Không tự lấy Nguyễn Duy Hùng làm người gửi form chỉ vì tên có trong đăng ký doanh nghiệp.':'Người gửi hồ sơ được chủ tài khoản xác nhận là Alex Nguyen. Giữ nguyên verified business identity Trolypage.',
     '| Contact email | support.mcp@trolypage.com |':'| Contact person | Alex Nguyen |\n| Contact email | support.mcp@trolypage.com |'
    }
    for a,b in replacements.items():s=s.replace(a,b)
    if p.name=='01-listing-and-copy.md':
        s=s.replace(old_description,description).replace(old_vi,vi_description).replace(old_subtitle,subtitle)
        s=s.replace('\n'.join('- '+x for x in old_prompts),'\n'.join('- '+x for x in prompts))
    p.write_text(s,encoding='utf-8')

for target in ['openai','claude']:
    p=ROOT/'packages'/target/'trolypage-mcp/README.md'
    s=p.read_text(encoding='utf-8').replace(old_description,description)
    s=s.replace('## Connection','[Explore product features](https://trolypage.com/features) · [MCP setup and troubleshooting](https://trolypage.com/mcp)\n\n## Connection',1)
    p.write_text(s,encoding='utf-8')
claude_path=ROOT/'packages/claude/trolypage-mcp/.claude-plugin/plugin.json'
claude=json.loads(claude_path.read_text(encoding='utf-8'))
claude['description']='AI customer support, CRM, social media scheduling and order management in your authorized TrolyPage workspace.'
claude['keywords']=['trolypage','customer-support','crm','social-media-scheduling','order-management']
save(claude_path,claude)

# Keep the optional initial-snapshot generator consistent with accepted copy.
p=ROOT/'build-review-pack.py';s=p.read_text(encoding='utf-8')
s=s.replace(old_description,description).replace(old_vi,vi_description).replace(old_subtitle,subtitle).replace(old_vi_subtitle,vi_subtitle)
s=s.replace("'contact_person_name': None", "'contact_person_name': 'Alex Nguyen'")
for a,b in replacements.items():s=s.replace(a,b)
old_literal=repr(old_prompts)
s=s.replace(old_literal,repr(prompts))
s=s.replace('Workspace demo và video thật; tên người gửi;', 'Workspace demo và video thật;')
p.write_text(s,encoding='utf-8')
p=ROOT/'README.md';s=p.read_text(encoding='utf-8').replace('Workspace demo và video thật; tên người gửi;', 'Workspace demo và video thật;')
s=s.replace('## Review theo thứ tự','Người phụ trách: **Alex Nguyen**, email **support.mcp@trolypage.com**. Bản review bổ sung phần SEO/khả năng được tìm thấy ở `review/09-seo-and-discovery.md`.\n\n## Review theo thứ tự')
p.write_text(s,encoding='utf-8')
print(json.dumps({'contact':'Alex Nguyen','subtitle':subtitle,'subtitle_length':len(subtitle),'vi_subtitle_length':len(vi_subtitle),'description_length':len(description),'brand_unchanged':interface['displayName']},ensure_ascii=False))
