from functools import lru_cache


@lru_cache()
def f(n):
    if n == 0: return 0
    if n > 0 and not n % 2: return f(n // 2)
    return 1 + f(n - 1)


for i in range(1, 501, 2): f(i)

cnt = 0
for num in range(1, 501):
    if f(num) == 8:
        cnt += 1
print(cnt)
