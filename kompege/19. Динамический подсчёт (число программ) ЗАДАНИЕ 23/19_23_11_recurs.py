def f(curr, end):
    if curr > end or curr in (11, 18): return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 2, end) + f(curr * 3, end)


print(f(4, 8) * f(8, 23))
