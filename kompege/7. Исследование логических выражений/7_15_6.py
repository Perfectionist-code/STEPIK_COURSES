def f(x: int, A: int) -> bool:
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & A != 0))


for A in range(1, 3000):
    if all((f(x, A) for x in range(1, 3000))):
        print(A)
        break
