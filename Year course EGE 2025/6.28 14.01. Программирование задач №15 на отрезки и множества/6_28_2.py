def f(x):
    P = 37 <= x <= 60
    Q = 40 <= x <= 77
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))


ox = [dx for x in (37, 60, 40, 77) for dx in (x - .0001, x, x + .0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(min(res))
