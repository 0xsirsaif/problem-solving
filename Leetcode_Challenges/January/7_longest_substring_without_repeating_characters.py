class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ptr_1 = ptr_2 = max_len = 0

        dict_ = {}
        while ptr_2 < len(s) and ptr_1 < len(s):
            print(ptr_1, ptr_2)
            does_exist = dict_.get(s[ptr_2], 0)
            if not does_exist:
                dict_[s[ptr_2]] = does_exist + 1
                ptr_2 += 1
            else:
                max_len = max(max_len, (ptr_2 - ptr_1))
                dict_[s[ptr_2]] -= 1
                ptr_1 += 1

        return max_len


S = Solution()
print(S.lengthOfLongestSubstring("pwwkew"))