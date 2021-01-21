class Solution:
    def isValid(self, s: str) -> bool:
        openings = "([{"
        table = {")": "(", "]": "[", "}": "{"}
        open_parentheses = []
        for i in range(len(s)):  # O(N) time complexity
            if s[i] in openings:
                open_parentheses.append(s[i])  # O(n/2) Space complexity
            else:
                try:
                    if table[s[i]] != open_parentheses.pop():
                        return False
                except:
                    return False
        return not open_parentheses

S = Solution()
print(S.isValid("()[]{}"))