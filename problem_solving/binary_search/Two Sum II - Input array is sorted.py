'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

LINK : http://bit.ly/2IxQHol
'''
def two_sum_of_target_number(numbers, target):
    # make target number the max number in this sorted list
    numbers = [int(number) for number in numbers if number < target]
    low = 0
    high = len(numbers)-1
    while low <= high:
        mid = round((high+low)/2)
        guess = numbers[mid]
        output = []
        if target-guess in numbers:
            output.append(numbers.index(guess)+1)
            output.append(numbers.index(target-guess)+1)
            return output

        else:
            print('high: ',high,'low: ',low,'guess: ',guess)
            high = mid-1
    else:
        low = 0
        high = len(numbers) - 1
        while low <= high:
            mid = round((high + low) / 2)
            guess = numbers[mid]
            output = []
            if target - guess in numbers:
                output.append(numbers.index(guess)+1)
                output.append(numbers.index(target - guess)+1)
                return output

            else:
                print('high: ', high, 'low: ', low, 'guess: ', guess)
                low = mid + 1


print(two_sum_of_target_number([int(num) for num in input().split()],3))