def f(x, A) -> bool:
    return (not A % 7) and (not 240 % x) <= (bool(A % x) <= bool(780 % x))


for A in range(1, 3000):
    if all((f(x, A)) for x in range(1, 3000)):
        print(A)
        break
