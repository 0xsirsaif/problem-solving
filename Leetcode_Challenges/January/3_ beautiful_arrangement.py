from itertools import permutations

class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 1:
            return 1
        a = list(permutations(range(1,n+1)))
        count = 0
        for i in a:
            for x in range(1, len(i)):
                if i[x] % x == 0:
                    count += 1
                    break
        print(count)
        print(a)
        return count

s = Solution()
print(s.countArrangement(2))