def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2
    return (not A) <= (B == C)


ox = tuple(dx for x in (36, 75, 60, 110) for dx in (x - 0.0001, x, x + 0.0001))

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(min(res))
