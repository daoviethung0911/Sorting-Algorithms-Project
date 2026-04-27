import sys
import time
from data_generator import generate_data # Import từ file data_generator.py của bạn

# ==========================================
# PHẦN 1: CÁC LỚP THUẬT TOÁN SẮP XẾP (CLASSES)
# ==========================================

class ShakerSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        comparisons = 0
        left = 0
        right = n - 1
        k = 0
        
        while left < right:
            for i in range(left, right):
                comparisons += 1
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    k = i
            right = k
            
            for i in range(right, left, -1):
                comparisons += 1
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    k = i
            left = k
            
        return arr, comparisons


class HeapSort:
    @staticmethod
    def _heapify(arr, n, i):
        comparisons = 0
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            comparisons += 1
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            _, comp_recursive = HeapSort._heapify(arr, n, largest)
            comparisons += comp_recursive
            
        return arr, comparisons

    @staticmethod
    def sort(arr):
        n = len(arr)
        total_comparisons = 0
        
        for i in range(n // 2 - 1, -1, -1):
            _, comps = HeapSort._heapify(arr, n, i)
            total_comparisons += comps
            
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            _, comps = HeapSort._heapify(arr, i, 0)
            total_comparisons += comps
            
        return arr, total_comparisons


class RadixSort:
    @staticmethod
    def _counting_sort_for_radix(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        comparisons = 0

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]
            
        return arr, comparisons

    @staticmethod
    def sort(arr):
        if not arr:
            return arr, 0
            
        max_val = max(arr)
        exp = 1
        total_comparisons = 0
        
        while max_val // exp > 0:
            total_comparisons += 1 
            _, comps = RadixSort._counting_sort_for_radix(arr, exp)
            total_comparisons += comps
            exp *= 10
            
        return arr, total_comparisons


# ==========================================
# PHẦN 2: CẤU HÌNH VÀ UTILITIES
# ==========================================

# Ánh xạ tên thuật toán trên command line với method tĩnh của Class
ALGORITHMS = {
    "shaker-sort": ShakerSort.sort,
    "heap-sort": HeapSort.sort,
    "radix-sort": RadixSort.sort
    # Thêm các class thuật toán khác vào đây:
    # "selection-sort": SelectionSort.sort,
}

ORDER_MAP = {
    "-rand": 0,
    "-sorted": 1,
    "-rev": 2,
    "-nsorted": 3
}

ORDER_NAME = {
    "-rand": "Randomize",
    "-sorted": "Sorted",
    "-rev": "Reversed",
    "-nsorted": "Nearly Sorted"
}

def write_file(filename, arr):
    """Ghi dữ liệu ra file theo format yêu cầu: dòng 1 là N, dòng 2 là các phần tử."""
    with open(filename, "w") as f:
        f.write(f"{len(arr)}\n")
        f.write(" ".join(map(str, arr)))


# ==========================================
# PHẦN 3: XỬ LÝ CÁC LỆNH (COMMANDS)
# ==========================================

def handle_command_2(args):
    """
    Xử lý Command 2: > python groupid.py -a Algorithm Input_size Input_order Output_parameter
    """
    algorithm_name = args[2]
    input_size = int(args[3])
    input_order = args[4]
    output_param = args[5]

    data_type = ORDER_MAP.get(input_order, 0)
    arr = generate_data(input_size, data_type)
    
    write_file("input.txt", arr) # Ghi mảng đầu vào ra file

    print("ALGORITHM MODE")
    print(f"Algorithm: {algorithm_name}")
    print(f"Input size: {input_size}")
    print(f"Input order: {ORDER_NAME.get(input_order, 'Unknown')}")
    print("-------------------------")

    if algorithm_name not in ALGORITHMS:
        print(f"Error: Thuật toán {algorithm_name} chưa được hỗ trợ.")
        return
    
    sort_function = ALGORITHMS[algorithm_name]

    start_time = time.time()
    sorted_arr, comparisons = sort_function(arr.copy())
    end_time = time.time()

    running_time_ms = (end_time - start_time) * 1000

    write_file("output.txt", sorted_arr) # Ghi mảng đã sắp xếp ra file

    if output_param in ["-time", "-both"]:
        print(f"Running time: {running_time_ms:.2f} ms")
    if output_param in ["-comp", "-both"]:
        print(f"Comparisons: {comparisons}")


def handle_command_5(args):
    """
    Xử lý Command 5: > python groupid.py -c Algorithm_1 Algorithm_2 Input_size Input_order
    """
    algo1_name = args[2]
    algo2_name = args[3]
    input_size = int(args[4])
    input_order = args[5]

    data_type = ORDER_MAP.get(input_order, 0)
    arr = generate_data(input_size, data_type)

    write_file("input.txt", arr) # Ghi mảng đầu vào ra file

    print("COMPARE MODE")
    print(f"Algorithm: {algo1_name} | {algo2_name}")
    print(f"Input size: {input_size}")
    print(f"Input order: {ORDER_NAME.get(input_order, 'Unknown')}")
    print("-------------------------")

    if algo1_name not in ALGORITHMS or algo2_name not in ALGORITHMS:
        print("Error: Một trong các thuật toán so sánh chưa được cấu hình.")
        return

    sort_func1 = ALGORITHMS[algo1_name]
    sort_func2 = ALGORITHMS[algo2_name]

    # Thuật toán 1
    start_time1 = time.time()
    _, comp1 = sort_func1(arr.copy())
    time1_ms = (time.time() - start_time1) * 1000

    # Thuật toán 2
    start_time2 = time.time()
    _, comp2 = sort_func2(arr.copy())
    time2_ms = (time.time() - start_time2) * 1000

    print(f"Running time: {time1_ms:.2f} ms | {time2_ms:.2f} ms")
    print(f"Comparisons: {comp1} | {comp2}")


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python groupid.py [-a/-c] [arguments...]")
        return

    mode = args[1]

    if mode == "-a":
        if len(args) == 6 and args[3].isdigit():
            handle_command_2(args)
        else:
            print("Đang chạy logic của Command 1 hoặc Command 3 (Cần implement thêm).")

    elif mode == "-c":
        if len(args) == 6 and args[4].isdigit():
            handle_command_5(args)
        else:
            print("Đang chạy logic của Command 4 (Cần implement thêm).")
    else:
        print("Chế độ không hợp lệ. Sử dụng -a (Algorithm) hoặc -c (Comparison).")

if __name__ == "__main__":
    main()