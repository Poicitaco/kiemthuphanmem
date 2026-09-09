"""
Bai 1: Tinh chu vi hinh chu nhat
Cong thuc: ChuVi = 2 * (dai + rong)
"""


def tinhChuViHCN(dai, rong):
    """
    Tinh chu vi hinh chu nhat.
    
    Tham so:
        dai  -- chieu dai (so thuc duong)
        rong -- chieu rong (so thuc duong)
    
    Tra ve:
        Chu vi hinh chu nhat neu dau vao hop le.
        Nem ValueError neu dai hoac rong khong hop le.
    """
    if not isinstance(dai, (int, float)) or not isinstance(rong, (int, float)):
        raise TypeError("Chieu dai va chieu rong phai la so")
    if isinstance(dai, bool) or isinstance(rong, bool):
        raise TypeError("Chieu dai va chieu rong phai la so")
    if dai <= 0 or rong <= 0:
        raise ValueError("Chieu dai va chieu rong phai lon hon 0")
    return 2 * (dai + rong)
