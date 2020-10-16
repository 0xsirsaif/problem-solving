from collections import Counter
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def _binary_search(arr, start, end, num):
            if start > end:
                return [-1, -1]

            mid = (start + end) // 2

            if arr[mid] == num:
                counter = dict(Counter(arr))
                before_target = sum([counter[x] for x in counter if x < num])
                after_target = len(arr) - before_target - counter[num]
                return [before_target, len(arr) - after_target - 1]
            elif num > arr[mid]:
                return _binary_search(arr, mid + 1, end, num)
            elif num < arr[mid]:
                return _binary_search(arr, start, mid - 1, num)

        return _binary_search(nums, 0, len(nums)-1, target)


A = [1]
s = Solution()
print(s.searchRange(A, 1))