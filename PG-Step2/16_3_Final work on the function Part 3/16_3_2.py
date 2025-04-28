from functools import reduce


def product_of_odds(data):  # data - список целых чисел
    return reduce(lambda a, b: a * b, filter(lambda x: x % 2 == 1, data), 1)

print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# from functools import reduce
# from operator import mul
#
# def product_of_odds(data):
#     return reduce(mul, filter(lambda x: x % 2 == 1, data), 1)