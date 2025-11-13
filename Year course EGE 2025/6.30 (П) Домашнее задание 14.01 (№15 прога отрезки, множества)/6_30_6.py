a = set()


def f(x):
    P = x in {14, 16, 18, 20, 22, 24}
    Q = x in {16, 19, 22, 25, 28}
    A = x in a
    return P <= ((Q and (not A)) <= (not P))


for x in range(1, 1000):
    if f(x) == False:
        a.add(x)
print(sum(a), a)
