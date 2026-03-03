# Tài liệu hướng dẫn sử dụng

## 1. Giới thiệu
Ứng dụng cho phép chọn tập tin nhị phân chứa các số thực (double, 8 bytes), sắp xếp tăng dần và minh họa quá trình sắp xếp.

## 2. Yêu cầu hệ thống
- Python 3.8 trở lên
- Thư viện Tkinter (có sẵn trong Python)

## 3. Hướng dẫn sử dụng
1. Chạy file `main.py`.
2. Nhấn "Chọn tập tin" để chọn file nhị phân chứa các số thực.
3. Dữ liệu sẽ hiển thị trên giao diện.
4. Nhấn "Sắp xếp và minh họa" để bắt đầu sắp xếp. Nếu file nhỏ (≤20 số), quá trình sắp xếp sẽ được minh họa từng bước.
5. Sau khi sắp xếp, nhấn "Lưu kết quả" để lưu file đã sắp xếp.

## 4. Lưu ý
- Ứng dụng chỉ hỗ trợ file nhị phân chứa số thực 8 bytes (double, IEEE 754).
- Nếu file lớn, chỉ hiển thị kết quả cuối cùng.
- File gen_sample_text.py có tác dụng tạo một file nhị phân tên là sample_data.bin chứa 10 số thực (kiểu double) được sinh ngẫu nhiên trong khoảng từ -100 đến 100 nhằm phục vụ cho việc tạo dữ liệu đầu vào cho file main.py nếu chưa có sẵn dữ liệu đầu vào. 
