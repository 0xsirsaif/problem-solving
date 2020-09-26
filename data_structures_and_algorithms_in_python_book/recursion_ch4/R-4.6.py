"""
to compute the harmonic number we rely on the recursive nature of the problem, and make use of the improvements of the
tail recursion, return a tuple of two values (n, sum). sum = 1/n + previous_sum and so on....
"""


def harmonic_number(n, sum=0):
    if n == 0:
        return sum
    return harmonic_number(n-1, (1/n)+sum)


print(harmonic_number(100))
