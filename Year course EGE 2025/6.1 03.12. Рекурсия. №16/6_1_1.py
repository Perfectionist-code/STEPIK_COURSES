def f(n: int):
    if n == 1:
        return 1
    return f(n - 1) * n
print('Ответ:', f(5))
