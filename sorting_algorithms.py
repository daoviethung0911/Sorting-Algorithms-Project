#Mỗi cái sort return running time và number of comparisons ở dạng tuple cho đồng bộ nha mn  sorted_array, (time, comp). (Time đơn vị ms nha)
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


def binary_insertion_sort(L: list):
    pass


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
    pass


import time

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
    pass


def merge_sort(L: list):
    pass


def quick_sort(L: list):
    pass


def counting_sort(L: list):
    arr = L.copy()
    comparisons = 0
    start_time = time.perf_counter()

    if not arr:
        return [], (0, 0.0)
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
    pass


def flash_sort(L: list):
    arr = L.copy()
    comparisons = 0
    start_time = time.perf_counter()

    if not arr:
        return [], (0, 0.0)

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
        return arr, (comparisons, (end_time - start_time) * 1000)

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
