# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

def isBadVersion(version):
    A = [True]
    return not A[version]

class Solution:
    def firstBadVersion(self, n):
        end = n - 1
        start = 0
        while (start <= end):
            mid = start + (end - start) / 2
            if isBadVersion(mid) is False:
                start = mid + 1
            else:
                end = mid - 1
        return start


s = Solution()
print(s.firstBadVersion(0))
# print(len([True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False,
#          False, False, False, ]))