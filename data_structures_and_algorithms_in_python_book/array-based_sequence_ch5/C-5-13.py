from sys import getsizeof


def list_size(n):
    """ either we begin with an empty or non-empty list,
     the sequence of values at which the array is expanding does not change"""
    A = [None,None,None,None,None,]
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