class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev_num = str(x)[::-1]
        if str(x) == rev_num:
            return True


def reverse(num):
    rev = 0
    while num > 0:
        print("num1 >>  ", num)
        rev = (10 * rev) + num % 10
        num //= 10
        print("rev >>  ", rev)
        print("num2 >>  ", num)
        print("===================")
    return rev
print(reverse(100))
