"""
Test Bai 6: Tinh tong S = 1 - 2 + 3 - 4 + ... + n
Phuong phap kiem thu: Hop den (Black-box Testing)
Ky thuat ap dung:
  - Phan lop tuong duong: n le, n chan
  - Phan tich gia tri bien: n = 1, n = 2
  - Du lieu khong hop le
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.bai6_tong_xen_ke import tinhTongXenKe


# -------------------------------------------------------------------
# NHOM 1: Du lieu hop le
# -------------------------------------------------------------------

class TestTongXenKeDuLieuHopLe:
    """Issue 1: Test case du lieu hop le"""

    def test_n_bang_1(self):
        """Gia tri bien: n = 1 (bien duoi) => S = 1"""
        assert tinhTongXenKe(1) == 1

    def test_n_bang_2(self):
        """Gia tri bien: n = 2 => S = 1 - 2 = -1"""
        assert tinhTongXenKe(2) == -1

    def test_n_bang_3(self):
        """Lop tuong duong n le: n = 3 => S = 1 - 2 + 3 = 2"""
        assert tinhTongXenKe(3) == 2

    def test_n_bang_4(self):
        """Lop tuong duong n chan: n = 4 => S = 1 - 2 + 3 - 4 = -2"""
        assert tinhTongXenKe(4) == -2

    def test_n_le_lon(self):
        """Lop tuong duong n le lon: n = 9 => S = 1-2+3-4+5-6+7-8+9 = 5"""
        assert tinhTongXenKe(9) == 5

    def test_n_chan_lon(self):
        """Lop tuong duong n chan lon: n = 10 => S = -5"""
        assert tinhTongXenKe(10) == -5

    def test_cong_thuc_le(self):
        """Kiem tra cong thuc n le: S = (n+1)/2"""
        for soChanLe in range(1, 20, 2):
            assert tinhTongXenKe(soChanLe) == (soChanLe + 1) // 2

    def test_cong_thuc_chan(self):
        """Kiem tra cong thuc n chan: S = -n/2"""
        for soChan in range(2, 20, 2):
            assert tinhTongXenKe(soChan) == -soChan // 2


# -------------------------------------------------------------------
# NHOM 2: Du lieu khong hop le
# -------------------------------------------------------------------

class TestTongXenKeDuLieuKhongHopLe:
    """Issue 2: Test case du lieu khong hop le, bien, ngoai le"""

    def test_n_bang_0(self):
        """Gia tri bien: n = 0 khong hop le"""
        with pytest.raises(ValueError):
            tinhTongXenKe(0)

    def test_n_am(self):
        """Lop tuong duong khong hop le: so am"""
        with pytest.raises(ValueError):
            tinhTongXenKe(-1)

    def test_n_la_so_thuc(self):
        """Ngoai le: so thuc"""
        with pytest.raises(TypeError):
            tinhTongXenKe(3.5)

    def test_n_la_chuoi(self):
        """Ngoai le: kieu du lieu sai"""
        with pytest.raises(TypeError):
            tinhTongXenKe("5")

    def test_n_la_None(self):
        """Ngoai le: None"""
        with pytest.raises(TypeError):
            tinhTongXenKe(None)
