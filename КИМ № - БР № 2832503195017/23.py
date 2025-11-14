def f(curr, end):
    if curr < end or curr == 20: return 0
    if curr == end: return 1
    return f(curr - 2, end) + f(curr - 3, end) + f(curr // 5, end)


print(f(41, 10) * f(10, 5))
