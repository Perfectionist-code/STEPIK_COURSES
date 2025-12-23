from functools import lru_cache


@lru_cache(None)
def f(n: int):
    return 2 * (g(n - 3) + 8)


@lru_cache(None)
def g(n: int):
    if n < 10: return 2 * n
    return g(n - 2) + 1


for i in range(9, 20000, 100): g(i)
for i in range(9, 15548, 100): f(i)

print(f(15548))
