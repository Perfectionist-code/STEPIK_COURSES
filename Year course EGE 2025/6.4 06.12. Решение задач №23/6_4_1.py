def f(current, end):
    if current > end: return 0
    if current == end: return 1
    return f(current + 1, end) + f(current * 2, end)


print('Ответ:', f(1, 16))
