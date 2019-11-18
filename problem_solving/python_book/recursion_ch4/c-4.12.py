"""
Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction.
"""
def calculate_product(m,n):
    if n == 1:
        return m
    else:
        sum = m + calculate_product(m,n-1)
        return sum

print(calculate_product(5,6))