"""
Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be 'snap&stop' .
"""


def reverse_str(s):
    str_list = list(s)
    def _revesre(str_list, start, end):
        if end - start >= 1:
            str_list[end], str_list[start] = str_list[start], str_list[end]
            _revesre(str_list, start+1, end-1)
        return str_list
    return "".join(str(x) for x in _revesre(str_list, 0, len(str_list)-1))

print(reverse_str("ABCDE"))