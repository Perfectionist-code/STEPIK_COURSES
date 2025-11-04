from functools import lru_cache


@lru_cache()
def f(n):
    if n <= 18: return n + 3
    if n > 18 and not n % 3: return (n // 3) * f(n // 3) + n - 12
    return f(n - 1) + n ** 2 + 5


for i in range(1, 1000, 2): f(i)

cnt = 0
for nn in range(1, 1001):
    if all(int(x) % 2 == 0 for x in str(f(nn))):
        cnt += 1
print(cnt)
