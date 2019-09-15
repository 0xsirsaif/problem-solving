'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

LINK : http://bit.ly/2J0efS6
'''



def get_item(list_, item):
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = round((high + low) / 2)
        guess = list_[mid]

        if guess == item:
            return mid

        elif item < guess:
            high = mid - 1

        elif item > guess:
            low = mid + 1
    else:
        return 'the expected index is {}'.format(low)

print(get_item(list(input().split()), input()))
