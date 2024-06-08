# Tracking-tools-for-Community-Call
SuperteamVN đang tìm kiếm nhà phát triển có khả năng xây dựng ứng dụng cho phép thống kê hoạt động của các thành viên trên Discord.

# Tên dự án
Project Name:
Tracking-tool-for-Community-Call
SuperteamVN đang tìm kiếm nhà phát triển có khả năng xây dựng ứng dụng cho phép thống kê hoạt động
của các thành viên trên Discord.

Discord Application ID:
1247074685217407098

PUBLIC KEY:
4d554519c10716e491424566755c4518a240aaa1815d1a7ace6109c347649c1f

## Cách triển khai

1. **Clone repo:**

    ```bash
    git clone https://github.com/natnguyen0852/Tracking-tool-for-Community-Call
    cd Tracking-tool-for-Community-Call
    ```

2. **Cài đặt các phụ thuộc:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Cấu hình môi trường:**

    Mô tả cách cấu hình môi trường, file json đã được upload lên Render.com

4. **Chạy dự án:**

    ```bash
    python main.py
    ```

## Cách sử dụng

Người dùng đăng nhập bằng tài khoản Discord.

Thông tin các thành viên khi họ tham gia các cuộc gọi cộng đồng theo thời gian thực, 
sẽ được ghi nhận vào Google Sheet, thông qua Google Cloud Console, bao gồm: 
+ Thời gian tham gia Stage.
+ Thời gian rời khỏi Stage.

Sử dụng Google Sheets làm database.

Cho phép xuất dữ liệu theo khoảng thời gian nhất định ra Google Sheets.

Đã config thành công để có thể deploy lên https://render.com/
