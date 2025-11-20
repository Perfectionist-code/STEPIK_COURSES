from functools import lru_cache


@lru_cache(None)
def f(n):
    if n > 10_000: return n + 6
    return 2 * n + 8 + f(n + 4)


for i in range(10_001, 4625, -1): f(i)

print(f(1092) - f(1104))
