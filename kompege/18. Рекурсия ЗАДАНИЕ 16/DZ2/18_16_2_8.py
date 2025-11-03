from functools import lru_cache
from fractions import Fraction
from math import factorial


@lru_cache()
def f(n: int):
    if n > 10000: return n - 10000
    return f(n + 1) + f(n + 2)


for i in range(12345, 10, -1): f(i)

print(f(12345)*((f(10)-f(12))//f(11)) + f(10101))
