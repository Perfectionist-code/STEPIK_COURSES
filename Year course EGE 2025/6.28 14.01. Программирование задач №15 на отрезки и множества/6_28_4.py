def f(x):
    P = 20 <= x <= 80
    Q = 35 <= x <= 57
    A = a1 <= x <= a2
    return A or (Q <= P)


ox = [dx for x in (20, 80, 35, 57) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) == 0 for x in ox):
            res.append(a2 - a1)
print(min(res))
