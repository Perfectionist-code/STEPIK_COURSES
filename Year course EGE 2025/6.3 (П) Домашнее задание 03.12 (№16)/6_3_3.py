from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 10000: return n
    if n < 10000 and n % 4:
        return 1 + f(n + 2)
    return n // 4 + f(n // 4 + 2)


for i in range(10000, 3, -1):
    if i % 2: f(i)

print('Ответ:', f(174) - f(3))
