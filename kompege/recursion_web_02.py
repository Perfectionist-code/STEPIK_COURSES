from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)


for i in range(1, 2000):
    f(i)

print('Ответ:', f(2023) / f(2020))
