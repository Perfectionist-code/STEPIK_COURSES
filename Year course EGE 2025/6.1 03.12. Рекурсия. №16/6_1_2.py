def f(n: int):
    if n == 1:
        return 1
    return 2 * f(n - 1) + 1


print('Ответ:', f(6))
