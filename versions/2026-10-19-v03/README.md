# FootballTrack — v03 — 19/10/2026

Lưu ngày 19/10/2026: hoàn thành bài lấy mẫu frame được giao cho ngày 18/10 và thử detection pretrained. Bản chụp giữ nguyên code của người học, không sửa implementation khi lưu.

## Thêm và thay đổi so với v02

- `test1.py`: dùng `frame_interval` cho điều kiện chia dư và tên thư mục đầu ra; cấu hình hiện tại là 60.
- Dừng sau khi đọc 300 frame; chờ 15 ms thay vì chờ phím ở mỗi frame.
- Kiểm tra giá trị trả về của `imwrite` và in thông báo thành công/thất bại.
- Chuẩn bị thư mục lấy mẫu every_15, every_30, every_60 và thư mục kết quả cho YOLO11n/YOLO11s. YOLO11s mới có thư mục, chưa được chạy so sánh.
- Thêm `src/detection/test_img.py`: nạp YOLO11n một lần, duyệt ảnh theo số frame, chỉ dự đoán lớp person, vẽ và lưu kết quả.
- Detection chạy CPU với conf=0.25, imgsz=640; bỏ qua output đã tồn tại; kiểm tra kiểu Results trước khi dùng plot.

## Không còn / giữ nguyên

- Không còn cố định khoảng lấy mẫu và tên thư mục ở số 30 trong `test1.py`.
- Không còn gọi `imwrite` hai lần cho cùng ảnh như bản trung gian trong buổi học.
- Giữ các version cũ và toàn bộ dữ liệu trên máy. Không xóa file dự án.
- Không đưa video, ảnh sinh ra hoặc trọng số lên GitHub; chỉ lưu các `.gitkeep` để giữ cấu trúc thư mục.

## Kết quả kiểm tra tại thời điểm lưu

- every_15: 20 ảnh; every_30: 10 ảnh; every_60: 5 ảnh.
- YOLO11n/every_30: 10 ảnh kết quả. Đây là kiểm tra sự hiện diện của file, chưa phải đánh giá độ chính xác detection.
- Log người học cung cấp cho frame 30: 14 detection person; chưa xác minh bằng nhãn chuẩn.
- Cú pháp của hai file nguồn và hai bản chụp hợp lệ qua ast.parse.
- SHA256 của mỗi bản chụp khớp file nguồn.
- Chưa chạy lại inference/GUI trong terminal của trợ lý.

## Các điểm còn lại

- Detection còn một vòng while duyệt chỉ số thừa trước vòng for thực hiện xử lý.
- Nhấn q trong detection sẽ thoát trước khi lưu ảnh đang xem.
- Output đã tồn tại bị bỏ qua theo tên file; đổi model hoặc cấu hình cần thư mục lần thử riêng để không dùng nhầm kết quả cũ.
- Script lấy frame chưa tự tạo thư mục cho một giá trị frame_interval mới.
- Chưa có nhãn chuẩn, precision/recall/mAP/confusion matrix hoặc kết luận model tốt nhất.

## Chạy từ thư mục gốc FootBallTrack

```powershell
python versions/2026-10-19-v03/test1.py
python versions/2026-10-19-v03/src/detection/test_img.py
```

Cần Python có OpenCV, NumPy, Ultralytics cùng các dependency; video ở `raw/data/test.mp4`, trọng số ở `models/yolo11n.pt`. Detection dùng ảnh ở `outputs/frames/every_30/` và lưu vào `outputs/detection/yolo11n/every_30/`.
