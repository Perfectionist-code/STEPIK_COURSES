import functools
import math

numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
print(math.prod(numbers))  # так
# print(functools.reduce(lambda x, y: x * y, numbers))  # или так
# _prod = 1
# for num in numbers:  # или так
#     _prod *= num
# print(_prod)
