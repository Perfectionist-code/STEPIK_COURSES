from functools import lru_cache

@lru_cache(None)
def f(n: int):
    if n <= 10: return n
    return n - 12 + f(n - 21)

for i in range(224356): f(i)
print((f(224356) - f(224272))//f(59))

# ОТВЕТ: 12125 2 часа 15 мин