from collections import Counter

def find_target(arr, start, end, target):
    if start > end-1:
        return False

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return find_target(arr, mid + 1, end, target)
    elif target < arr[mid]:
        return find_target(arr, start, mid - 1, target)


A = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(find_target(A, 0, len(A), 1))
