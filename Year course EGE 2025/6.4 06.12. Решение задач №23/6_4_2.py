def f(current, end):
    if current > end: return 0
    if current == end: return 1
    return f(current + 2, end) + f(current + 4, end)


print('Ответ:', f(4, 22))
