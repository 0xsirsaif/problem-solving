from math import sqrt


def vaild_perfect_sqr(num):
    sqrt_num = str(sqrt(num))
    right_side = sqrt_num.split('.')[1]
    if right_side == '0':
        return True
    else:
        return False


print(vaild_perfect_sqr(7))