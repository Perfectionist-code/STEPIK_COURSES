from functools import lru_cache

@lru_cache(None)
def g(n: int):
    if n <= 9: return 3 * n
    return g(n - 4) + 2


@lru_cache(None)
def f(n: int):
    return g(n - 1) + g(n - 3)


for i in range(9, 100000, 100): g(i)
for i in range(9, 43000, 100): f(i)

print(f(42999))
