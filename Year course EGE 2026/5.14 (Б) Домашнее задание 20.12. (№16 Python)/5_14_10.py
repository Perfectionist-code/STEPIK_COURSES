from functools import lru_cache


@lru_cache(None)
def g(n: int):
    if n >= 32572: return g(n - 7) - 120
    return 9 * n - 31


@lru_cache(None)
def f(n: int):
    if n > 29: return f(n - 3) + 2500
    return 2 * (g(50000 - n) + 50)


for i in range(32571, 10 ** 5, 2): g(i)
for i in range(28, 637): f(i)

print(f(637))
