def f(x):
    P = 5 <= x <= 110
    Q = 15 <= x <= 42
    R = 25 <= x <= 70
    A = a1 <= x <= a2
    return (P <= Q) or ((not A) <= (not R))


ox = [dx for x in (5, 110, 15, 42, 25, 70) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(min(res))