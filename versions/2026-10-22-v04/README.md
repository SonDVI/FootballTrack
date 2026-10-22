# FootballTrack v04

Lưu ngày 22/10/2026, tổng hợp tiến độ từ commit v03 ngày 19/10. Bản lưu giữ nguyên code hiện tại, chưa sửa implementation trong quá trình lưu version.

## Đã thêm

- `src/detection/measure_speed.py`: đo preprocess, inference, postprocess và tổng thời gian xử lý từng ảnh; warm-up một lần; xuất CSV từng ảnh và trung bình. Có tham số chọn YOLO11n/YOLO11s và interval 15/30/60; chạy CPU, không mở GUI.
- `src/video/video_detect.py`: nạp YOLO11n một lần, đọc liên tiếp frame từ video, chạy detection trực tiếp trên mảng ảnh, vẽ kết quả và hiển thị; hết video hoặc nhấn q thì thoát.
- `docs/detection_model_comparison.md`: tổng hợp đánh giá từ Word, phạm vi chỉ cầu thủ gồm thủ môn, bảng lỗi từng frame, so sánh tốc độ, giới hạn và quyết định chọn YOLO11n làm baseline trên CPU.
- `docs/benchmarks/2026-10-20/clean_speed.csv`: bản sao số đo trên ảnh sạch, giữ trong Git để số liệu báo cáo không chỉ tồn tại dưới outputs bị ignore.
- Profile terminal VS Code FootballTrack (Conda), dùng Command Prompt để kích hoạt footballtrack_env trên máy hiện tại; interpreter Python của dự án trỏ vào cùng môi trường.

## Đã thay đổi và loại bỏ

- `test_img.py`: dùng model_name cho cả trọng số và output; tránh nạp model s nhưng lưu nhầm vào thư mục n.
- Dùng bộ input sạch riêng và output `outputs/detection/{model_name}/clean_every_30/`; có 10 ảnh kết quả/model tại thời điểm lưu.
- Bỏ vòng while duyệt chỉ số thừa, giữ vòng for chạy detection.
- Sửa các lỗi ở bản video trong quá trình học: đường dẫn đầu vào, source=img thay vì str(img), __main__, gọi destroyAllWindows(), thống nhất tên cửa sổ để resize đúng.
- Sửa lỗi cộng trong trao đổi trước: tổng đúng là 76 lượt cầu thủ qua 10 ảnh, không phải 85; không phải 76 danh tính khác nhau.
- Không xóa các version cũ hoặc dữ liệu gốc. Không tự sửa code nguồn khi chụp version này.

## Đánh giá đã đạt

- Theo Word: n có 8 lượt bỏ sót, 1 Wrong Box, 6 Duplicate Box, 1 lỗi định vị; s tương ứng 7, 1, 6, 0.
- Đo lại ảnh sạch trên CPU, ba lượt sau warm-up: tổng xử lý trung bình n khoảng 47,37 ms/ảnh, s khoảng 121,51 ms/ảnh. Đây không phải FPS toàn pipeline; tải máy chưa được kiểm soát.
- Chọn n làm baseline nhờ tốc độ trong các lần đo và chất lượng quan sát gần nhau trên bộ ảnh nhỏ. Chưa kết luận model có accuracy tốt nhất; chưa có annotation box chuẩn hoặc mAP.
- Đã kiểm tra trước khi lưu: cú pháp Python; lần kiểm tra video trước đó xử lý và vẽ thành công ba frame không GUI. Chưa xác nhận toàn bộ thao tác cửa sổ GUI hoặc xử lý hết video.

## Phần chưa hoàn thiện

- Video hiện chỉ hiển thị, chưa ghi VideoWriter và chưa giới hạn 300 frame.
- frame_choose=30 trong video đang là delay chờ phím 30 ms; không phải khoảng lấy mẫu. Tên biến còn dễ gây nhầm.
- Video còn tạo thư mục output nhưng chưa ghi kết quả vào đó; fps, width, height đã đọc nhưng chưa dùng để ghi video.
- Nếu mở video thất bại chưa có thông báo lỗi riêng; xử lý lỗi và cleanup khi có exception chưa hoàn chỉnh.
- Trong test_img.py, nhấn q thoát trước khi lưu ảnh đang xem; output tồn tại bị bỏ qua theo tên, chưa xét model/config thay đổi.
- Lớp person vẫn bao gồm trọng tài/cổ động viên; chưa lọc chỉ cầu thủ hoặc tracking giữ ID.
- Cấu hình .vscode chứa đường dẫn riêng của máy; phải điều chỉnh khi dùng trên máy khác. Chưa có manifest dependency được chốt phiên bản.

## Chạy các script

Chạy từ thư mục gốc FootBallTrack trong môi trường có OpenCV, NumPy và Ultralytics, ví dụ footballtrack_env hiện tại. Video, trọng số và ảnh cần chuẩn bị lại nếu clone repo vì chúng không được commit.

```cmd
python src/detection/test_img.py
python src/detection/measure_speed.py --model yolo11n --interval 30
python src/video/video_detect.py
```

Code snapshot giữ cùng đường dẫn tương đối tới dữ liệu của dự án. Riêng measure_speed.py suy ra root từ vị trí file; hãy chạy bản trong src/ để dùng dữ liệu dự án, hoặc khôi phục cấu trúc snapshot thành project root trước khi chạy bản archive.

## Tiếp theo

Xác nhận cửa sổ và phím q hoạt động; giới hạn clip thử; thêm ghi video vào outputs/videos/ và kiểm tra kích thước, FPS, khả năng mở file. Sau đó mới làm lọc phạm vi hoặc tracking.
