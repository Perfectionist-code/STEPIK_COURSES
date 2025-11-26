def f(x):
    P = 64 <= x <= 95
    Q = 72 <= x <= 106
    A = a1 <= x <= a2
    return (Q and (not A)) <= ((not P) <= (not Q))


ox = [dx for x in (64, 95, 72, 106) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(min(res))
