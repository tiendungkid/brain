---
tags: [engineering-practices, ai-engineering]
sources: [Senior developer experience.md]
created: 2026-10-28
updated: 2026-10-28
---

# Deployment Checklist

File liệt kê việc **phải làm tay** trước và sau khi merge code vào staging/production. AI agent đề xuất tạo file này khi hoàn thành một task lớn. Là một loại [[ai-agent-handoff-documents|AI Agent Handoff Documents]].

## Trước khi generate: hỏi về CI/CD

- Project này có CI/CD không?
- Nếu có, CI/CD đã làm những gì?

Lưu câu trả lời vào `CLAUDE.md` ([[claude-code|Claude Code]]) để lần sau không hỏi lại.

## Có gì và không có gì

- **Bỏ qua** việc CI/CD đã lo: migration, build application...
- **Liệt kê** việc làm tay: chạy command một lần, deploy với tham số đặc biệt, lấy secret key từ bên thứ 3...

## Format

Tên file: `[Dev-checklist]-Ten-task.md`

Bắt đầu với bảng tóm tắt:

```md
| Việc cần làm | Lý do (Ngắn gọn) | Ưu tiên |
|--------------|------------------|---------|
```

Tiếp theo là chi tiết từng việc:

```
1. Việc 1
- Ưu tiên
- Công việc cần làm
- Lý do làm việc này
```

Ghi chú: trong ví dụ thực tế đi kèm [[qa-quick-checklist|QA Quick Checklist]], deploy checklist được đặt tên `deploy-checklist-<chủ-đề>-<YYYY-MM-DD>.md` trong `docs/`, khác với quy ước `[Dev-checklist]-Ten-task.md` của nguồn.

Nguồn: [[senior-developer-experience|Senior Developer Experience]].
