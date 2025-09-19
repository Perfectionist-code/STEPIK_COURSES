def f(curr, end):
    if curr < end: return 0
    if curr == end: return 1
    return f(curr - 8, end) + f(curr // 2, end)


print(f(102, 43) * f(43, 5))
