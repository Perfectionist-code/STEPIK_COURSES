def f(x):
    P = 55 <= x <= 80
    Q = 20 <= x <= 105
    A = a1 <= x <= a2
    return Q <= ((P == Q) or ((not P) <= A))


ox = [dx for x in (55, 80, 20, 105) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(min(res), res)
