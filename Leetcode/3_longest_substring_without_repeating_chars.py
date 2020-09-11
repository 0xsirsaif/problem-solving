class Solution:
    def lengthOfLongestSubstring(self, s):
        longest_substring = ("$"+s+"$")[1:len(s)+1]

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            return len(set(s))
        # all are different
        if len(set(s)) == len(s):
            if len(s) == 3:
                return 3
            return len(s)-2

        # [1:len] chars are different
        if len(set(longest_substring)) == len(longest_substring):
            return len(longest_substring)
        elif len(set(longest_substring)) == 1:
            return 1

        while len(s) > 1:
            _start = 0
            _end = len(longest_substring)

            increase_start = self.lengthOfLongestSubstring(longest_substring[_start: _end - 1])
            decrease_end = self.lengthOfLongestSubstring(longest_substring[1: _end])
            result = increase_start if (increase_start > 1) else decrease_end

            if result > 1:
                return result
            else:
                return result


obj = Solution()
# print(obj.lengthOfLongestSubstring("abba"))

test_cases = ["abba","bwf","cdd","aab","au","aa","","pwwkew"]
for i in test_cases:
    print(i, obj.lengthOfLongestSubstring(i))
