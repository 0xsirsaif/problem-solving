"""
Develop a nonrecursive implementation of the version of power from
Code Fragment 4.12 that uses repeated squaring.
"""


def power(x, n):
    partial = 1
    for i in range(n//2):
        partial *= x
    res = partial * partial
    if n % 2 == 0:
        return res
    return x*res

print(power(10,11))
print(power(10,10))