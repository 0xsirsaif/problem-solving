from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def compute_missing(actual, expected):
            return actual - expected

        missing_within = compute_missing(arr[-1], len(arr))
        # result lies outside list
        if missing_within < k or missing_within == 0:
            return arr[-1] + (k - missing_within)

        end = len(arr) - 1
        start = 0
        while start <= end:
            mid = (start + end) // 2
            missing = compute_missing(arr[mid], (mid + 1))
            if missing < k:
                start = mid + 1
            else:
                end = mid - 1

        if end == -1:
            return k

        return (arr[end] + k) - (compute_missing(arr[end], end+1))

    def findKthPositive_2(self, arr: List[int], k: int) -> int:
        missing_within = arr[-1] - len(arr)
        # result lies outside list
        if missing_within < k or missing_within == 0:
            return arr[-1] + (k - missing_within)

        end = len(arr) - 1
        start = 0
        while start <= end:
            mid = (start + end) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                start = mid + 1
            else:
                end = mid - 1

        small = start if start <= end else end
        if small < 0:
            return k

        rest = k - (arr[small] - small - 1)
        return arr[small] + rest


S = Solution()
print(S.findKthPositive([2], 1))
