def f(x, y, A):
    return (x > 39) or (y > 26) or ((2 * x + 4 * y) < A)


for A in range(1, 300):
    if all((f(x, y, A) for y in range(1, 300) for x in range(1, 300))):
        print(A)
        break
