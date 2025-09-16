from functools import lru_cache


@lru_cache(1000)
def f(n):
    if n <= 3:
        return 1
    return (n + 3) * f(n - 2)


for i in range(3, 2000, 3): f(i)
print('Ответ:', f(2028) // f(2024))
