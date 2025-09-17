def f(n):
    if n == 1: return 1
    if n == 2: return 3
    return f(n - 1) * f(n - 2) + (n - 2)


print('Ответ:', f(5))
