from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 10_000: return n
    if n < 10000 and n % 3:
        return 2 * n + f(n + 3)
    return n + f(n // 3)


for i in range(10000, 46, -1):
    if i % 3: f(i)

print('Ответ:', f(999) - f(46))
