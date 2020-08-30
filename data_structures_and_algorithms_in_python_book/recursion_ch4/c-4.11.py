"""
Describe an efficient recursive function for solving the element uniqueness
problem, which runs in time that is at most O(n2) in the worst case
without using sorting.
"""

arr = [10,0,3,45,405,4005,1000,1000]

def check_uniqueness(arr,element,index):
    if index == 0:
        if element == 1:
            if arr[1] == arr[0]:
                return "NOT UNIQUE"
            return "UNIQUE"
        else:
            if arr[element] == arr[0]:
                return "NOT UNIQUE"
            return arr[element-1]
    else:
        for i in range(1, index + 2):
            second = check_uniqueness(arr, element, index - 1)
            if second == "NOT UNIQUE":
                break
            else:
                if arr[element] == second:
                    return "NOT UNIQUE"
                else:
                    if index == element-1:
                        return check_uniqueness(arr,element-1,element-2)
                    else:
                        return arr[index]
        return "NOT UNIQUE"

arr_len = len(arr)-1
print(check_uniqueness(arr,arr_len,arr_len-1))
