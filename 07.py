from sorting_algorithms import *
from file_io import *
from data_generator import *
import sys
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


def command_2(algo_name: str, input_size: int, input_order: str, output_param: str):
    pass


def command_3(algo_name: str, input_size: int, output_param: str):
    print("ALGORITHM MODE")
    print(f"Algorithm: {algo_name}")
    print(f"Input size: {input_size}")
    print("-------------------------")

    if algo_name not in sorting_map:
        print(f"Lỗi: Không tìm thấy thuật toán '{algo_name}' trong hệ thống!")
        return
    sort_function = sorting_map[algo_name]

    for order in ["random", "nearly-sorted", "sorted", "reverse"]:
        print(f"Input order: {order}")
        print('-------------')
        arr = generate_data_v2(input_size, data_type=order)
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


def command_5(algo_1: str, algo_2: str, input_size: int, input_order: str):
    pass


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
            command_2(inp[2], int(inp[3]), inp[4], inp[5])
    else:
        if len(inp) == 5:
            command_4(inp[2], inp[3], inp[4])
        else:
            command_5(inp[2], inp[3], int(inp[4]), inp[5])


if __name__ == '__main__':
    main()
