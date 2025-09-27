from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 5: return n
    if n > 5 and n % 4: return n + f(n + 2)
    return n + f(n // 2 - 1)


for i in range(1000):
    try:
        print(i, f(i))
        res = i
    except RecursionError:
        continue
print('Ответ:', res)