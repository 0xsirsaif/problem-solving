# find summation of n integers
def n_sum(n):
    if n == 0:
        return 0
    summation = [0]
    for i in range(1, n+1):
        summation.append(summation[i-1] + i)
    return summation[-1]