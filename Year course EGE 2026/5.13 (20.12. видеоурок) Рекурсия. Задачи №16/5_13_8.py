from functools import lru_cache
from fractions import Fraction


@lru_cache(None)
def f(n: int):
    if n >= 19: return f(n - 4) + 3580
    return 6 * (g(n - 7) - 36)


@lru_cache(None)
def g(n: int):
    if n >= 248045: return Fraction(n, 20) + 28
    return g(n + 9) - 4


for i in range(248045, 1, -100): g(i)
for i in range(19, 673, 100): f(i)

print(f(673))
