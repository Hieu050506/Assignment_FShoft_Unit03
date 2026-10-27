import re


def tach_tu(noi_dung):
    """Chuyển về chữ thường và tách từ, bỏ dấu câu."""
    return re.findall(r"\w+", noi_dung.lower())


def dem_tu(noi_dung):
    """Đếm tổng số từ trong nội dung."""
    return len(tach_tu(noi_dung))


def tao_tu_dien(noi_dung):
    """Tạo dictionary lưu mỗi từ và số lần xuất hiện của từ đó."""
    tu_dien = {}
    for tu in tach_tu(noi_dung):
        tu_dien[tu] = tu_dien.get(tu, 0) + 1
    return tu_dien
