def f(curr: int, end: int):
    if curr < end or curr in (9, 16): return 0
    if curr == end: return 1
    return f(curr - 1, end) + f(curr - 2, end) + f(curr // 3, end)


print(f(19, 3))
