def f(x, A):
    return (((x & 13 != 0) or (x & A != 0)) <= (x & 13 != 0)) or (
        (x & A != 0) and (x & 39 == 0)
    )


for A in range(1, 3000):
    if all((f(x, A) for x in range(1, 3000))):
        print(A)
