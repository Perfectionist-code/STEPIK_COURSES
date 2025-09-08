def f(x, y, A):
    return not ((x * y > A) and (x > y) and (x < 8))


for A in range(1, 300):
    if all(f(x, y, A) for y in range(1, 300) for x in range(1, 300)):
        print(A)
        break
