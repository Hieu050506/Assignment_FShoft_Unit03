# Bài tập xử lý file với package utils

Chạy từ thư mục `D:\BTap`:

```powershell
python .\nguyenbahieu_Unit03\main.py
```

Hoặc mở terminal trong thư mục `nguyenbahieu_Unit03` và chạy `python main.py`.

Nếu lệnh `python` hoặc `py` trên máy báo lỗi khởi động, dùng Python có sẵn trong workspace.
Chạy tại `D:\BTap`:

```powershell
& .\.validation-python\python.exe -X utf8 -c "import sys; sys.path.insert(0, 'nguyenbahieu_Unit03'); from main import main; main()"
```

- `data.txt`: nội dung đầu vào, có thể thay bằng văn bản của bạn (lưu UTF-8).
- `utils/__init__.py`: đánh dấu thư mục utils là package.
- `utils/file_utils.py`: hàm `doc_file` đọc văn bản, hàm `ghi_file` ghi văn bản.
- `utils/word_utils.py`: tách từ, đếm từ và tạo dictionary tần suất.
- `main.py`: import các hàm, đọc dữ liệu, xử lý và ghi `ket_qua.txt`.

Luồng chạy: `data.txt` → `doc_file` → `dem_tu`, `tao_tu_dien` → `ghi_file` → `ket_qua.txt`.

Từ được chuyển về chữ thường và tách bằng biểu thức `\w+`, bỏ dấu câu.
Mỗi phần được tách là một từ trong bài tập này; ví dụ `xin chào` được tính là 2 từ.
Dictionary lưu từ làm khóa, số lần xuất hiện làm giá trị. Ví dụ `python: 2`.

`doc_file` trả về `None` khi có lỗi; file rỗng vẫn trả về chuỗi rỗng hợp lệ.
`ghi_file` trả về `True` nếu thành công và `False` nếu có lỗi.
Các hàm dùng `try-except` để thông báo khi không tìm thấy file/thư mục hoặc gặp lỗi đọc/ghi.
Chế độ `w` tạo file kết quả nếu chưa có và ghi đè nội dung cũ nếu file đã có.
# Assignment_FShoft_Unit03
