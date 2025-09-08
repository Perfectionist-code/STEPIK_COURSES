def f(x, A) -> bool:
    return (x & 107 == 0) <= ((x & 55 != 0) <= (x & A != 0))


for A in range(1, 3000):
    if all((f(x, A) for x in range(1, 3000))):
        print(A)
        break
