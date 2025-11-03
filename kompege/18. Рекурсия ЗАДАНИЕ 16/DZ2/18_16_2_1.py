from functools import lru_cache


@lru_cache()
def f(n: int):
    if n == 1: return 1
    return n * f(n - 1)


for i in range(1, 2023, 2): f(i)

print(f(2023) // f(2020))
