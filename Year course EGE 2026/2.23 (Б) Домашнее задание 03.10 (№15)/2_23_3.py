def f(x):
    P = 23 <= x <= 58
    Q = 1 <= x <= 39
    A = a1 <= x <= a2
    return (P or A) <= (Q or A)


ox = [dx for x in (23, 58, 1, 39) for dx in (x - 0.001, x, x + 0.001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2-a1)
print(min(res))
