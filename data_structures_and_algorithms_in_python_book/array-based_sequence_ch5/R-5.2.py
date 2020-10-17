from sys import getsizeof

def list_size(n):
    A = []
    reallocate = -1
    for k in range(n):
        arr_memory_usage = getsizeof(A)
        num_elements = (arr_memory_usage - 64)//8
        if num_elements != reallocate:
            print(num_elements)
            reallocate = num_elements
        A.append(None)

list_size(30)