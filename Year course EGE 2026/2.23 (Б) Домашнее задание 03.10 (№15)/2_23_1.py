def f(x):
    P = 12 <= x <= 62
    Q = 32 <= x <= 92
    A = a1 <= x <= a2
    return ((not A) and Q) <= P


ox = [dx for x in (12, 62, 32, 92) for dx in (x - 0.001, x, x + 0.001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
            print(a1, a2)
print(min(res))
