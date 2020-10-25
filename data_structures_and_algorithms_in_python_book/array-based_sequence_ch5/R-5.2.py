from sys import getsizeof


def list_size(n):
    """
    Python is not using a pure geometric progression, nor is it using arithmetic progression
    """
    A = []
    reallocate = -1
    for k in range(n):
        arr_len = len(A)
        arr_memory_usage = getsizeof(A)
        num_elements = (arr_memory_usage - 64)//8
        if num_elements != reallocate:
            print(num_elements)
            reallocate = num_elements
        print("Length: {0: 3d}; Size in bytes: {1: 4d}".format(arr_len, arr_memory_usage))
        A.append(None)

list_size(30)