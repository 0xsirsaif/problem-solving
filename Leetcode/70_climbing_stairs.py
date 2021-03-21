class Solution:
    # Time complexity => O(N)
    # Space complexity => O(N)
    def climbStairs(self, n: int) -> int:
        cache = {0: 1, 1: 1}
        i = 2
        while i <= n:
            exist = cache.get(i)
            if not exist:
                cache[i] = cache[i - 1] + cache[i - 2]
            i += 1
        ways = cache.get(n)
        return ways

    def optimized_solution(self, n: int) -> int:
        ptr_1 = 1
        ptr_2 = 1
        res = 1
        i = 2
        while i <= n:
            res = ptr_1 + ptr_2
            ptr_1 = ptr_2
            ptr_2 = res
            i += 1
        return res

S = Solution()
print(S.optimized_solution(3))
