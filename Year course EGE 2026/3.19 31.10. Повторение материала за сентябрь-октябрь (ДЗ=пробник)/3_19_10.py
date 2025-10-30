def f(x):
    B = 15 <= x <= 40
    C = 21 <= x <= 63
    A = a1 <= x <= a2
    return (not B) <= ((C and (not A)) <= B)


ox = [dx for x in (15, 40, 21, 63) for dx in (x - 0.001, x, x + 0.0001)]

res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in ox):
            res.append([a2 - a1])
print(min(res))
