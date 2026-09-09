"""
Test Bai 1: Tinh chu vi hinh chu nhat
Phuong phap kiem thu: Hop den (Black-box Testing)
Ky thuat ap dung:
  - Phan lop tuong duong (Equivalence Partitioning)
  - Phan tich gia tri bien (Boundary Value Analysis)
  - Du lieu hop le va khong hop le
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.bai1_chu_vi_hcn import tinhChuViHCN


# -------------------------------------------------------------------
# NHOM 1: Du lieu hop le - Phan lop tuong duong va gia tri bien
# -------------------------------------------------------------------

class TestChuViHCNDuLieuHopLe:
    """Issue 1: Test case du lieu hop le"""

    def test_so_nguyen_duong_thong_thuong(self):
        """Lop tuong duong: ca dai va rong deu la so nguyen duong thong thuong"""
        assert tinhChuViHCN(5, 3) == 16

    def test_so_thuc_duong(self):
        """Lop tuong duong: dau vao la so thuc duong"""
        assert tinhChuViHCN(2.5, 4.0) == pytest.approx(13.0)

    def test_hinh_vuong(self):
        """Truong hop dac biet: dai = rong (hinh vuong)"""
        assert tinhChuViHCN(4, 4) == 16

    def test_gia_tri_bien_duoi_gan_0(self):
        """Phan tich gia tri bien: ca hai gia tri gan 0 nhat con hop le"""
        ketQua = tinhChuViHCN(0.001, 0.001)
        assert ketQua == pytest.approx(0.004)

    def test_gia_tri_lon(self):
        """Phan tich gia tri bien: so lon"""
        assert tinhChuViHCN(1000, 500) == 3000

    def test_mot_canh_rat_nho_mot_canh_rat_lon(self):
        """Lop tuong duong: ty le chieu dai chieu rong chenh lech lon"""
        assert tinhChuViHCN(0.001, 1000) == pytest.approx(2000.002)


# -------------------------------------------------------------------
# NHOM 2: Du lieu khong hop le - Gia tri bien va ngoai le
# -------------------------------------------------------------------

class TestChuViHCNDuLieuKhongHopLe:
    """Issue 2: Test case du lieu khong hop le, bien, ngoai le"""

    def test_dai_bang_0(self):
        """Gia tri bien: dai = 0 khong hop le"""
        with pytest.raises(ValueError):
            tinhChuViHCN(0, 5)

    def test_rong_bang_0(self):
        """Gia tri bien: rong = 0 khong hop le"""
        with pytest.raises(ValueError):
            tinhChuViHCN(5, 0)

    def test_dai_am(self):
        """Lop tuong duong khong hop le: chieu dai am"""
        with pytest.raises(ValueError):
            tinhChuViHCN(-3, 5)

    def test_rong_am(self):
        """Lop tuong duong khong hop le: chieu rong am"""
        with pytest.raises(ValueError):
            tinhChuViHCN(5, -2)

    def test_ca_hai_am(self):
        """Lop tuong duong khong hop le: ca hai canh deu am"""
        with pytest.raises(ValueError):
            tinhChuViHCN(-4, -3)

    def test_dai_la_chuoi(self):
        """Ngoai le: truyen chuoi thay vi so"""
        with pytest.raises(TypeError):
            tinhChuViHCN("abc", 5)

    def test_rong_la_chuoi(self):
        """Ngoai le: truyen chuoi cho chieu rong"""
        with pytest.raises(TypeError):
            tinhChuViHCN(5, "xyz")

    def test_dai_la_None(self):
        """Ngoai le: truyen None"""
        with pytest.raises(TypeError):
            tinhChuViHCN(None, 5)

    def test_dai_la_bool(self):
        """Ngoai le: bool khong duoc coi la so hop le"""
        with pytest.raises(TypeError):
            tinhChuViHCN(True, 5)
