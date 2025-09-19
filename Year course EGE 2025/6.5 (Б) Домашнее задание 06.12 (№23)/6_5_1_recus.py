def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 4, end) + f(curr * 2, end)


print('Ответ:', f(3, 27))
