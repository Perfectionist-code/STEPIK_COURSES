from functools import lru_cache
from fractions import Fraction



@lru_cache(None)
def f(n: int):
    if n == 1: return 1
    return n * f(n - 1)


for i in range(1, 2024, 100): f(i)

print(Fraction(Fraction(f(2024), 4) + f(2023), f(2022)))

