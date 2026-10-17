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
