# Nhật ký thử nghiệm

Ghi lại khi thay đổi dữ liệu, mô hình hoặc tham số để biết điều gì giúp kết quả tốt hơn.

## Mẫu cho mỗi lần thử

- Ngày:
- Mục tiêu / câu hỏi cần kiểm tra:
- Video và đoạn thời gian sử dụng:
- Phiên bản Python, thư viện và tên trọng số mô hình:
- Thay đổi so với lần trước:
- Kết quả quan sát được:
- Lỗi cụ thể và frame / thời điểm xảy ra:
- Đường dẫn sản phẩm trong `outputs/`:
- Kết luận và bước tiếp theo:

Ví dụ câu hỏi: Khi hai người chạy cắt ngang nhau, ID có bị đổi không?

## 17/10/2026 — Lưu frame theo số thứ tự

- Mục tiêu: xem từng frame, lưu nhiều ảnh riêng biệt và tránh ghi đè khi chạy lại cùng video.
- Đầu vào: `raw/data/test.mp4`.
- Thay đổi: cửa sổ 640 × 360; thêm bộ đếm, tên ảnh dạng `{frame_count}_frame.jpg`, kiểm tra `Path.exists()`, giải phóng tài nguyên sau vòng lặp; bỏ biến cờ lưu một lần trong quá trình học.
- Quan sát: người học xác nhận lưu ảnh thành công; lần kiểm tra trước trong buổi thấy 14 ảnh đánh số liên tục từ 1 đến 14. Cuối buổi có 31 file ảnh đánh số, không có file rỗng.
- Kiểm tra cuối buổi: cú pháp Python hợp lệ; chưa chạy lại OpenCV do môi trường Python của terminal thiếu `cv2`.
- Giới hạn: vẫn dùng `waitKey(0)`; bỏ qua theo tên file, không theo nội dung; chưa kiểm tra kết quả trả về của `imwrite`.
- Sản phẩm: ảnh trong `outputs/frames/` (không commit); code và ghi chú trong `versions/2026-10-17-v02/`.
- Tiếp theo: sửa chú thích `waitKey(0)`, kiểm tra ghi ảnh thành công và thử chỉ lưu những frame được chọn.

## 19/10/2026 — Hoàn tất bài 18/10 và thử detection

- Lấy mẫu cùng 300 frame đầu: every_15 có 20 ảnh, every_30 có 10 ảnh, every_60 có 5 ảnh. Code lấy frame hiện cấu hình interval=60, waitKey(15), kiểm tra kết quả ghi ảnh.
- Thêm thử nghiệm detection YOLO11n pretrained, CPU, conf=0.25, imgsz=640, classes=[0]. Nạp model một lần và duyệt ảnh theo số frame; bỏ qua output đã có.
- Đầu ra: 10 ảnh trong `outputs/detection/yolo11n/every_30/`; ảnh, video và trọng số không commit.
- Log người học: frame 30 có 14 detection person. Chưa có ground truth để kết luận độ chính xác.
- Validation: cú pháp Python hợp lệ; bản chụp khớp nguồn theo SHA256; chưa chạy lại model trong terminal của trợ lý.
- Giới hạn: while thừa trong detection; nhấn q thoát trước khi lưu ảnh đang xem; chưa so sánh YOLO11s hoặc tính metric.
- Bản lưu: `versions/2026-10-19-v03/`. Giữ nguyên implementation khi chụp version.
- Tiếp theo: xem và phân tích lỗi trên ảnh detection; chuẩn bị nhãn và bộ test chung trước khi so sánh model.
