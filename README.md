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
    └── 2026-10-17-v02/
```

Các file `.gitkeep` chỉ giúp Git giữ lại thư mục trống, không phải code xử lý.

## Tiến độ ngày 17/10/2026

`test1.py` hiện hiển thị video trong cửa sổ 640 × 360, chờ phím ở mỗi frame bằng `waitKey(0)`, và lưu ảnh theo số thứ tự vào `outputs/frames/`. Đường dẫn ảnh đã tồn tại sẽ được bỏ qua; chương trình vẫn đọc video từ đầu. Đã thêm giải phóng nguồn video và đóng cửa sổ sau vòng lặp.

Xem [ghi chú v02](versions/2026-10-17-v02/README.md) để biết thay đổi, giới hạn và cách chạy bản lưu. Chưa triển khai detection hoặc tracking.

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

Hiện cấu trúc này chưa có implementation detection/tracking và chưa xác nhận môi trường chạy. Chưa tạo danh sách dependency hoặc chốt phiên bản thư viện; bổ sung khi thiết lập môi trường và kiểm tra thực tế.

## Quy ước

- Giữ video gốc trong `raw/data/`; ghi sản phẩm sinh ra vào `outputs/`.
- Đặt trọng số mô hình trong `models/`.
- Chạy các bài thực hành từ thư mục gốc dự án để đường dẫn tương đối nhất quán.
- Ghi mỗi thử nghiệm có ý nghĩa vào `docs/experiment_log.md`.
- Video, trọng số mô hình, kết quả sinh ra và môi trường Python được bỏ qua bởi Git. Bỏ qua bởi Git không xóa file trên máy và không bỏ theo dõi file đã được commit trước đó.
