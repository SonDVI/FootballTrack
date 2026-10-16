# FootballTrack — v01 — 2026-10-16

Bản chụp nguyên trạng `test1.py` khi kết thúc ngày 16/10/2026. Không sửa code trong quá trình lưu phiên bản.

## Đã triển khai trong code

- Mở video `raw/data/test.mp4` bằng OpenCV.
- Lấy FPS, chiều rộng và chiều cao của video.
- Đọc từng frame, dừng khi đọc thất bại.
- Hiển thị frame và kiểm tra phím `q` để thoát vòng lặp.
- Dùng `waitKey(0)`: chờ người dùng nhấn phím sau mỗi frame.

## Đã trao đổi

- Ý nghĩa `VideoCapture`, `read`, `imshow`, `waitKey`.
- Phân biệt FPS gốc, thời gian chờ và FPS xử lý thực tế.

## Phần tiếp theo

- Thêm `cap.release()` và `cv2.destroyAllWindows()` sau khối xử lý, không thụt lề.
- Dùng thời gian chờ dương nếu muốn phát video liên tục.
- Thực hành lưu một frame vào `outputs/frames/`.

## Cách chạy lại từ thư mục gốc FootBallTrack

```powershell
python versions/2026-10-16-v01/test1.py
```

Cần môi trường có `cv2`, `numpy` và video gốc tại `raw/data/test.mp4`. Video không được sao chép vào phiên bản này.

Đã kiểm tra bản sao có cùng SHA256 với file nguồn tại thời điểm lưu. Chưa chạy xác nhận hành vi cửa sổ hoặc phím bấm; đây là mốc lưu tiến độ, chưa phải bản hoàn thiện.
