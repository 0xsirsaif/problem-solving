class Solution:
    def romanToInt(self, s):
        roman_priority = {
            "I": 0,
            "V": 1,
            "X": 2,
            "L": 3,
            "C": 4,
            "D": 5,
            "M": 6
        }
        int_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        for i in range(len(s)):
            if i == (len(s) - 1):
                num += int_roman[s[i]]
                continue
            if roman_priority[s[i]] < roman_priority[s[i + 1]]:
                 num -= int_roman[s[i]]
            else:
                num += int_roman[s[i]]
        return num


s = Solution()
print(s.romanToInt("MCMXCIV"))
