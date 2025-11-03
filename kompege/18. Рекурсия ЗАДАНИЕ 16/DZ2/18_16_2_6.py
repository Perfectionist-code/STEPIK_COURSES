from functools import lru_cache
from decimal import Decimal


@lru_cache()
def f(n: int):
    if n == 1: return 1
    return Decimal((2 * n - 1) * f(n - 1))


for i in range(1, 3516): f(i)

print(f(3516) // f(3513))
