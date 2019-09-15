'''
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

LINK : http://bit.ly/2Lf3Ap4
'''

def sqrt(x):
    numbers_less_than_x = [int(i) for i in range(x)]
    low = 0
    high = len(numbers_less_than_x)-1

    while low <= high:
        mid = round((low+high)/2)
        guess = numbers_less_than_x[mid]

        if guess * guess == x:
            return '{} is the square root of {}'.format(guess,x)
        elif guess * guess > x:
            high = mid -1
        elif guess * guess < x:
            low = mid + 1
        print('low: ',low,'high: ',high,'guess: ',guess,'mid: ',mid)
    else:
        return '{} is the square root of {}'.format(high,x)

print(sqrt(16))