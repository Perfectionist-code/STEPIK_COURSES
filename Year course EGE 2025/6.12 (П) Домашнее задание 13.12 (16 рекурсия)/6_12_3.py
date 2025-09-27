from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1: return n
    if n > 1 and n % 3: return n + f(n + 3)
    return n + f(n // 3)


for i in range(100):
    try:
        if f(i) > 100:
            print(i)
            break
    except RecursionError:
        continue
