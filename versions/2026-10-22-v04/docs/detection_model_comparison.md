# So sánh YOLO11n và YOLO11s cho FootballTrack

Ngày tổng hợp: 21/10/2026.

## Kết luận và quyết định hiện tại

Chọn **YOLO11n làm baseline để tiếp tục phát triển pipeline trên CPU**. Theo bảng quan sát thủ công của người học, YOLO11s bỏ sót ít hơn một lượt cầu thủ và có ít hơn một lỗi định vị; tổng box nhận nhầm và box trùng bằng nhau. Các lần đo tốc độ hiện có đều cho thấy YOLO11n nhanh hơn trên máy đang dùng.

Đây là lựa chọn ban đầu trên một bộ ảnh nhỏ, chưa phải kết luận YOLO11n có độ chính xác cao hơn hoặc tối ưu cho mọi video. Giữ YOLO11s để đối chiếu các tình huống khó.

## Nguồn và phạm vi

- Đánh giá chất lượng: hai bảng trong tài liệu `COMPARISON OF YOLO MODEL.docx` do người học cung cấp, đọc lại ngày 21/10/2026. File gốc ở ngoài repo, tại thư mục Desktop; không sao chép hoặc chỉnh sửa file Word.
- Phạm vi được người học ghi rõ: chỉ tính cầu thủ nhìn thấy trong ảnh, bao gồm thủ môn; không tính trọng tài, cổ động viên hoặc nhân viên ngoài sân.
- Gồm 10 ảnh mang số frame 30, 60, ..., 300. Tổng số lượt cầu thủ mục tiêu là **76**, không phải 76 người khác nhau.
- Bộ ảnh sạch dùng cho thử nghiệm hiện tại: `outputs/comparison/2026-10-20-yolo11n-vs-yolo11s/clean_test/inputs/`.
- Trọng số COCO pretrained nhận lớp `person`, chưa tự phân biệt cầu thủ với các vai trò khác. Phát hiện đúng một cổ động viên là đúng lớp person nhưng nằm ngoài phạm vi cầu thủ của bài đánh giá này.

Các số liệu chất lượng dưới đây được chép và cộng từ bảng Word; chưa được kiểm chứng lại từng box bằng nhãn chuẩn.

## Quy ước các cột

| Cột | Ý nghĩa |
| --- | --- |
| Frame | Số frame theo tên ảnh |
| Bỏ sót | Số cầu thủ mục tiêu xuất hiện nhưng chưa được phát hiện |
| Wrong Box | Số lỗi nhận nhầm do người học ghi nhận; cần tách người thật ngoài phạm vi khỏi vật thể bị nhận nhầm thành người |
| Duplicate Box | Số box thừa do cùng một người bị phát hiện nhiều lần |
| Localization error | Số lỗi box bao lệch theo quan sát thủ công; chưa có ngưỡng IoU chuẩn hóa |
| Cầu thủ mục tiêu | Số cầu thủ nhìn thấy do người học đếm, dùng chung cho hai model |

Trong bảng YOLO11s của Word, hai tiêu đề vẫn là `A symmetrical Box` và `Total Object`. Bản Markdown thống nhất chúng thành `Localization error` và `Cầu thủ mục tiêu` theo phạm vi đã chốt, không thay đổi số liệu.

Không cộng tất cả các cột lỗi thành một số false positive: một box định vị lệch có thể vẫn ứng với một cầu thủ, và có thể bị ghi nhận cùng một lỗi khác.

## Đánh giá thủ công YOLO11n

| Frame | Bỏ sót | Wrong Box | Duplicate Box | Localization error | Cầu thủ mục tiêu |
| --- | ---: | ---: | ---: | ---: | ---: |
| 30 | 1 | 0 | 2 | 1 | 13 |
| 60 | 1 | 0 | 1 | 0 | 14 |
| 90 | 1 | 0 | 0 | 0 | 12 |
| 120 | 1 | 0 | 1 | 0 | 10 |
| 150 | 1 | 0 | 1 | 0 | 8 |
| 180 | 2 | 0 | 0 | 0 | 8 |
| 210 | 1 | 0 | 1 | 0 | 8 |
| 240 | 0 | 1 | 0 | 0 | 1 |
| 270 | 0 | 0 | 0 | 0 | 1 |
| 300 | 0 | 0 | 0 | 0 | 1 |
| **Tổng** | **8** | **1** | **6** | **1** | **76** |

## Đánh giá thủ công YOLO11s

| Frame | Bỏ sót | Wrong Box | Duplicate Box | Localization error | Cầu thủ mục tiêu |
| --- | ---: | ---: | ---: | ---: | ---: |
| 30 | 0 | 0 | 1 | 0 | 13 |
| 60 | 1 | 0 | 1 | 0 | 14 |
| 90 | 1 | 0 | 0 | 0 | 12 |
| 120 | 1 | 0 | 1 | 0 | 10 |
| 150 | 1 | 0 | 1 | 0 | 8 |
| 180 | 2 | 0 | 0 | 0 | 8 |
| 210 | 1 | 0 | 2 | 0 | 8 |
| 240 | 0 | 1 | 0 | 0 | 1 |
| 270 | 0 | 0 | 0 | 0 | 1 |
| 300 | 0 | 0 | 0 | 0 | 1 |
| **Tổng** | **7** | **1** | **6** | **0** | **76** |

## Tổng hợp chất lượng

| Tiêu chí | YOLO11n | YOLO11s | Diễn giải |
| --- | ---: | ---: | --- |
| Bỏ sót | 8 | 7 | s ít hơn một lượt cầu thủ |
| Wrong Box | 1 | 1 | Bằng nhau theo bảng quan sát |
| Duplicate Box | 6 | 6 | Cả hai vẫn còn lỗi trùng |
| Localization error | 1 | 0 | s ít hơn một lỗi |

Khác biệt tập trung ở hai ảnh: frame 30 nghiêng về YOLO11s, còn frame 210 có hai box trùng ở s so với một ở n. Tám ảnh còn lại có các số đếm lỗi bằng nhau. Không dùng số box nhiều hơn hoặc confidence cao hơn làm bằng chứng duy nhất rằng một model tốt hơn.

## Tốc độ xử lý bổ sung

Số liệu phần này lấy từ báo cáo tốc độ trong dự án, **không phải từ bảng Word**.

Lần đối chiếu trên ảnh sạch ngày 20/10 dùng cùng 10 ảnh, CPU, conf=0.25, imgsz=640, classes=[0]. Mỗi model warm-up một lần, sau đó chạy ba lượt, tạo 30 phép đo/model.

| Tiêu chí trung bình | YOLO11n | YOLO11s |
| --- | ---: | ---: |
| Inference | 43,67 ms/ảnh | 116,68 ms/ảnh |
| Preprocess + inference + postprocess | 47,37 ms/ảnh | 121,51 ms/ảnh |

Nguồn: [CSV đo lại trên ảnh sạch được giữ trong repo](benchmarks/2026-10-20/clean_speed.csv), sao chép nguyên trạng ngày 22/10 từ `outputs/comparison/2026-10-20-yolo11n-vs-yolo11s/clean_test/speed.csv`.

YOLO11s mất khoảng 2,56 lần thời gian xử lý trung bình trong lần đối chiếu này. Hai model chạy lần lượt; tải CPU, nhiệt độ và xung nhịp chưa được kiểm soát. Thời gian trên không gồm đọc ảnh từ ổ đĩa, vẽ box, hiển thị, chờ phím hoặc lưu output; không coi nghịch đảo của nó là FPS toàn pipeline.

Để đối chiếu lịch sử, các CSV every_30 cũ báo tổng xử lý trung bình 29,41 ms/ảnh cho n và 87,76 ms/ảnh cho s. Đây là những lần chạy khác, không gộp trung bình với lần đo lại; chênh lệch giữa các lần cho thấy cần lưu điều kiện đo khi so sánh.

## Giới hạn và bước tiếp theo

- Mười ảnh từ một đoạn video ngắn chưa đại diện cho nhiều góc camera, ánh sáng và mức che khuất.
- Chưa có annotation bounding box chuẩn, quy tắc ghép một-một hoặc ngưỡng IoU để tính precision, recall và mAP đáng tin cậy. Chưa có đánh giá tracking.
- Cần thống nhất Wrong Box có bao gồm người thật ngoài phạm vi hay không; nếu có, ghi riêng lỗi lọc phạm vi.
- Giữ nguyên input sạch; lưu kết quả ở `outputs/detection/{model_name}/clean_every_30/`.
- Tiếp tục với YOLO11n baseline, đưa detection vào một đoạn video ngắn và quan sát lỗi qua các frame. Việc lọc chỉ cầu thủ và giữ ID là các bước sau.
- Khi mở rộng bộ test, thêm cảnh cầu thủ nhỏ, che khuất, ngã, camera lia và chuyển cảnh; đánh giá lại lựa chọn model dựa trên chất lượng cùng tốc độ.

Các ảnh và CSV nằm dưới `outputs/` hiện được Git bỏ qua. File tổng hợp và bản sao CSV đo lại nằm trong `docs/` để có thể commit cùng source code. Tổng 85 lượt cầu thủ từng nêu trong chat trước đó là lỗi cộng; số đúng theo cả hai bảng Word là **76**.
