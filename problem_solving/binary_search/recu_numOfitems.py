def count_(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    else:
        return 1 + count_(arr[1:])


print(count_([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]))