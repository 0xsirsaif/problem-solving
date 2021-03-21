from typing import List


class Solution:
    """
    Time Complexity => O(N)
    Space Complexity => O(N)
    """
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum = 0
        _sum = 0
        for i in range(len(nums)):
            if nums[i] <= nums[i - 1]:
                maximum = _sum if _sum > maximum else maximum
                _sum = 0
            _sum += nums[i]
        return _sum if _sum > maximum else maximum

S = Solution()
print(S.maxAscendingSum([3,6,10,1,8,9,9,8,9]))