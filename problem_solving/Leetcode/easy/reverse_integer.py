class Solution:
    def reverse(self, x):
        rev_str = ''
        num = abs(x)
        if x == 0:
            return 0
        for i in range(len(str(num))):
            new_str = str(num)[i] + rev_str
            rev_str = new_str
        if x < 0:
            rev_str = '-' + rev_str
        if int(rev_str) >= 2**31-1 or int(rev_str) <= -2**31:
            return 0
        return int(rev_str)

S = Solution()
print(S.reverse(1534236469))