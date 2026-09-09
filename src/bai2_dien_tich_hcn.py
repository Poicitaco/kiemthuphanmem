"""
Bai 2: Tinh dien tich hinh chu nhat
Cong thuc: DienTich = dai * rong
"""


def tinhDienTichHCN(dai, rong):
    """
    Tinh dien tich hinh chu nhat.
    
    Tham so:
        dai  -- chieu dai (so thuc duong)
        rong -- chieu rong (so thuc duong)
    
    Tra ve:
        Dien tich hinh chu nhat neu dau vao hop le.
        Nem TypeError neu khong phai so.
        Nem ValueError neu dai hoac rong khong duong.
    """
    if not isinstance(dai, (int, float)) or not isinstance(rong, (int, float)):
        raise TypeError("Chieu dai va chieu rong phai la so")
    if isinstance(dai, bool) or isinstance(rong, bool):
        raise TypeError("Chieu dai va chieu rong phai la so")
    if dai <= 0 or rong <= 0:
        raise ValueError("Chieu dai va chieu rong phai lon hon 0")
    return dai * rong
