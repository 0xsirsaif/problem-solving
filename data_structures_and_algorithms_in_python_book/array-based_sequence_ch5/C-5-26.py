def find_repeated(arr):
    _dict = {x: 0 for x in arr}
    for i in arr:
        _dict[i] += 1
        if _dict[i] == 5:
            return i
    return False

print(find_repeated([1,1,1,1,1,5]))