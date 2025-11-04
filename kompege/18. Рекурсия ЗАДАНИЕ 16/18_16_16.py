from functools import lru_cache


@lru_cache()
def f(n):
    if n == 1: return 1
    if n >= 2 and not n % 2: return f(n // 2) + 1
    return f(n - 1) + n


for i in range(1, 501, 2): f(i)

cnt = 0
for num in range(1, 501):
    if f(num) == 19:
        print(num)
        break
