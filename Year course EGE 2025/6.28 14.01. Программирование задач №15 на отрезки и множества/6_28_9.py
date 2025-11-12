def f(x):
    P = 135 <= x <= 211
    Q = 234 <= x <= 356
    R = 288 <= x <= 384
    A = a1 <= x <= a2
    return (not (Q <= (P or R))) <= ((not A) <= (not Q))


ox = [dx for x in (135, 211, 234, 356, 288, 384) for dx in (x - 0.0001, x, x + 0.0001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append(a2 - a1)
print(min(res))
