"""
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.
You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.
The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.
The large sum is the maximal sum of any block.
For example, you are given integers K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:
[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.
Write a function:
def solution(K, M, A)
that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.
For example, given K = 3, M = 5 and array A such that:
  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.
Write an efficient algorithm for the following assumptions:
N and K are integers within the range [1..100,000];
M is an integer within the range [0..10,000];
each element of array A is an integer within the range [0..M].
"""

# function (block_nums) to get the NUM of arrays that can be produced
# from the original Array where the sum of each of these blocks
# are less than or Equal to the Specific NUM (mid num in Binary Search)

def block_nums(arr, max_block):
    num_of_arrs = 1
    pre_arr_sum = arr[0]
    for i in arr[1:]:
        if pre_arr_sum + i > max_block:
            if pre_arr_sum <= max_block:
                pre_arr_sum = i
                num_of_arrs += 1
            else:
                pre_arr_sum = i
        else:
            pre_arr_sum += i
    if num_of_arrs == 1 and max_block not in arr:
        return 0
    return num_of_arrs


# this Function make a Binary search over [max >> sum]
def minimal_large_sum(arr,block_num):
    start = max(arr)
    end = sum(arr)
    result = 0
    if block_num == 1:
        return end
    if block_num >= len(arr):
        return start
    while end >= start:
        mid = round((end+start)/2)
        mid_block_num = block_nums(arr,mid)
        if mid_block_num <= block_num:
            end = mid-1
            result = mid
        else:
            start = mid+1
    return result


print(minimal_large_sum([2, 1, 5, 1, 2, 2, 2],4))