from functools import lru_cache


def sum_fig(n: int) -> bool:
    return bool(sum(map(int, str(n))) % 2)


@lru_cache
def f(n):
    if n < 3: return 1
    if n > 2 and sum_fig(n): return f(n - 1) + f(n // 2)
    return f(n - 1) - f(n - 2)


print(f(100))
