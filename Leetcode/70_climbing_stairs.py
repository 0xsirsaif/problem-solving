class Solution:
    # Time complexity => O(N)
    # Space complexity => O(N)
    def climbStairs(self, n: int) -> int:
        cache = {0: 1,
                 1: 1
                 }
        i = 2
        while i <= n:
            exist = cache.get(i)
            if not exist:
                cache[i] = cache[i - 1] + cache[i - 2]
            i += 1
        ways = cache.get(n)
        return ways


S = Solution()
print(S.climbStairs(0))
