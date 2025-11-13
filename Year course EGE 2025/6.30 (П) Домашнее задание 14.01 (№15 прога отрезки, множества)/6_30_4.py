def f(x):
    P = 10 <= x <= 27
    Q = 20 <= x <= 40
    R = 32 <= x <= 50
    A = a1 <= x <= a2
    return (not A) or Q and (P or R)


ox = [dx for x in (10, 27, 20, 40, 32, 50) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(max(res))
