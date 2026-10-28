---
tags: [engineering-practices, ai-engineering]
sources: [Senior developer experience.md]
created: 2026-10-28
updated: 2026-10-28
---

# Senior Developer Experience

**Source:** Senior developer experience.md
**Date ingested:** 2026-10-28
**Type:** notes

## Summary

Ghi chú kinh nghiệm phát triển phần mềm, áp dụng cho AI agent xuyên suốt quá trình làm việc. Gồm hai loại tài liệu bàn giao agent nên sinh ra.

### 1. Deployment checklist

- Khi AI agent hoàn thành một task lớn, cần một "hook" hỏi người dùng có cần file deploy checklist không.
- Mục đích: người giao task nắm được việc phải làm trước và sau khi merge vào staging/production.
- Agent phải hỏi: project có CI/CD không? Nếu có, CI/CD đã làm những gì? Câu trả lời lưu vào `CLAUDE.md` để lần sau không hỏi lại.
- Bỏ qua việc CI/CD đã lo (migration, build application...). Chỉ liệt kê việc làm tay: chạy command một lần, deploy với tham số đặc biệt, lấy secret key từ bên thứ 3...
- Tên file: `[Dev-checklist]-Ten-task.md`.
- Nội dung: bảng tóm tắt (Việc cần làm | Lý do ngắn gọn | Ưu tiên), sau đó chi tiết từng việc (ưu tiên, công việc cần làm, lý do).

### 2. QA quick checklist

- Dùng cho việc dev tự phát sinh, không từ một task cụ thể: hotfix, fix sau khi scan security...
- Là file trung gian để QA hiểu: yêu cầu gốc là gì, dev đã làm gì, QA cần test gì.
- Ví dụ: Shopify yêu cầu app dùng Shopify AI Toolkit security scan toàn bộ project; dev fix theo báo cáo nhưng QA không hiểu ngôn ngữ của dev.
- Phải hỏi dev trước khi generate file.

## Key Claims

- AI agent nên chủ động đề xuất deploy checklist sau khi xong task lớn.
- Deploy checklist chỉ nên chứa việc làm tay mà CI/CD chưa lo.
- Thông tin CI/CD của project nên được lưu vào `CLAUDE.md` để không hỏi lại.
- Việc dev tự fix (hotfix, security fix) cần một QA checklist trung gian vì QA không đọc được báo cáo kỹ thuật.
- Agent phải hỏi người dùng/dev trước khi generate cả hai loại file.

## Entities Mentioned

- [[claude-code|Claude Code]] — hook và file `CLAUDE.md` lưu ngữ cảnh project
- [[shopify-app-security-checks|Shopify App Security Checks]] — ví dụ nguồn phát sinh việc cần QA checklist

## Concepts Covered

- [[ai-agent-handoff-documents|AI Agent Handoff Documents]] — chủ đề chung
- [[deployment-checklist|Deployment Checklist]] — mục 1
- [[qa-quick-checklist|QA Quick Checklist]] — mục 2
