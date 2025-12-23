from functools import lru_cache


@lru_cache(None)
def f(n: int):
    if n >= 2025: return n
    return n + 3 + f(n + 3)


for i in range(2025, 21, -100): f(i)

print(f(23) - f(21))
