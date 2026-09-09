"""
Bai 4: Tinh so ngay cua mot thang
Ho tro nam nhuan theo lich Gregory
"""


def laNamNhuan(nam):
    """Kiem tra nam co phai nam nhuan khong."""
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)


def soNgayTrongThang(thang, nam):
    """
    Tra ve so ngay cua mot thang trong mot nam cu the.
    
    Tham so:
        thang -- so thang (nguyen tu 1 den 12)
        nam   -- so nam (nguyen duong)
    
    Tra ve:
        So nguyen la so ngay trong thang do.
        Nem TypeError neu thang hoac nam khong phai so nguyen.
        Nem ValueError neu thang ngoai khoang [1, 12] hoac nam <= 0.
    """
    if not isinstance(thang, int) or isinstance(thang, bool):
        raise TypeError("Thang phai la so nguyen")
    if not isinstance(nam, int) or isinstance(nam, bool):
        raise TypeError("Nam phai la so nguyen")
    if not (1 <= thang <= 12):
        raise ValueError("Thang phai tu 1 den 12")
    if nam <= 0:
        raise ValueError("Nam phai la so nguyen duong")

    bangSoNgay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if thang == 2 and laNamNhuan(nam):
        return 29
    return bangSoNgay[thang - 1]
