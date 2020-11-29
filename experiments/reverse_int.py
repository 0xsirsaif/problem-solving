def reverse_int(num):
    length = len(str(num))
    result = 0
    for i in range(length):
        mod = num % 10
        result += mod * 10**(length - i - 1)
        num = num // 10
    return result


print(reverse_int(987654321))