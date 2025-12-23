from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3: return 1
    if n >= 2 and sum(int(x) for x in str(n)) % 2: return f(n - 1) + f(n // 2)
    return f(n - 1) - f(n - 2)


for i in range(101): f(i)

print(f(100))
