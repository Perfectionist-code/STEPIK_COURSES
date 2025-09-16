from functools import lru_cache


@lru_cache(1000)
def f(n):
    if n == 1: return 1
    if n == 2: return 2
    return n * (n - 1) + f(n - 1) - f(n - 2)


for i in range(1, 1500): f(i)
res = f(2024) + f(2020) - f(2019)
print('Ответ:', res)
