from functools import lru_cache


@lru_cache(1000)
def f(n):
    if n < 7: return 7
    return 2 * n + f(n - 1)


for i in range(6, 1500, 3): f(i)
print('Ответ:', f(2024) - f(2022))
