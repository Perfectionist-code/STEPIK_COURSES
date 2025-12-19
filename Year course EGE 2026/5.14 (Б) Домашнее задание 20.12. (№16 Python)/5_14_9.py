from functools import lru_cache


@lru_cache(None)
def g(n: int):
    if n >= 221337: return 2 * n + 50
    return g(n + 11) - 48


@lru_cache(None)
def f(n: int):
    if n > 30: return f(n - 6) + 2048
    return 3 * (g(n - 5) + 13)


for i in range(221338, 1, -1): g(i)
for i in range(29, 5078): f(i)

print(f(5078))
