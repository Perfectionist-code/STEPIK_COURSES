from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and not n % 4:
        return n // 4 + f(n // 4 + 2)
    return 1 + f(n + 2)


for i in range(10001, 3, -8):
    if i % 2:
           f(i)

print(f(174) - f(3))
