# Algorithm 1 By shifting
def shifting_insertion_sort(arr):
    for i in range(1, len(arr)):
        hand = arr[i]
        j = i-1
        while j >= 1 and arr[j] > hand:
            arr[j+1] = arr[j]
            j -= 1
        else:
            if hand > arr[j]:
                arr[j+1] = hand
            else:
                arr[j+1] = arr[j]
                arr[j] = hand
    return arr

# Algorithm 2 using binary search
def insertion_sort(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i+1] < arr[i]:
            left_curr = find_position(arr[:i+1], arr[i+1])
            arr[:len(left_curr)] = left_curr
        i += 1
    return arr

def find_position(arr, num):
    start, end = 0, len(arr)-1
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