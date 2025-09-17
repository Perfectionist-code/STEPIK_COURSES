from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 10000: return n
    if n < 10000 and n % 2:
        return n ** 2 + f(n + 2)
    return 1 + f(n // 2)


for i in range(10000, 9, -1):
    if i % 2:
        f(i)

print('Ответ:', f(192) - f(9))
