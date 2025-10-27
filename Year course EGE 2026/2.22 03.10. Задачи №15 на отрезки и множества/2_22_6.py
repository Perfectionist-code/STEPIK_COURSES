def f(x):
    P = 25 <= x <= 42
    Q = 1 <= x <= 98
    A = a1 <= x <= a2
    return Q <= ((not P and Q) <= A)


ox = [dx for x in (1, 25, 42, 98) for dx in (x, x + 0.1, x - 0.1)]

for a1 in ox:
    for a2 in ox:
        if a2 > a1 and all(f(x) for x in ox):
            print(a1,a2)

# def f(x):
#     P = 25 <= x <= 42
#     Q = 1 <= x <= 98
#     A = a1 <= x <= a2
#     return (((not P) and Q) <= A)
#
#
# ox = [dx for x in (1, 25, 42, 98) for dx in (x - 0.01, x, x + 0.01)]
#
# for a1 in ox:
#     for a2 in ox:
#         if a2 > a1 and all(f(x) for x in ox):
#             print(a1, a2)
