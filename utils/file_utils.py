def doc_file(duong_dan):
    """Đọc file văn bản và trả về nội dung dưới dạng chuỗi."""
    try:
        with open(duong_dan, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Không tìm thấy file: {duong_dan}")
    except UnicodeError as loi:
        print(f"Không đọc được nội dung UTF-8: {loi}")
    except OSError as loi:
        print(f"Lỗi khi đọc file: {loi}")
    return None


def ghi_file(duong_dan, noi_dung):
    """Ghi nội dung vào file; trả về True nếu ghi thành công."""
    try:
        with open(duong_dan, "w", encoding="utf-8") as file:
            file.write(noi_dung)
        return True
    except FileNotFoundError:
        print(f"Không tìm thấy thư mục để ghi file: {duong_dan}")
    except UnicodeError as loi:
        print(f"Không ghi được nội dung UTF-8: {loi}")
    except OSError as loi:
        print(f"Lỗi khi ghi file: {loi}")
    return False
