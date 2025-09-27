from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3: return n + 1
    if n >= 3 and n % 2: return f(n + 2) + n + 2
    return n + f(n - 2) - 2


cnt = 0
for i in range(10000):
    try:
        if 100_00 <= f(i) < 100_000:
            print(i, f(i))
            cnt += 1
    except RecursionError:
        continue
print('Ответ:', cnt)
