from sys import getsizeof


def monitor_array_size():
    arr = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    for i in range(len(arr)):
        print("", "array length : {0}, array size : {1}".format(len(arr), getsizeof(arr)))
        arr.pop()

monitor_array_size()
