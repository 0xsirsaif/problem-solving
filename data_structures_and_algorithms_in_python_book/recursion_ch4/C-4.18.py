"""
Use recursion to write a Python function for determining if a string s has
more vowels than consonants.
"""

def is_vowels_more(s):
    vowels = 'aAeEiIoOuU'
    def count_voewls(start, count):
        if start == len(s):
            return count
        elif s[start] in vowels:
            return count_voewls(start+1, count+1)
        else:
            return count_voewls(start+1, count)

    vowels_num = count_voewls(0, 0)
    return vowels_num > len(s) - vowels_num - 1

print(is_vowels_more('wwweeeiii'))
