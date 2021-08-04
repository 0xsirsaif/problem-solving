"""
Write a short recursive Python function that finds the minimum and
maximum values in a sequence without using any loops.
"""

def find_min_max(arr,n):
    if n == 0:
        return arr[0], arr[0]
    else:
        (num1,num2) = find_min_max(arr, n-1)
        if arr[n] < num1:
            if arr[n] < num2:
                return num1, arr[n]
        return arr[n], num2

arr = [-10,0,2,3,5,-2,1,10,4,100]
print(find_min_max(arr,len(arr)-1))