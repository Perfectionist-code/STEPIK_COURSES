def f(n):
    if n <= 1: return n
    if n > 1 and n % 3: return n + f(n + 3)
    return n + f(n // 3)


for n in range(-1000, 1000):
    try:
        if f(n) > 100:
            print(n)
            break
    except RecursionError:
        continue
