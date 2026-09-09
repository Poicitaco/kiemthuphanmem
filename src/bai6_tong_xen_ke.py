"""
Bai 6: Tinh tong S = 1 - 2 + 3 - 4 + ... + n
Cong thuc:
    - Neu n le:  S = (n + 1) / 2
    - Neu n chan: S = -n / 2
"""


def tinhTongXenKe(n):
    """
    Tinh tong xen ke S = 1 - 2 + 3 - 4 + ... + n.
    
    Tham so:
        n -- so nguyen duong, so hang cuoi cung
    
    Tra ve:
        Tong xen ke cua day tu 1 den n.
        Nem TypeError neu n khong phai so nguyen.
        Nem ValueError neu n <= 0.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n phai la so nguyen")
    if n <= 0:
        raise ValueError("n phai la so nguyen duong")

    tong = 0
    for soHang in range(1, n + 1):
        if soHang % 2 == 1:
            tong += soHang
        else:
            tong -= soHang
    return tong
