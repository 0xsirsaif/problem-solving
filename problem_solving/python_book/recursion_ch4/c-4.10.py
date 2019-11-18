"""
Describe a recursive algorithm to compute the integer part of the base-two
logarithm of n using only addition and integer division.
"""
# how many times we multiple two to get the n number
def calculate_logarithm(n):
    division = n // 2
    if division == 0 :
        return 0
    else:
        result = calculate_logarithm(division) + 1
        return result

print(calculate_logarithm())