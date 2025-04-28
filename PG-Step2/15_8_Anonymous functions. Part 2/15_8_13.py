from functools import reduce


def evaluate(coefficients, num):
    index_lst = list(range(len(coefficients) - 1, -1, -1))
    return reduce(lambda x, y: x + y, map(lambda cf, idx: cf * num ** idx, coefficients, index_lst))


_coefficients = tuple(map(int, input().split()))
_x = int(input())
print(evaluate(_coefficients, _x))
