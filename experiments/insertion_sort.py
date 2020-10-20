# Exchanging
def insertion_sort(arr):
    for i in range(1, len(arr)):
        hand = arr[i]
        j = i-1
        while j >= 1 and arr[j] > hand:
            arr[j+1] = arr[j]
            j -= 1
        else:
            print(j, hand, arr[j])
            if hand > arr[j]:
                arr[j+1] = hand
            else:
                arr[j+1] = arr[j]
                arr[j] = hand
        print(arr)
    return arr

print(insertion_sort([5,4,3,2,1]))