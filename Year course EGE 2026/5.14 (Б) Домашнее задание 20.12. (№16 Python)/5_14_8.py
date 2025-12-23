from functools import lru_cache


@lru_cache(None)
def g(n: int):
    if n >= 40: return g(n - 3) - 20
    return 30 * n + 24


@lru_cache(None)
def f(n: int):
    if n <= 250194: return f(n + 8) + 1050
    return 3 * (g(n - 5) + 27)


for i in range(39, 250195): g(i)
for i in range(250195, 10, -1): f(i)

print(f(10))
