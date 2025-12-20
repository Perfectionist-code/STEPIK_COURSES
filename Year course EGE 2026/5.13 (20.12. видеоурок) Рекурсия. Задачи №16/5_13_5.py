from functools import lru_cache


@lru_cache(None)
def f(n: int):
    if n >= 2025: return n
    return 2 * n + f(n + 2)


for i in range(2025, 82, -100): f(i)

print(f(82) - f(81))
