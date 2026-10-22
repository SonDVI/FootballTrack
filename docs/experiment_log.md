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

## 20–22/10/2026 — So sánh model và detection trực tiếp trên video

- Thêm measure_speed.py để đo ảnh tự động theo model/interval, warm-up rồi xuất CSV. Lưu bản sao CSV đo lại trên ảnh sạch trong docs/benchmarks/2026-10-20/clean_speed.csv.
- Chọn bộ every_30 cho thử nghiệm ban đầu; không coi interval là tham số làm mỗi ảnh inference nhanh hơn. Video gốc 25 FPS.
- Phát hiện ảnh đầu vào frame 30 đã có box; lấy lại input sạch vào thư mục comparison riêng, không ghi đè dữ liệu cũ.
- Đánh giá thủ công theo Word: chỉ cầu thủ nhìn thấy, gồm thủ môn. n/s có 8/7 lượt bỏ sót, 1/1 Wrong Box, 6/6 Duplicate Box, 1/0 lỗi định vị; cùng 76 lượt cầu thủ mục tiêu.
- Sửa tổng 85 từng báo trong chat thành 76 theo phép cộng bảng. Chi tiết và giới hạn ở detection_model_comparison.md.
- Chọn YOLO11n làm baseline CPU; phép đo lại ảnh sạch ba lượt có tổng xử lý trung bình khoảng 47,37 ms cho n, 121,51 ms cho s; chưa tính accuracy/mAP hoặc kiểm soát trạng thái máy.
- test_img.py dùng model_name nhất quán, input sạch, output riêng; bỏ while thừa. Mỗi model có 10 ảnh trong clean_every_30 tại thời điểm lưu.
- VS Code được cấu hình interpreter và profile terminal Conda cho footballtrack_env; đường dẫn riêng máy cần đổi trên máy khác.
- Thêm video_detect.py: đọc frame, chạy YOLO11n và plot trực tiếp, hiển thị cửa sổ thống nhất tên; q/hết video thì thoát. Chưa ghi video và chưa giới hạn frame.
- Kiểm tra trước lưu: cú pháp hợp lệ; ba frame video đã inference/plot thành công trong phép thử không GUI. Chưa kiểm tra toàn bộ GUI hoặc toàn video.
- Bản lưu v04 ngày 22/10 giữ nguyên implementation. Bước tiếp: xác nhận cửa sổ, thêm giới hạn clip và VideoWriter.
