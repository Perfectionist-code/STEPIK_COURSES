def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 3, end) + f(curr * 2, end)


print('Ответ', f(2, 6) * f(6, 10) * f(10, 14))
