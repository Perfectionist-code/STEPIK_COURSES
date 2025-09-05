def f(x: int, A: int) -> bool:
    return (bool(x % 84) or bool(x % 90)) <= bool(x % A)

for A in range(1, 3000):
    if all((f(x,A) for x in range(3000))):
        print(A)
        break
