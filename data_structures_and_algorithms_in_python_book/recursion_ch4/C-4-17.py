"""
Write a short recursive Python function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, racecar and
'gohangasalamiimalasagnahog' are palindromes.
"""
def is_palindrome(s):
    str_list = list(s)
    def _revesre(str_list, start, end):
        if end - start >= 1:
            str_list[end], str_list[start] = str_list[start], str_list[end]
            _revesre(str_list, start+1, end-1)
        return str_list
    return s == "".join(str(x) for x in _revesre(str_list, 0, len(str_list)-1))

print(is_palindrome("gohangasalamiimalasagnahog"))