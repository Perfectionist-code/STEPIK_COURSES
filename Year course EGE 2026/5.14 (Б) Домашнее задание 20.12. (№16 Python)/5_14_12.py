from functools import lru_cache


@lru_cache(None)
def g(n: int):
    if n > 75: return g(n - 7) - 120
    return n - 9


@lru_cache(None)
def f(n: int):
    if n >= 31197: return 2 * (g(n - 2) + 5)
    return f(n + 3) + 2500


for i in range(74, 100000, 2): g(i)
for i in range(31197, 36, -2): f(i)

print(f(37))
