def f(curr, end):
    if curr > end or curr == 21: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 3, end) + f(curr * 4, end)


print('Ответ:', f(2, 16) * f(16, 60))
