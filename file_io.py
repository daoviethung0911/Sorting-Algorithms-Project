def read_input_file(filename: str):
    with open(filename, 'r', encoding = 'utf-8') as f:
        f.readline()
        data = [int(x) for x in f.readline().split()]
    return data

def write_output_file(filename: str, data: list[int]):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write(f'{len(data)}\n')
        f.write(' '.join(map(str, data)))
