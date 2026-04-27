import random

def generate_random_data(n):
    """Generates an array with random values between 0 and n-1."""
    return [random.randint(0, n - 1) for _ in range(n)]

def generate_sorted_data(n):
    """Generates an array with values sorted in ascending order."""
    return list(range(n))

def generate_reverse_data(n):
    """Generates an array with values sorted in descending order."""
    return list(range(n - 1, -1, -1))

def generate_nearly_sorted_data(n):
    """Generates a sorted array and performs 10 random swaps."""
    a = list(range(n))
    for _ in range(10):
        r1 = random.randint(0, n - 1)
        r2 = random.randint(0, n - 1)
        # Python's clean way to swap two elements
        a[r1], a[r2] = a[r2], a[r1]
    return a

def generate_data(n, data_type):
    """Main function to generate data based on type."""
    if data_type == 0:
        return generate_random_data(n)
    elif data_type == 1:
        return generate_sorted_data(n)
    elif data_type == 2:
        return generate_reverse_data(n)
    elif data_type == 3:
        return generate_nearly_sorted_data(n)
    else:
        print("Error: unknown data type!")
        return None

def generate_data_v2(n, data_type):
    """Main function to generate data based on type."""
    #["Randomize", "Nearly Sorted", "Sorted", "Reversed"]
    if data_type == "Randomize":
        return generate_random_data(n)
    elif data_type == "Sorted":
        return generate_sorted_data(n)
    elif data_type == "Reversed":
        return generate_reverse_data(n)
    elif data_type == "Nearly Sorted":
        return generate_nearly_sorted_data(n)
    else:
        print("Error: unknown data type!")
        return None
# Usage example:
# n = 10
# random_array = generate_data(n, 0)
# print(random_array)
