from functools import lru_cache


@lru_cache()
def f(n: int):
    if n > 100_000: return n
    return f(n + 1) + 5 * n + 2


for i in range(100000, 2, -1): f(i)

print(f(3) - f(7))
