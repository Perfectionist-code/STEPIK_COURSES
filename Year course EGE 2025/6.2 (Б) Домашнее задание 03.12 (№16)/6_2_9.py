from functools import lru_cache
from fractions import Fraction


@lru_cache(None)
def f(n):
    if n == 1: return Fraction(1)
    return Fraction(2 * n * f(n - 1))


for i in range(1, 2024): f(i)
print('Ответ:', Fraction(Fraction(f(2024), 16) - f(2023), f(2022)))


# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     return 2 * n * f(n - 1)
#
#
# for i in range(1, 2024): f(i)
# print('Ответ:', (f(2024) // 16 - f(2023)) // f(2022))
