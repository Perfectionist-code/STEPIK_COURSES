from functools import lru_cache


@lru_cache()
def f(n: int):
    if n >= 10_000: return n
    if n > 3 and not n % 3: return n + f(n // 3)
    return 2 * n + f(n + 3)


for i in range(10000, 1, -3): f(i)

print(f(999) - f(46))
