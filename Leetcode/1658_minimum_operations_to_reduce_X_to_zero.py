from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        def _recur(arr, node, right, n_steps, result, flag):
            print(node)
            if node < len(arr):
                pass
            return -1

        _recur(nums, 0, len(nums)-1, 1, x, False)
        return 0


s = Solution()
print(s.minOperations([1,1,4,2,3], 5))