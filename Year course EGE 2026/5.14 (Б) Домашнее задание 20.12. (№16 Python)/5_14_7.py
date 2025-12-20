from functools import lru_cache

@lru_cache(None)
def g(n: int):
    if n <= 9: return 3 * n
    return g(n - 2) + 1


@lru_cache(None)
def f(n: int):
    return g(n - 1)


for i in range(8, 100000, 1000): g(i)
for i in range(8, 47995, 1000): f(i)

print(f(47995))
