from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # counter = dict(Counter(nums))
        #
        # for key in counter:
        #     if counter[key] > 1:
        #         arr.extend([key, key])
        #     else:
        #         arr.append(key)

        arr = list(set(nums))
        pairs_num = 0
        i = 0
        j = len(arr)-1
        print(arr)

        while j >= 0:
            print(i)
            if j == 0:
                i += 1
                j = len(arr)-1
            elif i == j:
                j -= 1
            if abs(arr[i] - arr[j]) == k:
                print(">>> ",arr[i], arr[j])
                pairs_num += 1
                j -= 1
            else:
                j -= 1

        return pairs_num



s = Solution()
print(s.findPairs([3,1,4,2], 2))

# arr = sorted(nums)
# def search_binary(arr, start, end, target):
#     while start <= end:
#         mid = (end + start) // 2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     else:
#         return False
#
#
# pairs_num = 0
# for i in arr:
#     print("=== ", i, k + i, -(k + i))
#     if search_binary(arr, 0, len(arr) - 1, k + i) or search_binary(arr, 0, len(arr) - 1, -(k + 1)):
#         pairs_num += 1
#
# return pairs_num
