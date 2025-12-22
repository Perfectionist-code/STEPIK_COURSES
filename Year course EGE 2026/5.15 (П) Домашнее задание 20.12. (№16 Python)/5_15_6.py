def f(n):
    if n <= 5: return n
    if n > 5 and n % 5: return n + f(n + 6)
    return n + f(n // 5 + 1)


for n in range(-1000, 1000):
    try:
        if f(n) > 1000:
            print(n)
            break
    except RecursionError:
        continue
