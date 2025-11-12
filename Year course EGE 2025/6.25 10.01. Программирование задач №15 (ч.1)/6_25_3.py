def f(x):
    return (not (x % a == 0)) <= (not (x % 21 == 0) and not (x % 35 == 0))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break
