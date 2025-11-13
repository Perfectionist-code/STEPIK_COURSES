def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = a1 <= x <= a2
    return (Q <= (not R)) and A and (not P)


ox = [dx for x in (10, 25, 15, 30, 40) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) == False for x in ox):
            res.append(a2 - a1)
print(max(res))
