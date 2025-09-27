def f(n):
    if n < 2: return 1
    if n >= 2 and n % 3: return f(n - 1) + 17
    return f(n // 3) - 1


for i in range(100000):
    if f(i) == 110:
        print(i)
        break