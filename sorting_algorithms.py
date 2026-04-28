#Mỗi cái sort return running time và number of comparisons ở dạng tuple cho đồng bộ nha mn  sorted_array, (time, comp). (Time đơn vị ms nha)
#Nhớ đếm cả so sánh của for while luôn nha mn.
import time
def selection_sort(L: list):
    arr = L.copy()
    comparisons = 0
    start_time = time.perf_counter()

    n = len(arr)
    i = 0

    while i < n:
        comparisons += 1
        min_idx = i
        j = i + 1
        while j < n:
            comparisons += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
            j += 1
            comparisons += 1
        comparisons += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        i += 1
    comparisons += 1
    
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    return arr, (execution_time, comparisons)


def insertion_sort(L: list):
    data = L.copy()
    start_time = time.perf_counter()
    cmp_cnt = 0
    n = len(data)
    for i in range(1, n):
        cmp_cnt += 1
        tmp = data[i]
        j = i - 1
        while True:
            cmp_cnt += 1 
            if j >= 0:
                cmp_cnt += 1 
                if tmp < data[j]:
                    data[j + 1] = data[j]
                    j -= 1
                else:
                    break
            else:
                break
        data[j + 1] = tmp
    cmp_cnt += 1 
    end_time = time.perf_counter()
    running_time = (end_time - start_time) * 1000
    return data, (running_time, cmp_cnt)

def binary_search(arr, val, start, end, cnt):
    cnt[0] += 1
    if start == end:
        cnt[0] += 1
        if arr[start] > val:
            return start
        else:
            return start + 1

    cnt[0] += 1
    if start > end:
        return start

    mid = (start + end) // 2
    
    cnt[0] += 1
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end, cnt)
    else:
        cnt[0] += 1
        if arr[mid] > val:
            return binary_search(arr, val, start, mid - 1, cnt)
        else:
            return mid
        
def binary_insertion_sort(L: list):
    data = L.copy()
    start_time = time.perf_counter()
    cmp_cnt = [0]
    
    for i in range(1, len(data)):
        cmp_cnt[0] += 1
        val = data[i]
        
        # Tìm vị trí chèn bằng Binary Search
        j = binary_search(data, val, 0, i - 1, cmp_cnt)
        
        data = data[:j] + [val] + data[j:i] + data[i+1:]
        
    cmp_cnt[0] += 1 # Lần kiểm tra kết thúc vòng lặp for
    
    end_time = time.perf_counter()
    running_time = end_time - start_time

    return data, (running_time * 1000, cmp_cnt[0])


def bubble_sort(L: list):
    data = L.copy()
    start_time = time.perf_counter()
    cmp_cnt = 0
    n = len(L)
    for i in range(0, n):
        cmp_cnt += 1
        for j in range(0, n - i - 1):
            cmp_cnt += 2
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        cmp_cnt += 1
    cmp_cnt += 1
    end_time = time.perf_counter()
    running_time = end_time - start_time
    return data, (running_time * 1000, cmp_cnt)


def shaker_sort(L: list):
    arr = L.copy()
    start_time = time.perf_counter()
    n = len(arr)
    comparisons = 0
    left = 0
    right = n - 1
    k = 0
    comparisons += 1
    while left < right:
        comparisons += 1
        for i in range(left, right):
            comparisons += 2
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                k = i
        right = k
        comparisons += 1
        for i in range(right, left, -1):
            comparisons += 2
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                k = i
        left = k
        comparisons += 1
    end_time = time.perf_counter()
    running_time = (end_time - start_time) * 1000
    return arr, (running_time, comparisons)


def shell_sort(L: list):
    data = L.copy()
    start_time = time.perf_counter()
    cmp_cnt = 0
    n = len(data)
    gap = n // 2
    while gap > 0:
        cmp_cnt += 1
        for i in range(gap, n):
            cmp_cnt += 1
            tmp = data[i]
            j = i
            while True:
                cmp_cnt += 1
                if j >= gap:
                    cmp_cnt += 1
                    if data[j - gap] > tmp:
                        data[j] = data[j - gap]
                        j -= gap
                    else:
                        break
                else:
                    break
            data[j] = tmp
        gap //= 2
    cmp_cnt += 1
    end_time = time.perf_counter()
    running_time = (end_time - start_time) * 1000
    return data, (running_time, cmp_cnt)


def heap_sort(L: list):
    def _heapify(arr, n, i):
        comparisons = 0
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        comparisons += 1
        if left < n:
            comparisons += 1
            if arr[left] > arr[largest]:
                largest = left
        comparisons += 1
        if right < n:
            comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            comparisons += 1
            arr[i], arr[largest] = arr[largest], arr[i]
            _, comp_recursive = _heapify(arr, n, largest)
            comparisons += comp_recursive
        return arr, comparisons
    
    arr = L.copy()
    start_time = time.perf_counter()
    n = len(arr)
    total_comparisons = 0
    total_comparisons += 1
    for i in range(n // 2 - 1, -1, -1):
        total_comparisons += 1
        _, comps = _heapify(arr, n, i)
        total_comparisons += comps
    total_comparisons += 1
    for i in range(n - 1, 0, -1):
        total_comparisons += 1
        arr[i], arr[0] = arr[0], arr[i]
        _, comps = _heapify(arr, i, 0)
        total_comparisons += comps   
    end_time = time.perf_counter()
    running_time = (end_time - start_time) * 1000
    return arr, (running_time, total_comparisons)


def merge(arr1, arr2, arr, cnt):
    i = j = 0
    cnt[0] += 1
    while i + j < len(arr):
        cnt[0] += 1 
        if j == len(arr2):
            arr[i+j] = arr1[i]
            i += 1
        else:
            cnt[0] += 1
            if i < len(arr1):
                cnt[0] += 1
                if arr1[i] < arr2[j]:
                    arr[i+j] = arr1[i]
                    i += 1
                else:
                    arr[i+j] = arr2[j]
                    j += 1
            else:
                arr[i+j] = arr2[j]
                j += 1    
        cnt[0] += 1

def merge_sort_add(arr, cnt):
    cnt[0] += 1
    if len(arr) <= 1:
        return
    
    n = len(arr)
    arr1 = arr[:n//2]
    arr2 = arr[n//2:]
    
    merge_sort_add(arr1, cnt)
    merge_sort_add(arr2, cnt)
    merge(arr1, arr2, arr, cnt)

def merge_sort(L: list):
    data = L.copy()
    start_time = time.perf_counter()
    cmp_cnt = [0] 

    merge_sort_add(data, cmp_cnt)
    
    end_time = time.perf_counter()
    running_time = end_time - start_time
    return data, (running_time * 1000, cmp_cnt[0])


def partitional_hoare(arr, low, high, cnt):
    i, j = low - 1, high + 1
    # Randomized Quick Sort
    # tránh trường hợp xấu nhất O(N^2) khi mảng đã được sort sẵn.
    # rd_idx = random.randint(low, high)
    # arr[low], arr[rd_idx] = arr[rd_idx], arr[low]
    p = arr[low]
    while True: 
        while True: # Tìm phần tử bên trái lớn hơn hoặc bằng pivot
            i += 1
            cnt[0] += 1
            if arr[i] >= p:
                break
        while True: # Tìm phần tử bên phải nhỏ hơn hoặc bằng pivot
            j -= 1
            cnt[0] += 1
            if arr[j] <= p:
                break
        cnt[0] += 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    return j

def quick_sort_hoare(arr, low, high, cnt):
    cnt[0] += 1
    if low >= high:
        return
        
    pivot = partitional_hoare(arr, low, high, cnt)
    quick_sort_hoare(arr, low, pivot, cnt)
    quick_sort_hoare(arr, pivot + 1, high, cnt)      
    
def quick_sort(L: list):
    data = L.copy()
    start_time = time.perf_counter()
    
    cmp_cnt = [0] 
    quick_sort_hoare(data, 0, len(data) - 1, cmp_cnt)
    end_time = time.perf_counter()
    running_time = end_time - start_time
    return data, (running_time * 1000, cmp_cnt[0])


def counting_sort(L: list):
    arr = L.copy()
    comparisons = 0
    start_time = time.perf_counter()

    if not arr:
        return [], (0.0, 0)
    n = len(arr)
    Maxval = -1
    for i in arr:
        comparisons += 1
        comparisons += 1
        if i > Maxval:
            Maxval = i
    comparisons += 1
    cont = [0] * (Maxval + 1) 
    result = [0] * n
    for i in arr:
        comparisons += 1
        cont[i] += 1
    comparisons += 1
    for i in range(1, Maxval + 1):
        comparisons += 1
        cont[i] += cont[i - 1]
    comparisons += 1
    for i in range(n - 1, -1, -1):
        comparisons += 1
        result[cont[arr[i]] - 1] = arr[i]
        cont[arr[i]] -= 1
    comparisons += 1
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    return result, (execution_time, comparisons)


def radix_sort(L: list):
    arr = L.copy()
    def _counting_sort_for_radix(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        comparisons = 0
        comparisons += 1
        for i in range(n):
            comparisons += 1
            index = arr[i] // exp
            count[index % 10] += 1
        comparisons += 1
        for i in range(1, 10):
            comparisons += 1
            count[i] += count[i - 1]

        i = n - 1
        comparisons += 1
        while i >= 0:
            comparisons += 1
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        comparisons += 1
        for i in range(n):
            comparisons += 1
            arr[i] = output[i]
            
        return arr, comparisons
    start_time = time.perf_counter()
    if not arr:
        return arr, (0.0, 0)
    max_val = max(arr)
    total_comparisons = 0
    total_comparisons += (2 * len(arr) - 1)
    exp = 1
    while max_val // exp > 0:
        total_comparisons += 1 
        _, comps = _counting_sort_for_radix(arr, exp)
        total_comparisons += comps
        exp *= 10
    total_comparisons += 1
    end_time = time.perf_counter()
    running_time = (end_time - start_time) * 1000
    return arr, (running_time, total_comparisons)


def flash_sort(L: list):
    arr = L.copy()
    comparisons = 0
    start_time = time.perf_counter()

    if not arr:
        return [], (0.0, 0)

    n = len(arr)
    
    min_val = arr[0]
    max_idx = 0
    i = 1
    
    while i < n:
        comparisons += 1
        comparisons += 1
        if arr[i] < min_val:
            min_val = arr[i]
            
        comparisons += 1
        if arr[i] > arr[max_idx]:
            max_idx = i
            
        i += 1
    comparisons += 1

    max_val = arr[max_idx]
    
    comparisons += 1
    if min_val == max_val:
        end_time = time.perf_counter()
        return arr, ((end_time - start_time) * 1000, comparisons)
    if n <= 2:
        comparisons += 1
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        end_time = time.perf_counter()
        return arr, ((end_time - start_time) * 1000, comparisons)
    m = int(0.45 * n) 
    L = [0] * m
    
    i = 0
    while i < n:
        comparisons += 1
        k = int((m - 1) * (arr[i] - min_val) / (max_val - min_val))
        L[k] += 1
        i += 1
    comparisons += 1
    
    i = 1
    while i < m:
        comparisons += 1
        L[i] += L[i - 1]
        i += 1
    comparisons += 1

    count = 0
    j = 0
    k = int((m - 1) * (arr[j] - min_val) / (max_val - min_val))
    
    while count < n - 1:
        comparisons += 1
        
        while j > L[k] - 1:
            comparisons += 1
            j += 1
            k = int((m - 1) * (arr[j] - min_val) / (max_val - min_val))
        comparisons += 1
        
        flash = arr[j]
        while j != L[k]:
            comparisons += 1
            k = int((m - 1) * (flash - min_val) / (max_val - min_val))
            L[k] -= 1
            arr[L[k]], flash = flash, arr[L[k]]
            count += 1
        comparisons += 1
    comparisons += 1

    i = 1
    while i < n:
        comparisons += 1
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
                
        if j < 0:
            comparisons += 1
            
        arr[j + 1] = key
        i += 1
    comparisons += 1

    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    
    return arr, (execution_time, comparisons)


sorting_map = {
    'selection-sort': selection_sort,
    'insertion-sort': insertion_sort,
    'binary-insertion-sort': binary_insertion_sort,
    'bubble-sort': bubble_sort,
    'shaker-sort': shaker_sort,
    'shell-sort': shell_sort,
    'heap-sort': heap_sort,
    'merge-sort': merge_sort,
    'quick-sort': quick_sort,
    'counting-sort': counting_sort,
    'radix-sort': radix_sort,
    'flash-sort': flash_sort,
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