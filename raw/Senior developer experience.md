Đây là các kinh nghiệm của tôi trong quá trình phát triển các phần mềm, ứng dụng, website,.. mà tôi có. Chúng có thể ứng dụng với các AI agent  xuyên suốt quá trình làm việc.
### 1. Deployment checklist

Khi giao 1 task lớn cho các AI Agent code các tasks khi chúng hoàn thành công việc của mình cần có 1 "hook" nhắc nhở người dùng, bạn có cần 1 file deploy checklist không?

Việc này giúp người gian task lắm bắt các công việc họ phải làm trước và sau khi merge code vào staging/production.

Việc generate checklist khá quan trọng việc hỏi người dùng xem liệu project có CICD chưa? CICD đã lo liệu các công việc gì rồi, -tôi sẽ phải làm tay các công việc gì?

Thường sẽ bỏ qua các công việc như:
- Migration
- Build application
- ....
Các việc này hầu hết đã được CICD lo liệu nên chỉ list ra những công việc thực sự cần làm bằng tay như:
- Chạy command 1 lần
- Deploy với tham số đặc biệt
- Lấy secret key từ 1 bên thứ 3
- ....

=> Vì vậy Agent phải hỏi lại các câu hỏi:
- Project này có CICD không?
- Nếu có rồi thì nó đã làm những gì
	- Các câu trả lời của người sẽ được lưu vào trong CLAUDE.MD để lần sau không hỏi lại

Một format chuẩn cho việc này bao gồm:
1. Tên file: `[Dev-checklist]-Ten-task.md`
2. Content format:

Bắt đầu với bảng tóm tắt
```md
| Việc cần làm | Lý do (Ngắn gọn) | Ưu tiên |
|--------------|------------------|---------|
|              |                  |         |
|              |                  |         |
|              |                  |         |
```

Tiếp tục với nội dung chi tiết
```
1. Việc 1
- Ưu tiên
- Công việc cần làm
- Lý do làm việc này
```

### 2. QA quick checklist

Khi phải hotfix một tính năng hoặc fix sau khi scan security,... với các công việc xuất phát từ dev tự fix không đến từ 1 task cụ thể thì cần có 1 file để QA có thể lắm bắt được các phần việc mà dev đã làm và cần test các tính năng nào liên quan.

Ví dụ: Shopify yêu cầu các app sử dụng Shopify AI toolkit security để scan toàn bộ project xem có dính lỗi bảo mật nào không. Sau khi đã scan xong và trả về 1 danh sách các tính năng dính lỗi, dev thực hiện fix trên các báo cáo đó nhưng QA đọc thì không hiểu ngôn ngữ của dev. Vì vậy cần có 1 file trung gian giúp QA hiểu được Shopify yêu cầu gì? Dev đã làm những gì? QA cần test gì?

Việc này cũng cần phải hỏi dev trước khi generate file.