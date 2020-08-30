class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest_char = min(strs, key=len)
        for i, char in enumerate(shortest_char):

            for other in strs:
                if other[i] != char:
                    return shortest_char[:i]
        return shortest_char



s = Solution()
print(s.longestCommonPrefix(["c","ac"]))


# def is_perfix_exist(perfix):
#     for s in strs:
#         if perfix not in s:
#             return False
#     return True


# if strs:
#     if len(strs) == 1:
#         return strs[0]
#     x = 0
#     y = 1
#     shortest_len = max([len(s) for s in strs])
#     perfixes = []
#     while y <= shortest_len:
#         perfix = strs[0][x:y]
#         if is_perfix_exist(perfix):
#             perfixes.append(perfix)
#             y += 1
#         else:
#             x += 1
#             y += 1
#     if perfixes:
#         return perfixes[-1]
# return ""


