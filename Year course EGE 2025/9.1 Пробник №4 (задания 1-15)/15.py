def f(x):
    return ((x % 9 == 0) <= (not (x % 6 == 0))) or (x + A >= 100)


for A in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break
