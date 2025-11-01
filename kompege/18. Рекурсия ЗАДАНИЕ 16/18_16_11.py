from functools import lru_cache


@lru_cache(None)
def g(n):
    if n == 1: return 1
    return f(n - 1) + g(n - 1) + n

@lru_cache(None)
def f(n):
    if n == 1: return 1
    return f(n - 1) - 2 * g(n - 1)

for  i in  range(1,50):
    g(i)
    f(i)

print(sum(map(int, str(g(36)))))

