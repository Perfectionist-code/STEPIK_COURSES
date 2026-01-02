from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1: return 2
    return 3 * f(n - 1) - n


for i in range(1, 2025): f(i)

print((f(2025) - f(2023) - 1) // 3 ** 2022)
