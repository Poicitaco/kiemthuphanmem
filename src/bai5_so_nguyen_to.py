"""
Bai 5: Kiem tra n co phai so nguyen to khong
So nguyen to la so lon hon 1 va chi chia het cho 1 va chinh no
"""


def laSoNguyenTo(n):
    """
    Kiem tra n co phai so nguyen to khong.
    
    Tham so:
        n -- so nguyen can kiem tra
    
    Tra ve:
        True neu n la so nguyen to, False neu khong phai.
        Nem TypeError neu n khong phai so nguyen.
        Nem ValueError neu n <= 0.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n phai la so nguyen")
    if n <= 0:
        raise ValueError("n phai la so nguyen duong")

    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    uocThu = 3
    while uocThu * uocThu <= n:
        if n % uocThu == 0:
            return False
        uocThu += 2

    return True
