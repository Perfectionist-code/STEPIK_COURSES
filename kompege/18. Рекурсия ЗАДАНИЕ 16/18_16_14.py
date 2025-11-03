from functools import lru_cache


@lru_cache()
def f(n):
    if n > 30: return n ** 2 + 5 * n + 4
    if n <= 30 and not n % 2: return f(n + 1) + 3 * f(n + 4)
    return 2 * f(n + 2) + f(n + 5)


for i in range(1, 1000, 2): f(i)

cnt = 0
for num in range(1, 1001):
    if sum((int(x) for x in str(f(num)))) == 27:
        cnt += 1
print(cnt)
