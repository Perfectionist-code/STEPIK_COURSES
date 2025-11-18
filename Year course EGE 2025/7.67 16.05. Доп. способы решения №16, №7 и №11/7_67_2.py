from functools import lru_cache


@lru_cache(None)
def f(n: int):
    if n < 4: return n
    return 2 * n * f(n - 4)


for i in range(5, 13766): f(i)

print((f(13766) - 9 * f(13762)) // f(13758))
