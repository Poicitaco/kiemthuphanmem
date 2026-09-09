"""
Bai 8: Tinh tong S = 1! + 2! + 3! + ... + n!
Su dung ham tinh giai thua cua n
"""


def tinhGiaiThua(n):
    """
    Tinh giai thua n! = 1 * 2 * 3 * ... * n.
    
    Tham so:
        n -- so nguyen khong am
    
    Tra ve:
        n! (so nguyen)
        Nem TypeError neu n khong phai so nguyen.
        Nem ValueError neu n < 0.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n phai la so nguyen")
    if n < 0:
        raise ValueError("n phai la so nguyen khong am")

    ketQua = 1
    for soNhan in range(2, n + 1):
        ketQua *= soNhan
    return ketQua


def tinhTongGiaiThua(n):
    """
    Tinh tong S = 1! + 2! + 3! + ... + n!.
    
    Tham so:
        n -- so hang cuoi cung (so nguyen duong)
    
    Tra ve:
        Tong cua cac giai thua tu 1! den n!.
        Nem TypeError neu n khong phai so nguyen.
        Nem ValueError neu n <= 0.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n phai la so nguyen")
    if n <= 0:
        raise ValueError("n phai la so nguyen duong")

    tongCong = 0
    for soHang in range(1, n + 1):
        tongCong += tinhGiaiThua(soHang)
    return tongCong
