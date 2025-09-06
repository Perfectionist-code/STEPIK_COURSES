def f(x, y, A):
    return (x**2 - 10 * x + 16 > 0) or (y**2 - 10 * y + 21 > 0) or (x * y < 2 * A)


for A in range(1, 300):
    if all((f(x, y, A) for y in range(1, 300) for x in range(1, 300))):
        print(A)
        break
