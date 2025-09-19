from functools import lru_cache


@lru_cache(2000)
def f(n):
    if n == 0: return 5
    if n > 0 and not n % 2: return 1 + f(n // 2)
    return f(n // 2)


cnt = 0
for i in range(1, 1_000):
    if (d := f(i)) == 7:
        cnt += 1
        print(bin(f(i))[2:], bin(i)[2:])
        print(cnt, i)
