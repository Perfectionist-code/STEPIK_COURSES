def f(x):
    P = 20 <= x <= 30
    Q = 5 <= x <= 15
    R = 35 <= x <= 50
    A = a1 <= x <= a2
    return (P <= Q) or ((not A) <= R)


ox = [dx for x in (20, 30, 5, 15, 35, 50) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(min(res))
