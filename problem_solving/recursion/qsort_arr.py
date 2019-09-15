def quicksort_(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort_(less) + [pivot] + quicksort_(greater)


print(quicksort_([0,1,5,6,3,9,8,7,4,11,12,45,98,32,0]))