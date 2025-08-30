from functools import reduce


def product(*args):
    return reduce(lambda a, b: a * b, args)


print(product(2,5,10))
