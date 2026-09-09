# Danh Sach Test Case — Kiem Thu Hop Den

Tong hop cac ca kiem thu (test case) cho 8 bai toan theo phuong phap kiem thu hop den.
Ap dung 3 ky thuat: **Phan lop tuong duong**, **Phan tich gia tri bien**, **Du lieu hop le / khong hop le**.

---

## Bai 1: Tinh Chu Vi Hinh Chu Nhat

**Ham:** `tinhChuViHCN(dai, rong)` | **Cong thuc:** `2 * (dai + rong)`

### Phan lop tuong duong

| Lop | Mo ta | Vi du dau vao | Ket qua mong doi |
|-----|-------|---------------|-----------------|
| HOP LE | Ca hai canh la so nguyen duong | dai=5, rong=3 | 16 |
| HOP LE | Ca hai canh la so thuc duong | dai=2.5, rong=4.0 | 13.0 |
| HOP LE | Hinh vuong (dai = rong) | dai=4, rong=4 | 16 |
| KHONG HOP LE | Mot canh bang 0 | dai=0, rong=5 | ValueError |
| KHONG HOP LE | Mot canh am | dai=-3, rong=5 | ValueError |
| KHONG HOP LE | Kieu sai (chuoi) | dai="abc", rong=5 | TypeError |
| KHONG HOP LE | None | dai=None, rong=5 | TypeError |
| KHONG HOP LE | Bool | dai=True, rong=5 | TypeError |

### Gia tri bien

| Bien | Gia tri | Ket qua mong doi |
|------|---------|-----------------|
| Bien duoi hop le | dai=0.001, rong=0.001 | ~0.004 |
| Gia tri lon | dai=1000, rong=500 | 3000 |

---

## Bai 2: Tinh Dien Tich Hinh Chu Nhat

**Ham:** `tinhDienTichHCN(dai, rong)` | **Cong thuc:** `dai * rong`

### Phan lop tuong duong

| Lop | Mo ta | Vi du dau vao | Ket qua mong doi |
|-----|-------|---------------|-----------------|
| HOP LE | Ca hai canh so nguyen duong | dai=5, rong=3 | 15 |
| HOP LE | So thuc duong | dai=2.5, rong=4.0 | 10.0 |
| HOP LE | Mot canh bang 1 | dai=1, rong=7 | 7 |
| KHONG HOP LE | Mot canh bang 0 | dai=0, rong=5 | ValueError |
| KHONG HOP LE | Mot canh am | dai=-5, rong=4 | ValueError |
| KHONG HOP LE | Kieu sai | dai="5", rong=3 | TypeError |
| KHONG HOP LE | Bool | dai=True, rong=5 | TypeError |

### Gia tri bien

| Bien | Gia tri | Ket qua mong doi |
|------|---------|-----------------|
| Bien duoi hop le | dai=0.001, rong=0.001 | ~0.000001 |
| Gia tri lon | dai=1000, rong=1000 | 1000000 |

---

## Bai 3: Giai Phuong Trinh Bac 2

**Ham:** `giaiPTB2(a, b, c)` | **Dang:** `a*x^2 + b*x + c = 0`

### Phan lop tuong duong

| Lop | Mo ta | Vi du dau vao | Ket qua mong doi |
|-----|-------|---------------|-----------------|
| HOP LE | delta > 0 | a=1, b=-5, c=6 | "Hai nghiem phan biet: x1=2.0, x2=3.0" |
| HOP LE | delta = 0 | a=1, b=-2, c=1 | "Nghiem kep: x = 1.0" |
| HOP LE | delta < 0 | a=1, b=1, c=1 | "Vo nghiem thuc" |
| HOP LE | a=0, b!=0 (bac nhat) | a=0, b=2, c=-4 | "Phuong trinh bac nhat: x = 2.0" |
| BIEN | a=0, b=0, c!=0 | a=0, b=0, c=5 | "Vo nghiem" |
| BIEN | a=0, b=0, c=0 | a=0, b=0, c=0 | "Vo so nghiem" |
| KHONG HOP LE | He so la chuoi | a="1", b=2, c=3 | TypeError |
| KHONG HOP LE | He so la None | a=1, b=None, c=3 | TypeError |
| KHONG HOP LE | Bool | a=True, b=2, c=3 | TypeError |

---

## Bai 4: So Ngay Trong Thang

**Ham:** `soNgayTrongThang(thang, nam)`

### Phan lop tuong duong

| Lop | Mo ta | Vi du dau vao | Ket qua mong doi |
|-----|-------|---------------|-----------------|
| HOP LE | Thang 31 ngay | thang=1, nam=2024 | 31 |
| HOP LE | Thang 30 ngay | thang=4, nam=2024 | 30 |
| HOP LE | Thang 2 nam nhuan | thang=2, nam=2024 | 29 |
| HOP LE | Thang 2 nam thuong | thang=2, nam=2023 | 28 |
| HOP LE | Nam nhuan dac biet (400) | thang=2, nam=2000 | 29 |
| HOP LE | Nam khong nhuan (100) | thang=2, nam=1900 | 28 |
| KHONG HOP LE | Thang 0 | thang=0, nam=2024 | ValueError |
| KHONG HOP LE | Thang 13 | thang=13, nam=2024 | ValueError |
| KHONG HOP LE | Thang am | thang=-1, nam=2024 | ValueError |
| KHONG HOP LE | Nam = 0 | thang=1, nam=0 | ValueError |
| KHONG HOP LE | Nam am | thang=1, nam=-2024 | ValueError |
| KHONG HOP LE | Thang la chuoi | thang="thang1", nam=2024 | TypeError |
| KHONG HOP LE | Thang la so thuc | thang=1.5, nam=2024 | TypeError |

### Gia tri bien

| Bien | Gia tri | Ket qua mong doi |
|------|---------|-----------------|
| Bien duoi thang | thang=1 | 31 |
| Bien tren thang | thang=12 | 31 |

---

## Bai 5: Kiem Tra So Nguyen To

**Ham:** `laSoNguyenTo(n)`

### Phan lop tuong duong

| Lop | Mo ta | Vi du dau vao | Ket qua mong doi |
|-----|-------|---------------|-----------------|
| HOP LE | So nguyen to | n=2, 3, 5, 7, 97 | True |
| HOP LE | Hop so | n=4, 9, 15, 100 | False |
| HOP LE | So 1 (khong la nguyen to) | n=1 | False |
| HOP LE | So 2 (nguyen to chan duy nhat) | n=2 | True |
| HOP LE | So chan > 2 | n=6, 100 | False |
| KHONG HOP LE | n = 0 | n=0 | ValueError |
| KHONG HOP LE | n am | n=-5 | ValueError |
| KHONG HOP LE | So thuc | n=7.5 | TypeError |
| KHONG HOP LE | Chuoi | n="7" | TypeError |
| KHONG HOP LE | None | n=None | TypeError |
| KHONG HOP LE | Bool | n=True | TypeError |

---

## Bai 6: Tong Xen Ke S = 1 - 2 + 3 - 4 + ... + n

**Ham:** `tinhTongXenKe(n)`

### Phan lop tuong duong

| Lop | Mo ta | Vi du dau vao | Ket qua mong doi |
|-----|-------|---------------|-----------------|
| HOP LE | n le | n=1 | 1 |
| HOP LE | n le | n=3 | 2 |
| HOP LE | n le | n=9 | 5 |
| HOP LE | n chan | n=2 | -1 |
| HOP LE | n chan | n=4 | -2 |
| HOP LE | n chan | n=10 | -5 |
| KHONG HOP LE | n = 0 | n=0 | ValueError |
| KHONG HOP LE | n am | n=-1 | ValueError |
| KHONG HOP LE | So thuc | n=3.5 | TypeError |
| KHONG HOP LE | Chuoi | n="5" | TypeError |

### Gia tri bien

| Bien | Gia tri | Ket qua mong doi |
|------|---------|-----------------|
| Bien duoi hop le | n=1 | 1 |
| Bien duoi khong hop le | n=0 | ValueError |

---

## Bai 7: Tim UCLN

**Ham:** `tinhUCLN(a, b)` | **Thuat toan:** Euclid

### Phan lop tuong duong

| Lop | Mo ta | Vi du dau vao | Ket qua mong doi |
|-----|-------|---------------|-----------------|
| HOP LE | a > b | a=12, b=8 | 4 |
| HOP LE | a < b | a=8, b=12 | 4 |
| HOP LE | a = b | a=7, b=7 | 7 |
| HOP LE | a la boi cua b | a=10, b=5 | 5 |
| HOP LE | Nguyen to cung nhau | a=7, b=9 | 1 |
| HOP LE | Mot so bang 1 | a=1, b=100 | 1 |
| HOP LE | Ket qua lon | a=360, b=240 | 120 |
| KHONG HOP LE | a = 0 | a=0, b=5 | ValueError |
| KHONG HOP LE | b = 0 | a=5, b=0 | ValueError |
| KHONG HOP LE | a am | a=-6, b=4 | ValueError |
| KHONG HOP LE | So thuc | a=6.5, b=4 | TypeError |
| KHONG HOP LE | Chuoi | a="6", b=4 | TypeError |
| KHONG HOP LE | Bool | a=6, b=True | TypeError |

---

## Bai 8: Tong Giai Thua S = 1! + 2! + ... + n!

**Ham:** `tinhTongGiaiThua(n)`, su dung ham con `tinhGiaiThua(n)`

### Phan lop tuong duong

| Lop | Mo ta | Vi du dau vao | Ket qua mong doi |
|-----|-------|---------------|-----------------|
| HOP LE | n = 1 | n=1 | 1 |
| HOP LE | n = 2 | n=2 | 3 |
| HOP LE | n = 3 | n=3 | 9 |
| HOP LE | n = 4 | n=4 | 33 |
| HOP LE | n = 5 | n=5 | 153 |
| HOP LE | n lon | n=10 | 4037913 |
| BIEN | 0! = 1 (ham giai thua) | tinhGiaiThua(0) | 1 |
| KHONG HOP LE | n = 0 (tong) | tinhTongGiaiThua(0) | ValueError |
| KHONG HOP LE | n am | tinhTongGiaiThua(-3) | ValueError |
| KHONG HOP LE | So thuc | tinhTongGiaiThua(2.5) | TypeError |
| KHONG HOP LE | Chuoi | tinhTongGiaiThua("3") | TypeError |
| KHONG HOP LE | None | tinhTongGiaiThua(None) | TypeError |

---

## Ket Qua Chay Kiem Thu

Chay lenh: `pytest tests/ -v`

Tong so test case: **74**
Ket qua: **74 PASSED** (xem ket qua chi tiet trong file `ket_qua_chay_test.txt`)
