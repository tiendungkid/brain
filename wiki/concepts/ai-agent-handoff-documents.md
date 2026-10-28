---
tags: [ai-engineering, engineering-practices]
sources: [Senior developer experience.md]
created: 2026-10-28
updated: 2026-10-28
---

# AI Agent Handoff Documents

Tài liệu bàn giao mà AI agent nên sinh ra sau khi làm xong việc, để người khác (người deploy, QA) nắm được phần việc của họ mà không cần đọc code.

## Hai loại chính

| Tài liệu | Khi nào | Người đọc |
| --- | --- | --- |
| [[deployment-checklist\|Deployment Checklist]] | Xong một task lớn, trước khi merge staging/production | Người giao task / người deploy |
| [[qa-quick-checklist\|QA Quick Checklist]] | Việc dev tự phát sinh: hotfix, security fix | QA |

Hai tài liệu có thể tham chiếu nhau: QA checklist ghi rõ case nào chạy sau bước nào của deploy checklist.

## Nguyên tắc chung

- **Hỏi trước khi generate.** Agent không tự đoán: hỏi người dùng có cần file không, và hỏi dev đã làm gì.
- **Lưu ngữ cảnh để không hỏi lại.** Thông tin ổn định của project (có CI/CD không, CI/CD lo những gì) lưu vào `CLAUDE.md` của [[claude-code|Claude Code]].
- **Dịch sang ngôn ngữ người đọc.** Chỉ ghi việc người đọc thực sự phải làm, kèm lý do ngắn gọn.
- **Kích hoạt bằng hook.** Nhắc người dùng khi agent hoàn thành task, thay vì trông vào việc người dùng nhớ ra.

Nguồn: [[senior-developer-experience|Senior Developer Experience]].
