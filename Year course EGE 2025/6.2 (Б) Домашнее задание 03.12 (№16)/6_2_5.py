def f(n):
    if n < 2: return 1
    return f(n - 1) + f(n - 2)


for i in range(300):
    if f(i) == 34:
        print('Ответ:', i)
        break