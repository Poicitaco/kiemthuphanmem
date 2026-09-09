"""
Bai 7: Tim uoc chung lon nhat (UCLN) cua a va b
Su dung thuat toan Euclid
"""


def tinhUCLN(a, b):
    """
    Tim uoc chung lon nhat cua a va b bang thuat toan Euclid.
    
    Tham so:
        a, b -- so nguyen duong
    
    Tra ve:
        UCLN(a, b) la so nguyen duong.
        Nem TypeError neu a hoac b khong phai so nguyen.
        Nem ValueError neu a hoac b <= 0.
    """
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("a phai la so nguyen")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("b phai la so nguyen")
    if a <= 0:
        raise ValueError("a phai la so nguyen duong")
    if b <= 0:
        raise ValueError("b phai la so nguyen duong")

    soLon = a
    soNho = b
    while soNho != 0:
        soLon, soNho = soNho, soLon % soNho
    return soLon
