# FootballTrack

Dự án học computer vision từng bước: đọc video bóng đá, phát hiện người trên sân, theo dõi ID và xuất kết quả.

## Cấu trúc

```text
FootBallTrack/
├── README.md
├── .gitignore
├── test1.py                # Bài thực hành đọc và hiển thị video hiện tại
├── raw/
│   └── data/               # Video đầu vào gốc
├── src/                    # Code sẽ được bổ sung khi học từng bước
│   ├── video/              # Đọc, ghi video và lấy thông tin frame
│   ├── detection/          # Phát hiện đối tượng, xử lý bounding box
│   ├── tracking/           # Theo dõi ID qua các frame
│   └── visualization/      # Vẽ box, ID và quỹ đạo lên frame
├── models/                 # Trọng số mô hình tải về hoặc huấn luyện
├── outputs/
│   ├── videos/             # Video kết quả
│   ├── frames/             # Ảnh frame để quan sát và kiểm tra lỗi
│   └── tracks/             # Dữ liệu tracking xuất ra CSV/JSON
├── docs/
│   └── experiment_log.md   # Nhật ký thử nghiệm và phân tích lỗi
└── versions/              # Bản chụp code và ghi chú theo buổi học
    ├── 2026-10-16-v01/
    ├── 2026-10-17-v02/
    └── 2026-10-19-v03/
```

Các file `.gitkeep` chỉ giúp Git giữ lại thư mục trống, không phải code xử lý.

## Tiến độ ngày 19/10/2026

`test1.py` hiện lấy mẫu theo `frame_interval`, lưu vào `outputs/frames/every_{frame_interval}/`, dừng sau 300 frame và dùng `waitKey(15)`. Giá trị hiện tại là 60. Đường dẫn ảnh đã tồn tại sẽ được bỏ qua; kết quả ghi ảnh được kiểm tra.

`src/detection/test_img.py` chạy YOLO11n trên các ảnh trong `outputs/frames/every_30/`, chỉ lấy lớp person và lưu ảnh có box vào `outputs/detection/yolo11n/every_30/`. Detection chờ phím từng ảnh, bỏ qua output đã có. Đã có 10 file kết quả tại thời điểm lưu; chưa đánh giá bằng nhãn chuẩn hoặc triển khai tracking.

Chạy từ thư mục gốc bằng `python src/detection/test_img.py`, trong môi trường có OpenCV và Ultralytics; cần trọng số `models/yolo11n.pt` và ảnh đầu vào trên máy. Xem [ghi chú v03](versions/2026-10-19-v03/README.md) để biết thay đổi, giới hạn và cách chạy bản lưu.

## Luồng dữ liệu dự kiến

`raw/data → video → detection → tracking → visualization → outputs`

Phần đọc video cung cấp từng frame. Detection trả về vị trí đối tượng trong frame; tracking gắn ID qua nhiều frame; visualization vẽ kết quả. Khi các phần chạy được, mới thêm chương trình điều phối chúng.

## Phạm vi bản đầu tiên

- Một clip ngắn, góc rộng, ít chuyển cảnh; xử lý offline.
- Phát hiện người trên sân và theo dõi ID trong cùng cảnh quay.
- Xuất video kết quả và dữ liệu vị trí để kiểm tra.
- ID tracking chưa phải số áo hoặc danh tính cầu thủ; kết quả phát hiện người có thể gồm trọng tài.

## Bắt đầu từ mã hiện tại

1. Hiểu `VideoCapture`, `ret`, `frame`, FPS và vòng lặp trong `test1.py`.
2. Đặt video đầu vào tại `raw/data/test.mp4` để khớp đường dẫn trong `test1.py`. Video gốc không được đưa lên GitHub.
3. Thực hành lưu một frame rồi ghi video đầu ra vào `outputs/`.
4. Sau đó mới bổ sung detection trên một ảnh, detection trên video và tracking.
5. Khi một phần đã hiểu và chạy được, chuyển phần đó vào thư mục tương ứng trong `src/`.

Đã có thử nghiệm detection pretrained trên ảnh; chưa triển khai tracking. Chưa tạo danh sách dependency hoặc chốt phiên bản thư viện, nên môi trường chưa được chuẩn hóa để tái lập trên máy khác.

## Quy ước

- Giữ video gốc trong `raw/data/`; ghi sản phẩm sinh ra vào `outputs/`.
- Đặt trọng số mô hình trong `models/`.
- Chạy các bài thực hành từ thư mục gốc dự án để đường dẫn tương đối nhất quán.
- Ghi mỗi thử nghiệm có ý nghĩa vào `docs/experiment_log.md`.
- Video, trọng số mô hình, kết quả sinh ra và môi trường Python được bỏ qua bởi Git. Bỏ qua bởi Git không xóa file trên máy và không bỏ theo dõi file đã được commit trước đó.
