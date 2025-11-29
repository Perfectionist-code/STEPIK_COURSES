from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1: return 3
    return 3 * n + 2 * f(n - 1)


for i in range(1, 2024): f(i)

print(f(2024) - 4 * f(2022))
