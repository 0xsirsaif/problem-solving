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
    return arr

# print(insertion_sort([5,4,3,2,1]))

# Better and simpler solution
def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i
        while j > 0 and arr[j-1] > curr:
            print("J :", j, "J-1 :", arr[j-1])
            arr[j] = arr[j-1]
            j -= 1
        print("J :", j)
        arr[j] = curr
        print("==========")
    return arr

print(insertion_sort_2([5,4,3,2,1]))