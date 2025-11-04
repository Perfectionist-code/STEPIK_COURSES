from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3: return n + 1
    if n >= 3 and not n % 2: return f(n - 2) + n - 2
    return f(n + 2) + n + 2


cnt = 0
for n in range(1, 1001):
    try:
        if 9999 < (D:=f(n)) < 100000:
            print(D)
            cnt += 1
    except RecursionError:
        continue
print(cnt)
