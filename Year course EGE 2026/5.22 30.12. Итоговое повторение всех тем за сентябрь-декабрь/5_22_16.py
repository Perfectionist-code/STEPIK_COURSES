def f(curr, end):
    if curr < end or curr == 36: return 0
    if curr == end: return 1
    return f(curr - 3, end) + f(curr - 6, end) + f(curr // 2, end)


print(f(86, 53) * f(53, 12))
