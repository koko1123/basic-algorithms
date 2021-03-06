import math

"""
implement Karatsuba multiplication

"""


def multiply(x, y):
    if len(x) in [1, 2] or len(y) in [1, 2]:
        return int(x) * int(y)
    middle_of_x = int(len(x) / 2)
    a = x[:middle_of_x]
    b = x[middle_of_x:]

    middle_of_y = int(len(y) / 2)
    c = y[:middle_of_y]
    d = y[middle_of_y:]

    step_one = multiply(c, a)
    step_two = multiply(d, b)
    step_three = multiply(str(int(a) + int(b)), str(int(c) + int(d)))
    gauss_trick = step_three - step_two - step_one
    return int(math.pow(10, len(x)) * step_one + math.pow(10, middle_of_x) * gauss_trick + step_two)


first_num = '3141592653589793238462643383279502884197169399375105820974944592'
second_num = '3141592653589793238462643383279502884197169399375105820974944592'
print(multiply(first_num, second_num))
