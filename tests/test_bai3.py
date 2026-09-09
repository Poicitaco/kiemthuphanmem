"""
Test Bai 3: Giai phuong trinh bac 2
Phuong phap kiem thu: Hop den (Black-box Testing)
Ky thuat ap dung:
  - Phan lop tuong duong: delta > 0, delta = 0, delta < 0
  - Truong hop bien: a = 0 (phuong trinh bac nhat)
  - Du lieu khong hop le
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.bai3_giai_ptb2 import giaiPTB2


# -------------------------------------------------------------------
# NHOM 1: Du lieu hop le
# -------------------------------------------------------------------

class TestGiaiPTB2DuLieuHopLe:
    """Issue 1: Test case du lieu hop le"""

    def test_hai_nghiem_phan_biet(self):
        """Lop tuong duong: delta > 0 => hai nghiem phan biet
        x^2 - 5x + 6 = 0 => x = 2 hoac x = 3"""
        ket_qua = giaiPTB2(1, -5, 6)
        assert "Hai nghiem phan biet" in ket_qua
        assert "2.0" in ket_qua
        assert "3.0" in ket_qua

    def test_nghiem_kep(self):
        """Lop tuong duong: delta = 0 => nghiem kep
        x^2 - 2x + 1 = 0 => x = 1"""
        ket_qua = giaiPTB2(1, -2, 1)
        assert "Nghiem kep" in ket_qua
        assert "1.0" in ket_qua

    def test_vo_nghiem_thuc(self):
        """Lop tuong duong: delta < 0 => vo nghiem thuc
        x^2 + x + 1 = 0"""
        assert giaiPTB2(1, 1, 1) == "Vo nghiem thuc"

    def test_a_bang_0_b_khac_0(self):
        """Truong hop bien: a = 0 => phuong trinh bac nhat
        0*x^2 + 2*x - 4 = 0 => x = 2"""
        ket_qua = giaiPTB2(0, 2, -4)
        assert "Phuong trinh bac nhat" in ket_qua
        assert "2.0" in ket_qua

    def test_he_so_am(self):
        """Lop tuong duong: he so am, van co nghiem
        -x^2 + 5x - 6 = 0 => x = 2 hoac x = 3"""
        ket_qua = giaiPTB2(-1, 5, -6)
        assert "Hai nghiem phan biet" in ket_qua

    def test_he_so_thuc(self):
        """Lop tuong duong: he so la so thuc
        x^2 - 2.5x + 1.5 = 0"""
        ket_qua = giaiPTB2(1, -2.5, 1.5)
        assert "Hai nghiem phan biet" in ket_qua

    def test_c_bang_0(self):
        """Truong hop dac biet: c = 0 => mot nghiem bang 0
        x^2 - x = 0 => x = 0 hoac x = 1"""
        ket_qua = giaiPTB2(1, -1, 0)
        assert "Hai nghiem phan biet" in ket_qua


# -------------------------------------------------------------------
# NHOM 2: Du lieu khong hop le, bien, ngoai le
# -------------------------------------------------------------------

class TestGiaiPTB2DuLieuKhongHopLe:
    """Issue 2: Test case du lieu khong hop le, bien, ngoai le"""

    def test_a_bang_0_b_bang_0_c_khac_0(self):
        """Bien: a = 0, b = 0, c != 0 => vo nghiem"""
        assert giaiPTB2(0, 0, 5) == "Vo nghiem"

    def test_a_bang_0_b_bang_0_c_bang_0(self):
        """Bien: a = 0, b = 0, c = 0 => vo so nghiem"""
        assert giaiPTB2(0, 0, 0) == "Vo so nghiem"

    def test_he_so_la_chuoi(self):
        """Ngoai le: he so la chuoi"""
        with pytest.raises(TypeError):
            giaiPTB2("1", 2, 3)

    def test_he_so_la_None(self):
        """Ngoai le: he so la None"""
        with pytest.raises(TypeError):
            giaiPTB2(1, None, 3)

    def test_he_so_la_bool(self):
        """Ngoai le: bool khong hop le"""
        with pytest.raises(TypeError):
            giaiPTB2(True, 2, 3)
