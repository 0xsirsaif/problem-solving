from typing import List
from itertools import accumulate


def brute_force(nums: List[int]) -> int:
    i = j = 0
    while j <= len(nums) and i <= len(nums):
        yield nums[i:j+1]
        j += 1
        if j == len(nums):
            i += 1
            j = i


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pass








S = Solution()
print(S.subarraySum([1],0))

