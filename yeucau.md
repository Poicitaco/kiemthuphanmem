# BÀI THỰC HÀNH 03

## Bài thực hành: Kiểm thử hộp đen

 xây dựng chương trình và thiết kế kiểm thử cho các bài toán sau, sau đó đưa toàn bộ mã nguồn lên một GitHub repo của em:

1. Tính chu vi hình chữ nhật.
2. Tính diện tích hình chữ nhật.
3. Giải phương trình bậc 2.
4. Tính số ngày của một tháng.
5. Kiểm tra `n` có phải là số nguyên tố hay không.
6. Tính tổng `S = 1 - 2 + 3 - 4 + ... + n`.
7. Tìm UCLN của `a` và `b`.
8. Tính tổng `S = 1! + 2! + 3! + ... + n!`
   (trong đó có sử dụng hàm tính giai thừa của `n`).

---

## Yêu cầu thực hiện

* Với mỗi bài toán, em cần xác định **đầu vào**, **đầu ra mong đợi** và các trường hợp kiểm thử theo hướng **kiểm thử hộp đen**.
* Cần thiết kế các test case dựa trên các kỹ thuật kiểm thử hộp đen phù hợp như:

  * **Phân lớp tương đương**;
  * **Phân tích giá trị biên**;
  * **Dữ liệu hợp lệ và dữ liệu không hợp lệ**.

---

## Yêu cầu bổ sung

* Với mỗi bài toán, ngoài các trường hợp dữ liệu đúng, cần xây dựng **tối thiểu 1 tình huống dữ liệu sai hoặc không hợp lệ** để quan sát và kiểm tra kết quả xử lý của chương trình.
* Có thể sử dụng các AI agent để:

  * Gợi ý mã nguồn chương trình;
  * Gợi ý các lớp tương đương;
  * Xác định giá trị biên;
  * Đề xuất các test case kiểm thử hộp đen.

---

## Yêu cầu làm việc với GitHub

Sau khi hoàn thành các chương trình, em thực hiện các yêu cầu sau trên GitHub:

* **Tạo issue 1:** Thiết kế và viết các ca kiểm thử hộp đen cho các trường hợp **dữ liệu hợp lệ**.
* **Tạo issue 2:** Thiết kế và viết các ca kiểm thử hộp đen cho các trường hợp **dữ liệu không hợp lệ, biên và ngoại lệ**.

Sau đó, lần lượt giải quyết từng issue và tạo **commit tương ứng** cho mỗi issue đã hoàn thành.

---

## Yêu cầu nộp bài

* Nộp **link GitHub repo** để giảng viên có thể truy cập bài làm.
* Trong repo cần có:

  * Mã nguồn chương trình;
  * Danh sách test case;
  * Kết quả chạy kiểm thử;
  * Mô tả ngắn gọn cách em áp dụng **kiểm thử hộp đen** cho từng bài.
