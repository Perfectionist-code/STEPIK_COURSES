def del_(n, m):
    return n % m == 0


def f(x):
    return (not del_(x, a)) <= (del_(x, 6) <= (not del_(x, 4)))


for a in range(100, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break
