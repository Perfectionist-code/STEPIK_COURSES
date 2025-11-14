from functools import lru_cache


@lru_cache(None)
def f(n: int):
    if n < 4: return 1
    if n > 3 and n % 2: return n
    return f(n - 1) + f(n - 2) + f(n - 3)


for i in range(3, 2254): f(i)

print(f(2254) - f(2252))
