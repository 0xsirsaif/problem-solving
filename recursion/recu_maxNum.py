def get_max(arr):

    if len(arr) == 0:
        return 'no item'
    elif len(arr) == 1:
        return 'max num is {}'.format(arr[0])
    else:
        if arr[1] > arr[0]:
            return get_max(arr[1:])
        else:
            arr.pop(arr.index(arr[1]))
            return get_max(arr)


print(get_max([4,2000,3,100,1000,6]))