from sorting_algorithms import *
from file_io import *
from data_generator import *
import sys
def command_1(algo_name: str, input_file: str, output_param: str):
    pass


def command_2(algo_name: str, input_size: int, input_order: str, output_param: str):
    pass


def command_3(algo_name: str, input_size: int, output_param: str):
    pass


def command_4(algo_1: str, algo_2: str, input_file: str):
    pass


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