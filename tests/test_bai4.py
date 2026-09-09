"""
Test Bai 4: Tinh so ngay cua mot thang
Phuong phap kiem thu: Hop den (Black-box Testing)
Ky thuat ap dung:
  - Phan lop tuong duong: thang 31 ngay, 30 ngay, thang 2
  - Phan tich gia tri bien: thang 1, 12, nam nhuan/thuong
  - Du lieu khong hop le
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.bai4_so_ngay_trong_thang import soNgayTrongThang, laNamNhuan


# -------------------------------------------------------------------
# NHOM 1: Du lieu hop le
# -------------------------------------------------------------------

class TestSoNgayTrongThangDuLieuHopLe:
    """Issue 1: Test case du lieu hop le"""

    def test_thang_co_31_ngay(self):
        """Lop tuong duong: cac thang co 31 ngay (1,3,5,7,8,10,12)"""
        assert soNgayTrongThang(1, 2024) == 31
        assert soNgayTrongThang(3, 2024) == 31
        assert soNgayTrongThang(7, 2024) == 31
        assert soNgayTrongThang(12, 2024) == 31

    def test_thang_co_30_ngay(self):
        """Lop tuong duong: cac thang co 30 ngay (4,6,9,11)"""
        assert soNgayTrongThang(4, 2024) == 30
        assert soNgayTrongThang(6, 2024) == 30
        assert soNgayTrongThang(9, 2024) == 30
        assert soNgayTrongThang(11, 2024) == 30

    def test_thang_2_nam_nhuan(self):
        """Lop tuong duong: thang 2 cua nam nhuan => 29 ngay"""
        assert soNgayTrongThang(2, 2024) == 29
        assert soNgayTrongThang(2, 2000) == 29

    def test_thang_2_nam_thuong(self):
        """Lop tuong duong: thang 2 cua nam thuong => 28 ngay"""
        assert soNgayTrongThang(2, 2023) == 28
        assert soNgayTrongThang(2, 1900) == 28

    def test_thang_1_gia_tri_bien_tren(self):
        """Gia tri bien: thang 1 (bien duoi hop le)"""
        assert soNgayTrongThang(1, 2024) == 31

    def test_thang_12_gia_tri_bien_duoi(self):
        """Gia tri bien: thang 12 (bien tren hop le)"""
        assert soNgayTrongThang(12, 2024) == 31

    def test_nam_nhuan_chia_het_4_khong_chia_het_100(self):
        """Lop tuong duong: nam nhuan thong thuong"""
        assert laNamNhuan(2020) == True

    def test_nam_nhuan_chia_het_400(self):
        """Lop tuong duong: nam nhuan dac biet chia het 400"""
        assert laNamNhuan(2000) == True

    def test_nam_thuong_chia_het_100_khong_chia_het_400(self):
        """Lop tuong duong: nam chia het 100 nhung khong chia het 400 => khong nhuan"""
        assert laNamNhuan(1900) == False


# -------------------------------------------------------------------
# NHOM 2: Du lieu khong hop le
# -------------------------------------------------------------------

class TestSoNgayTrongThangDuLieuKhongHopLe:
    """Issue 2: Test case du lieu khong hop le, bien, ngoai le"""

    def test_thang_0(self):
        """Gia tri bien: thang 0 (duoi bien hop le)"""
        with pytest.raises(ValueError):
            soNgayTrongThang(0, 2024)

    def test_thang_13(self):
        """Gia tri bien: thang 13 (tren bien hop le)"""
        with pytest.raises(ValueError):
            soNgayTrongThang(13, 2024)

    def test_thang_am(self):
        """Lop tuong duong khong hop le: thang am"""
        with pytest.raises(ValueError):
            soNgayTrongThang(-1, 2024)

    def test_nam_bang_0(self):
        """Gia tri bien: nam = 0"""
        with pytest.raises(ValueError):
            soNgayTrongThang(1, 0)

    def test_nam_am(self):
        """Lop tuong duong khong hop le: nam am"""
        with pytest.raises(ValueError):
            soNgayTrongThang(1, -2024)

    def test_thang_la_chuoi(self):
        """Ngoai le: kieu du lieu sai"""
        with pytest.raises(TypeError):
            soNgayTrongThang("thang1", 2024)

    def test_thang_la_so_thuc(self):
        """Ngoai le: so thuc khong phai so nguyen"""
        with pytest.raises(TypeError):
            soNgayTrongThang(1.5, 2024)

    def test_nam_la_bool(self):
        """Ngoai le: bool khong hop le"""
        with pytest.raises(TypeError):
            soNgayTrongThang(1, True)
