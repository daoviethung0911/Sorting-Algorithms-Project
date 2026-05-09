# Hướng dẫn sử dụng: Đồ án Cài đặt và Đánh giá thuật toán sắp xếp

Dự án này cài đặt 12 thuật toán sắp xếp bằng ngôn ngữ Python và đánh giá hiệu năng của chúng (dựa trên thời gian chạy và số lần so sánh) qua các kích thước và thứ tự dữ liệu khác nhau.

## 1. Tổ chức mã nguồn

Mã nguồn của dự án được chia thành 4 tập tin chính:

*   `7.py`: Tập tin thực thi chính của chương trình. Chịu trách nhiệm phân tích tham số từ dòng lệnh và điều hướng thực thi đến 1 trong 5 lệnh (command) tương ứng.
*   `sorting_algorithms.py`: Chứa mã nguồn cài đặt của 12 thuật toán sắp xếp. Mỗi hàm thuật toán trả về một danh sách: `[sorted_array, (time, comparisons)]`.
*   `data_generator.py`: Hàm sinh dữ liệu đầu vào. Hỗ trợ tạo các mảng dữ liệu với nhiều kích thước và thứ tự khác nhau.
*   `file_io.py`: Xử lý các thao tác đọc và ghi tập tin. Bao gồm hàm đọc mảng từ tập tin và hàm ghi dữ liệu ra tập tin.

## 2. Các tham số dòng lệnh hợp lệ

Khi biên dịch và chạy chương trình, vui lòng sử dụng chính xác các từ khóa sau:

**Tên các thuật toán (Algorithm):**
*   `selection-sort`, `insertion-sort`, `binary-insertion-sort`, `bubble-sort`, `shaker-sort`, `shell-sort`, `heap-sort`, `merge-sort`, `quick-sort`, `counting-sort`, `radix-sort`, `flash-sort`

**Thứ tự dữ liệu đầu vào (Input_order):**
*   `-rand`: Dữ liệu ngẫu nhiên (Randomized)
*   `-sorted`: Dữ liệu đã sắp xếp (Sorted)
*   `-rev`: Dữ liệu sắp xếp ngược (Reversed)
*   `-nsorted`: Dữ liệu gần như đã sắp xếp (Nearly sorted)

**Tham số đầu ra (Output_parameter):**
*   `-time`: Chỉ hiển thị thời gian chạy (tính bằng milliseconds).
*   `-comp`: Chỉ hiển thị số lần so sánh.
*   `-both`: Hiển thị cả thời gian chạy và số lần so sánh.

---

## 3. Cú pháp thực thi

Vui lòng mở Terminal/Command Prompt và chạy các lệnh theo 5 cú pháp chuẩn dưới đây(Có thể thay python bằng pypy nếu sử dụng pypy).

### Chế độ Thuật toán (Algorithm mode: `-a`)

**Lệnh 1: Chạy một thuật toán trên dữ liệu từ tập tin đầu vào có sẵn.**
> **Cú pháp:** `python 7.py -a [Algorithm] [Input_file] [Output_parameter]`
*   *Ví dụ:* `python 7.py -a radix-sort input.txt -both`
*   *Ghi vào tập tin:* Ghi mảng đã sắp xếp ra tập tin `output.txt`.

**Lệnh 2: Chạy một thuật toán trên dữ liệu được sinh tự động.**
> **Cú pháp:** `python 7.py -a [Algorithm] [Input_size] [Input_order] [Output_parameter]`
*   *Ví dụ:* `python 7.py -a selection-sort 50 -rand -time`
*   *Ghi vào tập tin:* Ghi mảng vừa sinh ra tập tin `input.txt` và mảng đã sắp xếp ra tập tin `output.txt`.

**Lệnh 3: Chạy một thuật toán trên TẤT CẢ các thứ tự dữ liệu của một kích thước chỉ định.**
> **Cú pháp:** `python 7.py -a [Algorithm] [Input_size] [Output_parameter]`
*   *Ví dụ:* `python 7.py -a quick-sort 70000 -comp`
*   *Ghi vào tập tin:* Sinh ra và ghi vào 4 tập tin đầu vào: `input_1.txt` (random), `input_2.txt` (nearly sorted), `input_3.txt` (sorted), và `input_4.txt` (reversed).

### Chế độ So sánh (Comparison mode: `-c`)

**Lệnh 4: Chạy hai thuật toán trên dữ liệu từ tập tin đầu vào có sẵn để so sánh.**
> **Cú pháp:** `python 7.py -c [Algorithm_1] [Algorithm_2] [Input_file]`
*   *Ví dụ:* `python 7.py -c heap-sort merge-sort input.txt`
*   *Ghi vào tập tin:* Không ghi tập tin. Kết quả so sánh cả time và comparisons sẽ in được in trực tiếp ra màn hình console.

**Lệnh 5: Chạy hai thuật toán trên dữ liệu được sinh tự động để so sánh.**
> **Cú pháp:** `python 7.py -c [Algorithm_1] [Algorithm_2] [Input_size] [Input_order]`
*   *Ví dụ:* `python 7.py -c quick-sort merge-sort 100000 -nsorted`
*   *Ghi vào tập tin:* Ghi mảng vừa sinh ra tập tin `input.txt`. Kết quả so sánh cả time và comparisons sẽ in được in trực tiếp ra màn hình console.

---

## 4. Định dạng tập tin dữ liệu

Định dạng dùng chung cho tất cả các tập tin đầu vào và đầu ra (`.txt`) của dự án:
*   Dòng 1: Chứa một số nguyên `n`, đại diện cho số lượng phần tử.
*   Dòng 2: Chứa `n` số nguyên, các số được phân tách nhau bởi một khoảng trắng (space).