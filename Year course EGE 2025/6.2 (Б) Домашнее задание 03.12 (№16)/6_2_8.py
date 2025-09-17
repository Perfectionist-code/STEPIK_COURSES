from functools import lru_cache


@lru_cache()
def f(n):
    if n == 1: return 1
    return n * f(n - 1)


for i in range(1, 2024, 2): f(i)

print('Ответ:', (2 * f(2024) + f(2023)) // f(2022))
