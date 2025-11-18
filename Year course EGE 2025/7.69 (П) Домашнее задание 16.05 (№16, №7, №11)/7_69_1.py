from functools import lru_cache


@lru_cache(None)
def f(n: int):
    if n < 7: return 7
    if n >= 7 and n % 3: return 5 - f(n - 1)
    return 3 + f(n - 1)


for i in range(6, 3014): f(i)
print(f(3015))
