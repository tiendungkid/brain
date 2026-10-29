# PhpStorm Inspect CLI (PHP/Laravel)

Chạy bộ inspection của PhpStorm bằng CLI (`bin/inspect.bat` / `inspect.sh` có sẵn trong PhpStorm) để AI agent tự kiểm tra code PHP/Laravel sau khi viết. Tool dùng license PhpStorm sẵn có, không cần Qodana (bản PHP của Qodana phải mua license Ultimate).

| File | Vai trò |
|------|---------|
| `phpstorm-inspect.sh` | Chạy PhpStorm inspect trên một project rồi in kết quả gọn |
| `inspect-summary.py` | Đọc output JSON, mỗi lỗi một dòng `[SEVERITY] file:line InspectionId - message` |
| `language-inspection.xml` | Inspection profile, cấu hình y như trong PhpStorm |

## Cài đặt

1. Cài **PhpStorm** và kích hoạt license (đã có thì bỏ qua). Script tự tìm PhpStorm ở `C:\Program Files\JetBrains\PhpStorm*`, `%LOCALAPPDATA%\Programs\PhpStorm*` (Toolbox), `/Applications/PhpStorm*.app` và `~/Applications`. Nếu cài ở chỗ khác thì set `PHPSTORM_INSPECT=<đường dẫn tới bin/inspect.bat hoặc inspect.sh>`.
2. Cài **Python 3**.
3. Trên Windows chạy bằng **Git Bash**.

Lần chạy đầu mất khoảng 1 phút để khởi tạo. Các lần sau nhanh hơn nhờ cache index ở `~/.cache/phpstorm-inspect` (đổi bằng `PHPSTORM_INSPECT_HOME`).

Chạy được cả khi PhpStorm đang mở: script dùng config/system dir riêng và copy `phpstorm.key` từ config của PhpStorm sang.

## Chạy

```bash
# Chỉ file có thay đổi chưa commit (mặc định cho agent)
tools/jetbrains/phpstorm-inspect.sh <project-dir> -changes

# Một thư mục
tools/jetbrains/phpstorm-inspect.sh <project-dir> -d app/Services

# Toàn project
tools/jetbrains/phpstorm-inspect.sh <project-dir>
```

- `-changes` chỉ lấy file git đang track (modified/staged). File mới tạo thì chạy `git add -N <file>` trước.
- `-changes` báo lỗi của **cả file** có thay đổi, không chỉ những dòng đã sửa.
- Kết quả JSON thô nằm ở `$TMPDIR/phpstorm-inspect/<tên-project>/`.
- Lỗi trong `vendor/`, `node_modules/`, `storage/` bị lọc khỏi output.
- Nếu project chưa có `.idea/`, PhpStorm sẽ tạo tạm, script xóa đi sau khi chạy xong.

## Cấu hình inspection giống PhpStorm

`language-inspection.xml` dùng đúng format inspection profile của PhpStorm. Có 2 cách chỉnh:

- **Export từ IDE:** PhpStorm → Settings → Editor → Inspections → ⚙ → *Export*, rồi ghi đè file này. Agent sẽ chạy đúng bộ rule bạn đang thấy trong IDE.
- **Sửa tay:** mỗi dòng ghi đè một inspection, inspection nào không ghi thì giữ mặc định của PhpStorm:
  ```xml
  <inspection_tool class="PhpUnused" enabled="false" level="WEAK WARNING" enabled_by_default="false" />
  <inspection_tool class="PhpUnusedLocalVariableInspection" enabled="true" level="WARNING" enabled_by_default="true" />
  ```
  `class` là `InspectionId` in ra ở mỗi dòng kết quả.

Profile hiện tại tắt sẵn 3 inspection hay gây nhiễu:
- `PhpUnused`: với Laravel thì controller, job, listener nào cũng bị báo "never instantiated".
- `SpellCheckingInspection`: kiểm tra chính tả.
- `GrazieInspection`: kiểm tra ngữ pháp.

Nếu bạn export profile mới từ IDE, nhớ tắt lại 3 cái này.

Plugin cài thêm trong PhpStorm (ví dụ *Php Inspections (EA Extended)*) không tự có trong bản inspect vì nó dùng plugin dir riêng. Muốn dùng thì copy plugin vào `~/.cache/phpstorm-inspect/config/plugins/`.

## Lỗi thường gặp

| Triệu chứng | Cách xử lý |
|-------------|-----------|
| `Không tìm thấy PhpStorm` | Set `PHPSTORM_INSPECT` |
| `Cảnh báo: không thấy phpstorm.key` / bị treo | Mở PhpStorm, kích hoạt license, chạy lại |
| `-changes` ra 0 lỗi dù có sửa file mới | `git add -N <file>` |
| Hàng loạt lỗi `Undefined class` | Chạy `composer install` trong project |
