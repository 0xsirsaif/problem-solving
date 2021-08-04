def add_two_dimensional_elements(arr, pair1, pair2, res, count):
    """
    we call that function (n//2)+1 calls instead of n*n calls.
    running time = O(n)
    """
    print(count)
    # break
    if pair1 == pair2:
        meet_point = pair1[0]
        res += arr[meet_point][meet_point]
        return res

    elif pair1[0] - pair2[0] == 1:
        return res

    x1, y1 = pair1
    x2, y2 = pair2
    res += array[x1][y1] + array[x2][y2]

    # change x
    if y1 == 0 and y2 == len(arr) - 1:
        x1 += 1
        y1 = len(array)
        x2 -= 1
        y2 = -1

    y1 -= 1
    y2 += 1

    return add_two_dimensional_elements(arr, (x1, y1), (x2, y2), res, count+1)


array = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],

]
array_len = len(array) - 1
print(add_two_dimensional_elements(array, (0, array_len), (array_len, 0), 0, 1))
