def f(x, A) -> bool:
    return (x % 4 != 3 or x % 6 != 1) <= (x % 36 != A)

for A in range(1, 3000):
    if all((f(x, A) for x in range(1, 3000))):
        print(A)
        break
