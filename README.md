# 🛠️ Quy trình ETL bằng Python

## 📌 Tổng quan

Dự án này trình bày một quy trình ETL (Extract, Transform, Load) hoàn chỉnh được xây dựng bằng Python trên nền Google Colab.

Quy trình kết nối với nhiều nguồn dữ liệu khác nhau bao gồm Google Sheets, file Excel, CSV, bảng HTML và cơ sở dữ liệu MySQL. Script sẽ tự động tải, xử lý, làm sạch và chuẩn bị dữ liệu để phân tích hoặc báo cáo.

Mục tiêu là thực hành tự động hóa toàn bộ quy trình ETL, đảm bảo khả năng tái sử dụng và thể hiện cách xử lý dữ liệu thực tế bằng các công cụ mã nguồn mở.

---

## 📂 Nguồn dữ liệu sử dụng

| Nguồn | Mô tả | Định dạng |
|-------|------|-----------|
| [Dữ liệu Enrollies](https://docs.google.com/spreadsheets/d/1VCkHwBjJGRJ21asd9pxW4_0z2PWuKhbLR3gUHm-p4GI) | Thông tin cơ bản như tên, thành phố, giới tính từ biểu mẫu đăng ký | Google Sheets |
| [Trình độ học vấn](https://assets.swisscoding.edu.vn/company_course/enrollies_education.xlsx) | Trình độ học vấn, ngành học, tình trạng đại học | Excel |
| [Kinh nghiệm làm việc](https://assets.swisscoding.edu.vn/company_course/work_experience.csv) | Số năm kinh nghiệm, loại hình công ty, thời gian đổi việc gần nhất | CSV |
| Chỉ số phát triển thành phố | Chỉ số tham khảo từ website | Bảng HTML |
| Giờ học đào tạo | Lấy từ hệ thống LMS (MySQL) | Bảng SQL |
| Trạng thái việc làm | Xác định sinh viên đã được tuyển sau khóa học | Bảng SQL |

⚠️ Các file **không được lưu trữ nội bộ**. Thay vào đó, chúng được tải trực tiếp khi chạy chương trình thông qua URL hoặc truy vấn cơ sở dữ liệu.

---

## 🔁 Mô tả quy trình ETL

1. **Extract (Trích xuất)**
   - Kết nối và tải dữ liệu từ:
     - Google Sheet (bằng URL)
     - Excel/CSV từ internet
     - MySQL bằng SQLAlchemy + PyMySQL
     - Trang web HTML bằng `pandas.read_html()`

2. **Transform (Chuyển đổi)**
   - Đổi tên cột, làm sạch dữ liệu
   - Xử lý giá trị thiếu (NaN, định dạng lỗi)
   - Chuẩn hóa dữ liệu dạng phân loại
   - Gộp các bảng theo `enrollee_id`
   - Tạo đặc trưng mới phục vụ phân tích

3. **Load (Tải vào)**
   - Kết quả là một DataFrame sạch đã xử lý
   - Có thể lưu ra `.csv`, chèn vào database hoặc dùng trực tiếp để phân tích

---

## 🧰 Công nghệ sử dụng

- `pandas`
- `requests`
- `openpyxl`
- `sqlalchemy`
- `PyMySQL`
- Google Colab / Jupyter

---

## 🎯 Mục tiêu

Dự án này được xây dựng với mục tiêu thực hành bài học ETL trong khoá học Data Science. Mô phỏng một tình huống thực tế nơi dữ liệu đến từ nhiều nguồn, cần được xử lý và hợp nhất để phục vụ cho việc phân tích hoặc ra quyết định.

---

