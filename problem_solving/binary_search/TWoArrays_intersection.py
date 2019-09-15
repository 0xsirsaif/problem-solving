'''
Given two arrays, write a function to compute their intersection.

link : http://bit.ly/2XMlZk4
'''

# first solution


def arrays_intersection(arr1,arr2):
    return list(set(arr1) & set(arr2))

# second solution Do what set Do , get smallest item > sort arr > remove duplicates > get intersection


def get_smallest_item_inedx(arr):
    smallest_item = arr[0]
    smallest_item_index = 0
    for i in range(1,len(arr)):
        if smallest_item > arr[i]:
            smallest_item = arr[i]
            smallest_item_index = i
    return smallest_item_index


def sort_arr(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest_item_index = get_smallest_item_inedx(arr)
        sorted_arr.append(arr.pop(smallest_item_index))
    return sorted_arr


# another function to sort arr with QuickSort Algorithm that apply recursion (divide and conquer)
# def quicksort_(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#         greater = [i for i in arr[1:] if i > pivot]
#         return quicksort_(less) + [pivot] + quicksort_(greater)


def remove_duplicate_items(arr):
    arr = sort_arr(arr)
    non_duplicated_arr = []
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            non_duplicated_arr.append(arr[i])
            if i == len(arr)-2:
                if arr[-1] > arr[i]:
                    non_duplicated_arr.append(arr[-1])
    return non_duplicated_arr


def get_intersection(arr_1,arr_2):
    arr_1 = remove_duplicate_items(arr_1)
    arr_2 = remove_duplicate_items(arr_2)

    if len(arr_2) > len(arr_1):
        short_list = arr_1
        long_list = arr_2
    elif len(arr_1) > len(arr_2):
        short_list = arr_2
        long_list = arr_1
    else:
        short_list = arr_1
        long_list = arr_2
    intersect_element = []
    print(long_list)
    print(short_list)
    for i in short_list:
        if i in long_list:
            intersect_element.append(i)
    return intersect_element


print(get_intersection([100,5,4,79,3,1,2,2,2,4,7,8,0,-1,-100,-45,-45,7,8,0],[4,7,8,0,-1,-100,-45,-45,7,8,0]))