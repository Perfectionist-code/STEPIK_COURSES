from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1: return n
    if n > 1 and not n % 3: return n + f(n // 3)
    return n + f(n + 3)

for n in range(1, 1001):
    try:
        if f(n) > 100:
            print(n)
            break
    except RecursionError:
        continue
