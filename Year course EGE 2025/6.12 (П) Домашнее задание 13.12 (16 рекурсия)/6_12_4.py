from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 5: return n
    if n > 5 and n % 5: return n + f(n + 6)
    return n + f(n // 5 + 1)


for i in range(1000):
    try:
        if f(i) > 1000:
            print(i)
            break
    except RecursionError:
        continue
