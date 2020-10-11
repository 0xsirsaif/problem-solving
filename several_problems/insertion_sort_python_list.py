def insertion_sort(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i+1] < arr[i]:
            left_curr = find_position(arr[:i+1], arr[i+1])
            arr[:len(left_curr)] = left_curr
        i += 1
    return arr

def find_position(arr, num):
    start, end, idx = 0, len(arr)-1, None
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == num:
            arr.insert(mid, num)
            return arr
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    else:
        if arr[mid] >= num:
            arr.insert(mid, num)
        else:
            arr.insert(mid+1, num)

    return arr

print(insertion_sort([0,1,-1,-2,-10,4,5,8,7,10,14,-100]))