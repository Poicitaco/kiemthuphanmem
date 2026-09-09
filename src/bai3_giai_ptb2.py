"""
Bai 3: Giai phuong trinh bac 2
Dang: a*x^2 + b*x + c = 0
"""
import math


def giaiPTB2(a, b, c):
    """
    Giai phuong trinh bac hai a*x^2 + b*x + c = 0.
    
    Tham so:
        a, b, c -- he so phuong trinh (so thuc)
    
    Tra ve:
        - "Phuong trinh bac nhat: ..." neu a = 0, b != 0
        - "Vo nghiem" neu a = 0, b = 0, c != 0
        - "Vo so nghiem" neu a = 0, b = 0, c = 0
        - "Vo nghiem thuc" neu delta < 0
        - "Nghiem kep: x = ..." neu delta = 0
        - "Hai nghiem phan biet: x1 = ..., x2 = ..." neu delta > 0
        Nem TypeError neu a, b, c khong phai so.
    """
    for thamSo, tenThamSo in [(a, "a"), (b, "b"), (c, "c")]:
        if not isinstance(thamSo, (int, float)):
            raise TypeError(f"He so {tenThamSo} phai la so")
        if isinstance(thamSo, bool):
            raise TypeError(f"He so {tenThamSo} phai la so")

    if a == 0:
        if b == 0:
            if c == 0:
                return "Vo so nghiem"
            else:
                return "Vo nghiem"
        else:
            nghiem = -c / b
            return f"Phuong trinh bac nhat: x = {nghiem}"

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return "Vo nghiem thuc"
    elif delta == 0:
        nghiemKep = -b / (2 * a)
        return f"Nghiem kep: x = {nghiemKep}"
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return f"Hai nghiem phan biet: x1 = {x1}, x2 = {x2}"
