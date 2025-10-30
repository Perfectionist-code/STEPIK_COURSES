def f(x):
    P = 15 <= x <= 60
    Q = 15 <= x <= 30
    A = a1 <= x <= a2
    return (not Q or P) and A


ox = [dx for x in (15, 30, 60) for dx in (x - 0.01, x, x + 0.01)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and not all(f(x) for x in ox):
            res.append(a2 - a1)
            print(a1, a2, a2 - a1)
print('---' * 10)
print(min(res))
