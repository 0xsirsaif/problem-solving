class Solution:
    def integerReplacement(self, n: int) -> int:
        def _recur(num, count):
            if num == 1:
                return count
            if num%2 == 0:
                return _recur(num//2, count+1)
            else:
                add = _recur(num+1, count+1)
                sub = _recur(num-1, count+1)
                if add >= sub:
                    return sub
                return add

        return _recur(n, 0)

s = Solution()
print(s.integerReplacement(1234))
