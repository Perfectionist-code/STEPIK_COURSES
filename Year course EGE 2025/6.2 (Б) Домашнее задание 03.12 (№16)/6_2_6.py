from functools import lru_cache

@lru_cache()
def f(n):
    if n < 11: return n
    return  n + f(n-1)

for i in range(10, 2024, 2): f(i)

print('Ответ:', f(2024) - f(2021))