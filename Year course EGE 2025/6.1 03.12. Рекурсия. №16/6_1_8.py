from functools import lru_cache


@lru_cache(1000)
def f(n):
    if n < 3:
        return 3
    return 2 * n + 5 + f(n - 2)


for i in range(2, 2000, 1): f(i)
print('Ответ:', f(3027) - f(3023))
