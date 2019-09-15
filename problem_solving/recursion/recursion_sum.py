def sum_(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0]+sum_(arr[1:])


print(sum_([0, 100, 55, 44, 77, 99, 0, 0]))