from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 15: return 4 * n - 3
    return f(n - 3) + 5

@lru_cache(None)
def g(n):
    return f(n - 1) + f(n - 3)

for i in range(15, 54449): f(i)

print(g(54449))
