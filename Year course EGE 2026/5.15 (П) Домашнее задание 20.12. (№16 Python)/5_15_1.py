from functools import lru_cache


@lru_cache(1010)
def f(n: int):
    if n == 0: return 0
    if n % 2: return 1 + f(n - 1)
    return f(n // 2) - 1


for i in range(1001): f(i)

cnt = 0
for n in range(1000):
    if f(n) == 0:
        cnt += 1
print(cnt)
