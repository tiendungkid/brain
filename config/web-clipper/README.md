# Obsidian Web Clipper

Lưu cấu hình và template của extension Obsidian Web Clipper cho vault này.

| File | Nội dung |
| --- | --- |
| `second-brain-template.json` | Template lưu bài vào `raw/`. Có thêm property `why` để ghi lý do lưu bài |
| `obsidian-web-clipper-settings.json` | Bản export toàn bộ settings. Bị `.gitignore` vì có thể chứa API key của Interpreter |

## Import template

1. Mở Web Clipper → ⚙️ Settings → **Templates** → **Import**, chọn `second-brain-template.json`.
2. Kéo template **Second Brain** lên đầu danh sách: template đầu tiên là template mặc định.

## Backup / khôi phục toàn bộ settings

- Backup: Settings → **General** → **Export all settings** → **Export**, lưu vào thư mục này với tên `obsidian-web-clipper-settings.json`.
- Khôi phục: Settings → **General** → **Import all settings** → **Import**, chọn file trên. Thao tác này **thay thế toàn bộ** settings hiện tại.
- Sau khi sửa template trong extension, dùng **Export** của template đó để ghi đè `second-brain-template.json`.
