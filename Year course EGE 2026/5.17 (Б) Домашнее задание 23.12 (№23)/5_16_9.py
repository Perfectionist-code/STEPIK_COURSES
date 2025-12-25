def f(curr: int, end: int):
    if curr > end or curr == 13: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 2, end) + f(curr * 3, end)


print(f(3, 8) * f(8, 18))
