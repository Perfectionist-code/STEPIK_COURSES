from functools import lru_cache
from fractions import Fraction

@lru_cache(None)
def f(n):
    if n == 1: return 1
    return 3 * n * f(n - 1)


for i in range(10, 2024): f(i)

print((Fraction(f(2024), 6) + f(2023)) // f(2022))
