from typing import List
import bisect
from sortedcontainers import SortedList


# using bisect module
class Solution1:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        ans = 0
        for i in instructions:
            left = bisect.bisect_left(nums, i)
            right = len(nums) - bisect.bisect_right(nums, i)
            ans += min(left, right)
            bisect.insort(nums, i)
        return ans % (10**9 + 7)


# using SortedContainers module
class Solution2:
    def createSortedArray(self, instructions: List[int]) -> int:
        sorted_list = SortedList()
        ans = 0
        for i in instructions:
            ans += min(sorted_list.bisect_left(i), len(sorted_list) - sorted_list.bisect_right(i))
            sorted_list.add(i)
        return ans % (100**9 + 7)


# FAILED in the last test case because the time limit exceeded
# for every update operation we need to update all cells depending on that call
# so we need to optimize the update method -> BIT Data Structure
# get function ->
# overall time complexity -> O(n^2)
class Solution3:
    def createSortedArray(self, instructions: List[int]) -> int:
        def get(x):
            res = 0
            for i in range(x + 1):
                res += new_arr[i]
            return res

        def update(x):
            for i in range(x, new_len + 1):
                new_arr[i] += 1

        new_len = max(instructions)
        new_arr = [0] * (new_len + 1)

        ans = 0
        for idx, num in enumerate(instructions):
            ans += min(get(num - 1), get(new_len) - get(num))
            update(num)

        return ans % (10**9 + 7)


# make use of BIT Data Structure -> efficiently update array values O(log n)
# overall time complexity -> O(n log n)
class Solution5:
    def createSortedArray(self, instructions: List[int]) -> int:
        def get(x):
            res = 0
            while x > 0:
                res += tree[x]
                x -= x & -x
            return res

        def update(x):
            while x <= new_len:
                tree[x] += 1
                x += x & -x

        new_len = max(instructions)
        tree = [0] * (new_len + 1)

        ans = 0
        for idx, num in enumerate(instructions):
            ans += min(get(num - 1), get(new_len) - get(num))
            update(num)
        return ans % (10**9 + 7)