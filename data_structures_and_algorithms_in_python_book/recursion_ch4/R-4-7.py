"""
Describe a recursive function for converting a string of digits into the in-
teger it represents. For example, 13531 represents the integer 13, 531.
"""


def str_to_int(s):
    def _recur(s, ptr, sum):
        sum += int(s[ptr]) * (10 ** (len(s) - ptr - 1))
        if ptr == 0:
            return sum
        return _recur(s, ptr-1, sum)
    return _recur(s, len(s)-1, 0)

print(str_to_int('13544'))