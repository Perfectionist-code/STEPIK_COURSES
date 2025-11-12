def f(x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = a1 <= x <= a2
    return (P == Q) <= (not A)


ox = [dx for x in (5, 30, 14, 23) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(max(res))
