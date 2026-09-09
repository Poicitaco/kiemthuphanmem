"""
Test Bai 7: Tim UCLN cua a va b
Phuong phap kiem thu: Hop den (Black-box Testing)
Ky thuat ap dung:
  - Phan lop tuong duong: a > b, a < b, a = b
  - Phan tich gia tri bien: a = 1 hoac b = 1, a va b nguyen to cung nhau
  - Du lieu khong hop le
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.bai7_ucln import tinhUCLN


# -------------------------------------------------------------------
# NHOM 1: Du lieu hop le
# -------------------------------------------------------------------

class TestUCLNDuLieuHopLe:
    """Issue 1: Test case du lieu hop le"""

    def test_a_lon_hon_b(self):
        """Lop tuong duong: a > b"""
        assert tinhUCLN(12, 8) == 4

    def test_a_nho_hon_b(self):
        """Lop tuong duong: a < b"""
        assert tinhUCLN(8, 12) == 4

    def test_a_bang_b(self):
        """Lop tuong duong: a = b => UCLN = a = b"""
        assert tinhUCLN(7, 7) == 7

    def test_mot_so_la_boi_cua_so_kia(self):
        """Lop tuong duong: a la boi cua b"""
        assert tinhUCLN(10, 5) == 5
        assert tinhUCLN(100, 25) == 25

    def test_nguyen_to_cung_nhau(self):
        """Lop tuong duong: a va b nguyen to cung nhau => UCLN = 1"""
        assert tinhUCLN(7, 9) == 1
        assert tinhUCLN(13, 17) == 1

    def test_mot_so_bang_1(self):
        """Gia tri bien: mot so bang 1 => UCLN luon la 1"""
        assert tinhUCLN(1, 100) == 1
        assert tinhUCLN(100, 1) == 1

    def test_ca_hai_bang_1(self):
        """Gia tri bien: a = b = 1"""
        assert tinhUCLN(1, 1) == 1

    def test_so_lon(self):
        """Lop tuong duong: so lon"""
        assert tinhUCLN(1000000, 999999) == 1
        assert tinhUCLN(360, 240) == 120

    def test_vi_du_thuc_te(self):
        """Kiem tra vi du tien ich: UCLN(48, 18) = 6"""
        assert tinhUCLN(48, 18) == 6


# -------------------------------------------------------------------
# NHOM 2: Du lieu khong hop le
# -------------------------------------------------------------------

class TestUCLNDuLieuKhongHopLe:
    """Issue 2: Test case du lieu khong hop le, bien, ngoai le"""

    def test_a_bang_0(self):
        """Gia tri bien: a = 0 khong hop le"""
        with pytest.raises(ValueError):
            tinhUCLN(0, 5)

    def test_b_bang_0(self):
        """Gia tri bien: b = 0 khong hop le"""
        with pytest.raises(ValueError):
            tinhUCLN(5, 0)

    def test_a_am(self):
        """Lop tuong duong khong hop le: a am"""
        with pytest.raises(ValueError):
            tinhUCLN(-6, 4)

    def test_b_am(self):
        """Lop tuong duong khong hop le: b am"""
        with pytest.raises(ValueError):
            tinhUCLN(6, -4)

    def test_a_la_so_thuc(self):
        """Ngoai le: so thuc"""
        with pytest.raises(TypeError):
            tinhUCLN(6.5, 4)

    def test_a_la_chuoi(self):
        """Ngoai le: kieu du lieu sai"""
        with pytest.raises(TypeError):
            tinhUCLN("6", 4)

    def test_b_la_bool(self):
        """Ngoai le: bool khong hop le"""
        with pytest.raises(TypeError):
            tinhUCLN(6, True)
