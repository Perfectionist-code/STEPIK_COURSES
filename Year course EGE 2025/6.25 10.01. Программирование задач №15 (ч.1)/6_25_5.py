def f(x):
    return (((x & 13 != 0) or (x & 39 == 0)) <= (x & 13 != 0)) or ((x & a == 0) and (x & 13 == 0))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break
