def f(x, y):
    return (7 * y + x < A) or (2 * x + 3 * y > 98)


for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break
