from functools import lru_cache


@lru_cache(None)
def f(n: int):
    if n > 3000: return n
    return (2 * n + 4) * f(n + 2)


for i in range(3001, 19, -1): f(i)

res = str(f(20) // f(28))
print(sum(int(x) for x in res))
