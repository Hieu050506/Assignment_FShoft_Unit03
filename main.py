from pathlib import Path

from utils.file_utils import doc_file, ghi_file
from utils.word_utils import dem_tu, tao_tu_dien


def main():
    # Lấy thư mục chứa main.py để tìm đúng data.txt khi chạy ở nơi khác.
    thu_muc = Path(__file__).resolve().parent
    noi_dung = doc_file(thu_muc / "data.txt")

    if noi_dung is None:
        return

    so_tu = dem_tu(noi_dung)
    tu_dien = tao_tu_dien(noi_dung)

    print("Nội dung file:")
    print(noi_dung)
    print(f"Tổng số từ: {so_tu}")
    print("Từ điển tần suất:")
    print(tu_dien)

    # Ghép kết quả thành chuỗi để ghi ra file.
    ket_qua = f"Tổng số từ: {so_tu}\nTừ điển tần suất:\n"
    for tu, so_lan in tu_dien.items():
        ket_qua += f"{tu}: {so_lan}\n"

    file_ket_qua = thu_muc / "ket_qua.txt"
    if ghi_file(file_ket_qua, ket_qua):
        print(f"Đã ghi kết quả vào: {file_ket_qua}")


if __name__ == "__main__":
    main()
