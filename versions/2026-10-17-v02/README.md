# FootballTrack — v02 — 2026-10-17

Bản chụp nguyên trạng `test1.py` cuối buổi học ngày 17/10/2026, tiếp nối `2026-10-16-v01`.

## Đã thêm

- Tạo cửa sổ có thể thay đổi kích thước bằng `namedWindow` và `WINDOW_NORMAL`; đặt kích thước hiển thị 640 × 360 bằng `resizeWindow`.
- Biến `frame_count` tăng sau mỗi lần đọc frame thành công.
- Đặt tên ảnh `outputs/frames/1_frame.jpg`, `2_frame.jpg`, ... bằng f-string.
- Dùng `pathlib.Path.exists()` để chỉ ghi ảnh khi đường dẫn chưa tồn tại.
- Gọi `cap.release()` và `cv2.destroyAllWindows()` sau vòng lặp, trong khối mở video thành công.
- Thêm chú thích giải thích các bước trong code.

## Đã thay đổi và bỏ

- Mở rộng từ bài xem video sang xem và xuất từng frame thành ảnh.
- Bỏ cách dùng biến cờ `frame_saved` để chỉ lưu một ảnh. Đây là thay đổi trong quá trình học hôm nay; bản v01 chưa có phần lưu ảnh này.
- Không xóa file dự án hoặc phiên bản cũ.
- Giữ `waitKey(0)` để tiến từng frame bằng phím; chưa chuyển sang tự phát theo FPS.

## Hành vi cần nhớ

- Nhấn một phím trong cửa sổ video để tiếp tục; `waitKey(0)` không có nghĩa phải nhấn phím số 0. Chú thích ở dòng này trong code còn diễn đạt sai.
- Lệnh lưu ảnh nằm sau `waitKey(0)`, nên frame hiện tại được kiểm tra/lưu sau khi nhấn phím, kể cả khi phím đó là `q`; sau đó chương trình mới kiểm tra thoát.
- Bỏ qua theo tên file tồn tại, chưa so sánh nội dung hoặc kiểm tra file đó có phải ảnh hợp lệ. Khi chạy lại vẫn đọc video từ đầu.
- Khi đổi video đầu vào, cần thư mục đầu ra riêng hoặc quy ước tên riêng để tránh bỏ qua ảnh do trùng tên.
- Chưa kiểm tra giá trị trả về của `imwrite`; thư mục `outputs/frames/` phải tồn tại.
- Thu nhỏ cửa sổ không thay đổi kích thước ảnh gốc được lưu.

## Xác minh

- Đã phân tích cú pháp Python bằng `ast.parse`: hợp lệ.
- Đã so sánh SHA256: bản chụp trùng với file nguồn tại thời điểm lưu.
- Người học xác nhận đã lưu ảnh thành công trong buổi học.
- Chưa chạy lại GUI hoặc kiểm tra đọc ảnh bằng OpenCV trong terminal: Python đang được terminal chọn thiếu module `cv2`.
- Video đầu vào và ảnh sinh ra ở lại máy, được `.gitignore` loại khỏi commit.

## Chạy lại từ thư mục gốc dự án

```powershell
python versions/2026-10-17-v02/test1.py
```

Chọn môi trường Python có `cv2`, `numpy`, chuẩn bị video `raw/data/test.mp4` và thư mục `outputs/frames/`.

## Bước học tiếp theo

- Sửa cách diễn đạt chú thích `waitKey(0)` và kiểm tra kết quả trả về của `imwrite`.
- Thực hành phát liên tục với thời gian chờ dương, rồi chọn chỉ lưu một số frame để giảm dung lượng.
