"""
Test Bai 5: Kiem tra so nguyen to
Phuong phap kiem thu: Hop den (Black-box Testing)
Ky thuat ap dung:
  - Phan lop tuong duong: so nguyen to, hop so, so 1
  - Phan tich gia tri bien: n = 1, 2, 3
  - Du lieu khong hop le
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.bai5_so_nguyen_to import laSoNguyenTo


# -------------------------------------------------------------------
# NHOM 1: Du lieu hop le
# -------------------------------------------------------------------

class TestSoNguyenToDuLieuHopLe:
    """Issue 1: Test case du lieu hop le"""

    def test_so_nguyen_to_nho(self):
        """Lop tuong duong: so nguyen to nho"""
        assert laSoNguyenTo(2) == True
        assert laSoNguyenTo(3) == True
        assert laSoNguyenTo(5) == True
        assert laSoNguyenTo(7) == True

    def test_so_nguyen_to_lon(self):
        """Lop tuong duong: so nguyen to lon"""
        assert laSoNguyenTo(97) == True
        assert laSoNguyenTo(101) == True

    def test_hop_so(self):
        """Lop tuong duong: hop so (khong phai so nguyen to)"""
        assert laSoNguyenTo(4) == False
        assert laSoNguyenTo(9) == False
        assert laSoNguyenTo(15) == False
        assert laSoNguyenTo(100) == False

    def test_so_1_khong_phai_nguyen_to(self):
        """Gia tri bien: n = 1 la gia tri bien duoi, khong la so nguyen to"""
        assert laSoNguyenTo(1) == False

    def test_so_2_la_so_nguyen_to_chan_duy_nhat(self):
        """Gia tri bien: n = 2 la so nguyen to chan duy nhat"""
        assert laSoNguyenTo(2) == True

    def test_so_chan_lon_hon_2(self):
        """Lop tuong duong: moi so chan > 2 deu la hop so"""
        assert laSoNguyenTo(6) == False
        assert laSoNguyenTo(100) == False


# -------------------------------------------------------------------
# NHOM 2: Du lieu khong hop le
# -------------------------------------------------------------------

class TestSoNguyenToDuLieuKhongHopLe:
    """Issue 2: Test case du lieu khong hop le, bien, ngoai le"""

    def test_n_bang_0(self):
        """Gia tri bien: n = 0 khong hop le"""
        with pytest.raises(ValueError):
            laSoNguyenTo(0)

    def test_n_am(self):
        """Lop tuong duong khong hop le: so am"""
        with pytest.raises(ValueError):
            laSoNguyenTo(-5)

    def test_n_la_so_thuc(self):
        """Ngoai le: so thuc"""
        with pytest.raises(TypeError):
            laSoNguyenTo(7.5)

    def test_n_la_chuoi(self):
        """Ngoai le: kieu du lieu sai"""
        with pytest.raises(TypeError):
            laSoNguyenTo("7")

    def test_n_la_None(self):
        """Ngoai le: None"""
        with pytest.raises(TypeError):
            laSoNguyenTo(None)

    def test_n_la_bool(self):
        """Ngoai le: bool khong hop le"""
        with pytest.raises(TypeError):
            laSoNguyenTo(True)
