def f(x, y, A):
    return (2 * x + y != 70) or (x < y) or (A < x)


for A in range(1, 300):
    if all((f(x, y, A) for y in range(1, 300) for x in range(1, 300))):
        print(A)
