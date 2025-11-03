from functools import lru_cache


@lru_cache()
def f(n: int):
    if n == 1: return 1
    return n ** 2 + f(n - 1)


for i in range(1, 1000, 2): f(i)

print(f(1000) - f(997))
