def f(x):
    return (x % a == 0) <= ((x % 21 == 0) or (x % 35 == 0))


for a in range(1, 100):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
