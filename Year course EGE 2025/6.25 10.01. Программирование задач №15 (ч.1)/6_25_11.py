def f(x):
    B = 120 <= x <= 130
    return B <= ((not (x % 7 == 0)) or (A > 2 * x))


for A in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(A)
        break
