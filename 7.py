from sorting_algorithms import *
from file_io import *
from data_generator import *
import sys
import threading
sys.setrecursionlimit(1000000000)
def command_1(algo_name: str, input_file: str, output_param: str):
    arr = read_input_file(input_file)
    input_size = len(arr)
    print("ALGORITHM MODE")
    print(f"Algorithm: {algo_name}")
    print(f"Input file: {input_file}")
    print(f"Input size: {input_size}")
    print("-------------------------")

    if algo_name not in sorting_map:
        print(f"Lỗi: Không tìm thấy thuật toán '{algo_name}' trong hệ thống!")
        return
    sort_function = sorting_map[algo_name]
    sorted_arr, time_comps = sort_function(arr)
    exec_time, comps = time_comps

    if output_param == "-time":
        print(f"Running time (if required): {exec_time:.4f}")
    if output_param == "-comp":
        print(f"Comparisons (if required): {comps}")
    if output_param == "-both":
        print(f"Running time (if required): {exec_time:.4f}")
        print(f"Comparisons (if required): {comps}")
        
    write_output_file("output.txt", sorted_arr)


def command_2(args):
    """
    Xử lý Command 2: > python groupid.py -a Algorithm Input_size Input_order Output_parameter
    """
    algorithm_name = args[2]
    input_size = int(args[3])
    input_order = args[4]
    output_param = args[5]

    data_type = ORDER_MAP.get(input_order, 0)
    arr = generate_data(input_size, data_type)
    
    write_output_file("input.txt", arr) # Ghi mảng đầu vào ra file

    print("ALGORITHM MODE")
    print(f"Algorithm: {algorithm_name}")
    print(f"Input size: {input_size}")
    print(f"Input order: {ORDER_NAME.get(input_order, 'Unknown')}")
    print("-------------------------")

    if algorithm_name not in sorting_map:
        print(f"Error: Thuật toán {algorithm_name} chưa được hỗ trợ.")
        return
    
    sort_function = sorting_map[algorithm_name]

    tmp = sort_function(arr)
    sorted_arr, running_time_ms, comparisons = tmp[0], tmp[1][0], tmp[1][1]
    
    write_output_file("output.txt", sorted_arr) # Ghi mảng đã sắp xếp ra file

    if output_param in ["-time", "-both"]:
        print(f"Running time: {running_time_ms:.2f} ms")
    if output_param in ["-comp", "-both"]:
        print(f"Comparisons: {comparisons}")


def command_3(algo_name: str, input_size: int, output_param: str):
    print("ALGORITHM MODE")
    print(f"Algorithm: {algo_name}")
    print(f"Input size: {input_size}")
    print("-------------------------")

    if algo_name not in sorting_map:
        print(f"Lỗi: Không tìm thấy thuật toán '{algo_name}' trong hệ thống!")
        return
    sort_function = sorting_map[algo_name]

    for order in ["Randomize", "Nearly Sorted", "Sorted", "Reversed"]:
        print(f"Input order: {order}")
        print('-------------')
        arr = generate_data(input_size, data_type=ORDER_MAP_2[order])
        if order == "Randomize":
            write_output_file("input1.txt", arr)
        elif order == "Nearly Sorted":
            write_output_file("input2.txt", arr)            
        elif order == "Sorted":
            write_output_file("input3.txt", arr)            
        elif order == "Reversed":
            write_output_file("input4.txt", arr)            
        sorted_arr, time_comps = sort_function(arr)
        exec_time, comps = time_comps
        if output_param == "-time":
            print(f"Running time (if required): {exec_time:.4f}")
            print()
        if output_param == "-comp":
            print(f"Comparisons (if required): {comps}")
            print()
        if output_param == "-both":
            print(f"Running time (if required): {exec_time:.4f}")
            print(f"Comparisons (if required): {comps}")
            print()


def command_4(algo_1: str, algo_2: str, input_file: str):
    arr = read_input_file(input_file)
    input_size = len(arr)
    if algo_1 not in sorting_map :
        print(f"Lỗi: Không tìm thấy thuật toán '{algo_1}' trong hệ thống!")
        return
    if algo_2 not in sorting_map :
        print(f"Lỗi: Không tìm thấy thuật toán '{algo_2}' trong hệ thống!")
        return

    sort_function_1 = sorting_map[algo_1]
    sort_function_2 = sorting_map[algo_2]
    sorted_arr_1, time_comps_1 = sort_function_1(arr)
    time1, comps1 = time_comps_1
    sorted_arr_2, time_comps_2 = sort_function_2(arr)
    time2, comps2 = time_comps_2

    print("COMPARE MODE")
    print(f"Algorithm: {algo_1} | {algo_2}")
    print(f"Input file: {input_file}")
    print(f"Input size: {input_size}")
    print("-------------------------")
    print(f"Running time: {time1:.4f} | {time2:.4f}")
    print(f"Comparisons: {comps1} | {comps2}")


def command_5(args):
    """
    Xử lý Command 5: > python groupid.py -c Algorithm_1 Algorithm_2 Input_size Input_order
    """
    algo1_name = args[2]
    algo2_name = args[3]
    input_size = int(args[4])
    input_order = args[5]

    data_type = ORDER_MAP.get(input_order, 0)
    arr = generate_data(input_size, data_type)

    write_output_file("input.txt", arr) # Ghi mảng đầu vào ra file

    print("COMPARE MODE")
    print(f"Algorithm: {algo1_name} | {algo2_name}")
    print(f"Input size: {input_size}")
    print(f"Input order: {ORDER_NAME.get(input_order, 'Unknown')}")
    print("-------------------------")

    if algo1_name not in sorting_map or algo2_name not in sorting_map:
        print("Error: Một trong các thuật toán so sánh chưa được cấu hình.")
        return

    sort_func1 = sorting_map[algo1_name]
    sort_func2 = sorting_map[algo2_name]

    # Thuật toán 1
    tmp = sort_func1(arr)
    comp1 = tmp[1][1]
    time1_ms = tmp[1][0]

    # Thuật toán 2
    tmp = sort_func2(arr)
    comp2 = tmp[1][1]
    time2_ms = tmp[1][0]

    print(f"Running time: {time1_ms:.2f} ms | {time2_ms:.2f} ms")
    print(f"Comparisons: {comp1} | {comp2}")


def main():
    inp = sys.argv
    if len(inp) < 5:
        print('Đầu vào lỗi')
        return
    mode = inp[1]
    if mode == '-a':
        if len(inp) == 5:
            if inp[3].isdigit():
                command_3(inp[2], int(inp[3]), inp[4])
            else:
                command_1(inp[2], inp[3], inp[4])
        else:
            command_2(inp)
    else:
        if len(inp) == 5:
            command_4(inp[2], inp[3], inp[4])
        else:
            command_5(inp)


if __name__ == '__main__':
    # 2. Ép Windows cấp phát 128MB cho Stack (Đơn vị là Byte: 128 * 1024 * 1024)
    threading.stack_size(134217728)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()

