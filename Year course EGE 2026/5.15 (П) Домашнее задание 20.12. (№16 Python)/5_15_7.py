def f(n):
    if n <= 5: return n
    if n > 5 and n % 4: return n + f(n + 2)
    return n + f(n // 2 - 1)


for n in range(-1000, 1000):
    try:
        if f(n):
            print(n)
    except RecursionError:
        continue
