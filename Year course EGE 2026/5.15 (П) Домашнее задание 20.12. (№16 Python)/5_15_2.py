from functools import lru_cache
from fractions import Fraction


@lru_cache(None)
def f(n):
    if n < 15: return 4
    if n >= 15 and n % 3: return f(n - 1) + 3
    return f(Fraction(2 * n, 3)) + n - 1


for i in range(1000): f(i)

res = []
for n in range(1000):
    print(d := f(n))
    if d == 251:
        res.append(n)
print('-----' * 5)
print(max(res))
