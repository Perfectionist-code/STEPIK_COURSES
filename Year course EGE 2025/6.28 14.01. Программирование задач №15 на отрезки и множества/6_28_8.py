def f(x):
    P = 20 <= x <= 30
    Q = 5 <= x <= 53
    A = a1 <= x <= a2
    return A and (Q <= P)


ox = [dx for x in (20, 30, 5, 53) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) == False for x in ox):
            res.append(a2 - a1)
print(max(res))
