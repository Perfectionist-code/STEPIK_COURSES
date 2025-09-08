def f(x, A) -> bool:
    return ((not x % 15) and bool(x % 21)) <= (bool(x % A) or bool(x % 15))


for A in range(1, 3000):
    if all((f(x, A) for x in range(3000))):
        print(A)
        break
