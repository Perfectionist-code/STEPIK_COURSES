def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = a1 <= x <= a2
    return (not (C or J)) <= (not A)


ox = [dx for x in (48, 94, 83, 100) for dx in (x - 0.0001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(max(res))
