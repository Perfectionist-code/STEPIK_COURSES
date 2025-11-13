def f(x):
    P = 10 <= x <= 20
    Q = 35 <= x <= 45
    A = a1 <= x <= a2
    return ((not P) <= Q) and (not A)


ox = [dx for x in (10, 20, 35, 45) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) == 0 for x in ox):
            res.append(a2 - a1)
print(min(res), res)
