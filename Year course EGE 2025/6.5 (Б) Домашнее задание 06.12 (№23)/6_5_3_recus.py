def f(curr, end):
    if curr > end or curr == 15: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 3, end)


print('Ответ:', f(2, 10) * f(10, 20))
