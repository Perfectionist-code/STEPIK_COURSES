def f(n):
    if n == 1: return 1
    return f(n - 1) ** 2 - f(n - 1) * n + 2 * n


print('Ответ:', f(4))
