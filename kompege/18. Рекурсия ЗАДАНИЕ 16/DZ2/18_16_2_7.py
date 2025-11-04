from functools import lru_cache
from fractions import Fraction
from math import factorial


@lru_cache()
def f(n: int):
    if n >= 5000: return factorial(n)
    if 1 <= n < 5000: return Fraction((2 * f(n + 1)),(n + 1))


for i in range(5000, 1, -1): f(i)

print(f(7) / f(4) * 1000)
