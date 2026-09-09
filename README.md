# Bai Thuc Hanh 03 — Kiem Thu Hop Den

> **Mon hoc:** Kiem Thu Phan Mem  
> **Bai:** Thuc hanh 03 — Kiem thu hop den (Black-box Testing)

## Gioi Thieu

Bai thuc hanh nay xay dung **8 chuong trinh Python** va thiet ke cac ca kiem thu theo phuong phap **kiem thu hop den**, ap dung 3 ky thuat:

- **Phan lop tuong duong** (Equivalence Partitioning)
- **Phan tich gia tri bien** (Boundary Value Analysis)  
- **Du lieu hop le va khong hop le** (Valid / Invalid data)

---

## Cau Truc Du An

```
kiemthuphanmem/
├── README.md
├── yeucau.md
├── src/
│   ├── bai1_chu_vi_hcn.py         # Chu vi hinh chu nhat
│   ├── bai2_dien_tich_hcn.py      # Dien tich hinh chu nhat
│   ├── bai3_giai_ptb2.py          # Giai phuong trinh bac 2
│   ├── bai4_so_ngay_trong_thang.py # So ngay cua mot thang
│   ├── bai5_so_nguyen_to.py        # Kiem tra so nguyen to
│   ├── bai6_tong_xen_ke.py         # Tong 1-2+3-4+...+n
│   ├── bai7_ucln.py                # Tim UCLN(a, b)
│   └── bai8_tong_giai_thua.py      # Tong 1!+2!+...+n!
├── tests/
│   ├── test_bai1.py
│   ├── test_bai2.py
│   ├── test_bai3.py
│   ├── test_bai4.py
│   ├── test_bai5.py
│   ├── test_bai6.py
│   ├── test_bai7.py
│   └── test_bai8.py
└── docs/
    └── test_cases.md               # Danh sach test case chi tiet
```

---

## Cac Bai Toan

| # | Bai toan | Ham chinh | So test |
|---|----------|-----------|---------|
| 1 | Chu vi hinh chu nhat | `tinhChuViHCN(dai, rong)` | 10 |
| 2 | Dien tich hinh chu nhat | `tinhDienTichHCN(dai, rong)` | 9 |
| 3 | Giai phuong trinh bac 2 | `giaiPTB2(a, b, c)` | 12 |
| 4 | So ngay cua mot thang | `soNgayTrongThang(thang, nam)` | 17 |
| 5 | Kiem tra so nguyen to | `laSoNguyenTo(n)` | 12 |
| 6 | Tong xen ke S=1-2+3-...+n | `tinhTongXenKe(n)` | 13 |
| 7 | Tim UCLN(a, b) | `tinhUCLN(a, b)` | 16 |
| 8 | Tong giai thua S=1!+2!+...+n! | `tinhTongGiaiThua(n)` | 13 |
| | **Tong cong** | | **102** |

---

## Cach Chay Kiem Thu

### Yeu cau
- Python 3.x
- pytest: `pip install pytest`

### Chay toan bo test

```bash
pytest tests/ -v
```

### Chay test cho tung bai

```bash
pytest tests/test_bai1.py -v
pytest tests/test_bai2.py -v
# ... tuong tu cho cac bai khac
```

### Chay test theo nhom (Issue)

```bash
# Chi chay test du lieu hop le (Issue 1)
pytest tests/ -v -k "DuLieuHopLe"

# Chi chay test du lieu khong hop le (Issue 2)
pytest tests/ -v -k "DuLieuKhongHopLe"
```

---

## Ket Qua Kiem Thu

Xem file `ket_qua_chay_test.txt` hoac chay lai lenh:

```bash
pytest tests/ -v --tb=short > ket_qua_chay_test.txt
```

---

## Mo Ta Ap Dung Kiem Thu Hop Den

### Bai 1 & 2 (HCN)
- **Phan lop tuong duong**: (dai > 0, rong > 0), (dai = 0), (dai < 0), kieu sai
- **Gia tri bien**: bien duoi hop le (0.001), so rat lon (1000)

### Bai 3 (PTB2)
- **Phan lop tuong duong**: delta > 0, delta = 0, delta < 0, a = 0
- **Bien dac biet**: a = b = c = 0 (vo so nghiem), a = b = 0 c != 0 (vo nghiem)

### Bai 4 (So ngay thang)
- **Phan lop tuong duong**: thang 31 ngay, thang 30 ngay, thang 2 nam nhuan, thang 2 nam thuong
- **Gia tri bien**: thang 1 (bien duoi), thang 12 (bien tren), thang 0 va 13 (ngoai bien)
- **Bien dac biet**: nam nhuan chia het 100 (1900) vs nam nhuan chia het 400 (2000)

### Bai 5 (So nguyen to)
- **Phan lop tuong duong**: so nguyen to, hop so, so 1
- **Bien dac biet**: n = 1 (khong la nguyen to), n = 2 (nguyen to chan duy nhat)

### Bai 6 (Tong xen ke)
- **Phan lop tuong duong**: n le (S = (n+1)/2), n chan (S = -n/2)
- **Gia tri bien**: n = 1 (bien duoi hop le), n = 0 (ngoai bien)

### Bai 7 (UCLN)
- **Phan lop tuong duong**: a > b, a < b, a = b, nguyen to cung nhau, mot so la boi cua so kia
- **Gia tri bien**: a = 1 hoac b = 1 (UCLN = 1)

### Bai 8 (Tong giai thua)
- **Phan lop tuong duong**: n = 1, n nho (2-5), n lon (10)
- **Bien dac biet**: 0! = 1 (ham giai thua chap nhan n = 0)
- Ham `tinhGiaiThua` duoc kiem thu rieng biet de dam bao tinh dung dan

---

## GitHub Issues

| Issue | Noi dung | Trang thai |
|-------|----------|------------|
| #1 | Thiet ke va viet cac ca kiem thu cho **du lieu hop le** | Closed |
| #2 | Thiet ke va viet cac ca kiem thu cho **du lieu khong hop le, bien, ngoai le** | Closed |
