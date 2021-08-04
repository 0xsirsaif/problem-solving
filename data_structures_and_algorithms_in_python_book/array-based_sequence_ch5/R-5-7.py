# using insertion sort until reach to the repeated int
def insertion_sort(arr):
    for i in range(1, len(arr)):
        hand = arr[i]
        j = i-1
        while j >= 1 and arr[j] > hand:
            arr[j+1] = arr[j]
            j -= 1
        else:
            if hand == arr[j]:
                return hand
            if hand > arr[j]:
                arr[j+1] = hand
            else:
                arr[j+1] = arr[j]
                arr[j] = hand

    return False