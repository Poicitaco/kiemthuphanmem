"""
Test Bai 2: Tinh dien tich hinh chu nhat
Phuong phap kiem thu: Hop den (Black-box Testing)
Ky thuat ap dung:
  - Phan lop tuong duong
  - Phan tich gia tri bien
  - Du lieu hop le va khong hop le
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.bai2_dien_tich_hcn import tinhDienTichHCN


# -------------------------------------------------------------------
# NHOM 1: Du lieu hop le
# -------------------------------------------------------------------

class TestDienTichHCNDuLieuHopLe:
    """Issue 1: Test case du lieu hop le"""

    def test_so_nguyen_duong_thong_thuong(self):
        """Lop tuong duong: ca hai canh deu la so nguyen duong"""
        assert tinhDienTichHCN(5, 3) == 15

    def test_so_thuc_duong(self):
        """Lop tuong duong: dau vao la so thuc"""
        assert tinhDienTichHCN(2.5, 4.0) == pytest.approx(10.0)

    def test_hinh_vuong(self):
        """Truong hop dac biet: dai = rong"""
        assert tinhDienTichHCN(6, 6) == 36

    def test_gia_tri_bien_duoi_gan_0(self):
        """Gia tri bien: gia tri nho nhat con hop le"""
        ketQua = tinhDienTichHCN(0.001, 0.001)
        assert ketQua == pytest.approx(0.000001)

    def test_mot_canh_bang_1(self):
        """Gia tri bien: mot canh bang 1"""
        assert tinhDienTichHCN(1, 7) == 7

    def test_gia_tri_lon(self):
        """Gia tri bien: so lon"""
        assert tinhDienTichHCN(1000, 1000) == 1000000


# -------------------------------------------------------------------
# NHOM 2: Du lieu khong hop le
# -------------------------------------------------------------------

class TestDienTichHCNDuLieuKhongHopLe:
    """Issue 2: Test case du lieu khong hop le, bien, ngoai le"""

    def test_dai_bang_0(self):
        """Gia tri bien: dai = 0"""
        with pytest.raises(ValueError):
            tinhDienTichHCN(0, 5)

    def test_rong_bang_0(self):
        """Gia tri bien: rong = 0"""
        with pytest.raises(ValueError):
            tinhDienTichHCN(3, 0)

    def test_dai_am(self):
        """Lop tuong duong khong hop le: dai am"""
        with pytest.raises(ValueError):
            tinhDienTichHCN(-5, 4)

    def test_rong_am(self):
        """Lop tuong duong khong hop le: rong am"""
        with pytest.raises(ValueError):
            tinhDienTichHCN(4, -5)

    def test_ca_hai_am(self):
        """Lop tuong duong khong hop le: ca hai am"""
        with pytest.raises(ValueError):
            tinhDienTichHCN(-2, -3)

    def test_dai_la_chuoi(self):
        """Ngoai le: kieu du lieu sai"""
        with pytest.raises(TypeError):
            tinhDienTichHCN("5", 3)

    def test_rong_la_None(self):
        """Ngoai le: truyen None"""
        with pytest.raises(TypeError):
            tinhDienTichHCN(5, None)

    def test_dau_vao_la_bool(self):
        """Ngoai le: bool khong duoc coi la so"""
        with pytest.raises(TypeError):
            tinhDienTichHCN(True, 5)
