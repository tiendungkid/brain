---
tags: [engineering-practices, ai-engineering]
sources: [Senior developer experience.md]
created: 2026-10-28
updated: 2026-10-28
---

# QA Quick Checklist

File trung gian giúp QA hiểu và test những việc **dev tự phát sinh**, không đến từ một task cụ thể: hotfix, fix sau khi scan security... Là một loại [[ai-agent-handoff-documents|AI Agent Handoff Documents]].

## Vì sao cần

QA không đọc được ngôn ngữ của dev. Ví dụ: Shopify yêu cầu scan bảo mật bằng [[shopify-app-security-checks|Shopify App Security Checks]], dev fix theo báo cáo kỹ thuật, QA đọc báo cáo không biết phải test gì. File phải trả lời:

- Yêu cầu gốc là gì (Shopify yêu cầu gì)?
- Dev đã làm những gì?
- QA cần test tính năng nào?

Agent phải **hỏi dev trước khi generate**.

## Format

Theo mẫu tác giả cung cấp: <https://github.com/shopify-dhnl/product-rental/blob/main/docs/qa-checklist-security-scan-2026-10-27.md>

- **Tên file:** `docs/qa-checklist-<chủ-đề>-<YYYY-MM-DD>.md`, tiêu đề `# QA checklist — <chủ đề> <YYYY-MM-DD>`.
- **Dòng hướng dẫn ghi kết quả:** cột **KQ** ghi ✅ đạt, ❌ lỗi (kèm link ảnh hoặc log).
- **Mục 0 — Môi trường và điều kiện trước khi test:**
  - Môi trường: app/config test, store test.
  - Công cụ và quyền cần có (`curl`, quyền cài/gỡ app, quyền xem log...).
  - Điều kiện tiên quyết (đã merge, đã deploy...), ghi rõ chưa đủ thì không test mục nào.
  - Cách lấy dữ liệu test (ví dụ session token qua DevTools), kèm cảnh báo không dán token vào ticket/chat.
  - Link tới plan của dev.
- **Mỗi fix là một mục** (tiêu đề nói bằng hành vi, ví dụ "Chặn giả mạo webhook Shopify"), có bảng:

```md
| # | Bước | Kỳ vọng | KQ |
| --- | --- | --- | --- |
| 1.1 | (Bình thường) ... | ... | |
| 1.2 | (Chặn) ... | ... | |
```

- **Nhãn bước:** `(Bình thường)` = luồng cũ vẫn chạy (regression); `(Chặn)` = case tấn công/sai phải bị chặn; `(Chuẩn bị)` = bước setup.
- **Bước copy-paste được:** lệnh `curl` đầy đủ với placeholder `<...>`.
- **Kỳ vọng kiểm chứng được:** HTTP status, message, trạng thái dữ liệu cụ thể; ghi kèm hành vi của code cũ để QA phân biệt được bản sửa.
- **Ghi chú chuẩn bị đầu mục** khi cần setup riêng, và thứ tự phụ thuộc với [[deployment-checklist|Deployment Checklist]] (ví dụ "chạy sau bước 1 của deploy checklist").
- **Báo trước kết quả dễ bị hiểu nhầm là regression** (ví dụ lỗi 500 giờ chỉ hiện message chung là đúng).

Nguồn: [[senior-developer-experience|Senior Developer Experience]].
