def f(n):
    if n == 1: return 2
    if n == 2: return 4
    return 3 * f(n - 1) - 2 * f(n - 2)


print('Ответ:', f(7))
