def f(curr, end):
    if curr > end or curr == 17: return 0
    if curr == end: return 1
    return f(curr + 2, end) + f(curr + 3, end) + f(curr * 2, end)


print('Ответ', f(3, 10) * f(10, 25))
