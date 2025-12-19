from functools import lru_cache


@lru_cache(None)
def g(n: int):
    if n > 80: return g(n - 5) + 205
    return 4 * (f(n - 3) - 15)


@lru_cache(None)
def f(n: int):
    if n >= 201208: return n // 4 + 150
    return f(n + 7) - 91


for i in range(201208, 1, -2): f(i)
for i in range(80, 2040, 2): g(i)

print(abs(g(2040)))
