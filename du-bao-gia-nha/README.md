# Dự Báo Giá Nhà

Dự án máy học đơn giản giúp dự báo giá nhà dựa trên các thông tin cơ bản bằng thuật toán **Hồi quy tuyến tính (Linear Regression)**.

## Các đặc trưng dữ liệu
- **DienTich**: Diện tích căn nhà (m²).
- **PhongNgu**: Số lượng phòng ngủ.
- **PhongTam**: Số lượng phòng tắm.
- **TuoiNha**: Tuổi của căn nhà (năm).
- **GiaNha**: Giá căn nhà (VNĐ) - Mục tiêu cần dự báo.

## Yêu cầu hệ thống
Đảm bảo bạn đã cài đặt Python, sau đó cài đặt các thư viện cần thiết bằng lệnh:

```bash
pip install pandas scikit-learn