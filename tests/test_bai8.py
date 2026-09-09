"""
Test Bai 8: Tinh tong S = 1! + 2! + 3! + ... + n!
Phuong phap kiem thu: Hop den (Black-box Testing)
Ky thuat ap dung:
  - Phan lop tuong duong: n nho, n lon
  - Phan tich gia tri bien: n = 1
  - Du lieu khong hop le
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.bai8_tong_giai_thua import tinhGiaiThua, tinhTongGiaiThua


# -------------------------------------------------------------------
# NHOM 1: Du lieu hop le
# -------------------------------------------------------------------

class TestGiaiThuaDuLieuHopLe:
    """Issue 1: Test ham giai thua - du lieu hop le"""

    def test_giai_thua_0(self):
        """Gia tri bien: 0! = 1"""
        assert tinhGiaiThua(0) == 1

    def test_giai_thua_1(self):
        """Gia tri bien: 1! = 1"""
        assert tinhGiaiThua(1) == 1

    def test_giai_thua_5(self):
        """Lop tuong duong: 5! = 120"""
        assert tinhGiaiThua(5) == 120

    def test_giai_thua_10(self):
        """Lop tuong duong: 10! = 3628800"""
        assert tinhGiaiThua(10) == 3628800


class TestTongGiaiThuaDuLieuHopLe:
    """Issue 1: Test tong giai thua - du lieu hop le"""

    def test_n_bang_1(self):
        """Gia tri bien: n = 1 => S = 1! = 1"""
        assert tinhTongGiaiThua(1) == 1

    def test_n_bang_2(self):
        """Lop tuong duong: n = 2 => S = 1! + 2! = 1 + 2 = 3"""
        assert tinhTongGiaiThua(2) == 3

    def test_n_bang_3(self):
        """Lop tuong duong: n = 3 => S = 1! + 2! + 3! = 1 + 2 + 6 = 9"""
        assert tinhTongGiaiThua(3) == 9

    def test_n_bang_4(self):
        """Lop tuong duong: n = 4 => S = 1 + 2 + 6 + 24 = 33"""
        assert tinhTongGiaiThua(4) == 33

    def test_n_bang_5(self):
        """Lop tuong duong: n = 5 => S = 1+2+6+24+120 = 153"""
        assert tinhTongGiaiThua(5) == 153

    def test_n_lon(self):
        """Lop tuong duong: n lon (n = 10)"""
        ketQua = tinhTongGiaiThua(10)
        assert ketQua == 4037913


# -------------------------------------------------------------------
# NHOM 2: Du lieu khong hop le
# -------------------------------------------------------------------

class TestGiaiThuaDuLieuKhongHopLe:
    """Issue 2: Test ham giai thua - du lieu khong hop le"""

    def test_giai_thua_am(self):
        """Lop tuong duong khong hop le: n am"""
        with pytest.raises(ValueError):
            tinhGiaiThua(-1)

    def test_giai_thua_so_thuc(self):
        """Ngoai le: so thuc"""
        with pytest.raises(TypeError):
            tinhGiaiThua(3.5)

    def test_giai_thua_chuoi(self):
        """Ngoai le: kieu du lieu sai"""
        with pytest.raises(TypeError):
            tinhGiaiThua("5")

    def test_giai_thua_bool(self):
        """Ngoai le: bool khong hop le"""
        with pytest.raises(TypeError):
            tinhGiaiThua(True)


class TestTongGiaiThuaDuLieuKhongHopLe:
    """Issue 2: Test tong giai thua - du lieu khong hop le"""

    def test_n_bang_0(self):
        """Gia tri bien: n = 0 khong hop le cho tong"""
        with pytest.raises(ValueError):
            tinhTongGiaiThua(0)

    def test_n_am(self):
        """Lop tuong duong khong hop le: n am"""
        with pytest.raises(ValueError):
            tinhTongGiaiThua(-3)

    def test_n_la_so_thuc(self):
        """Ngoai le: so thuc"""
        with pytest.raises(TypeError):
            tinhTongGiaiThua(2.5)

    def test_n_la_chuoi(self):
        """Ngoai le: kieu du lieu sai"""
        with pytest.raises(TypeError):
            tinhTongGiaiThua("3")

    def test_n_la_None(self):
        """Ngoai le: None"""
        with pytest.raises(TypeError):
            tinhTongGiaiThua(None)
