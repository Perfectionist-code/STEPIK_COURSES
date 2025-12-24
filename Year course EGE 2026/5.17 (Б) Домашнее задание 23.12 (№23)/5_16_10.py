def f(curr: int, end: int):
    if curr < end or curr == 35: return 0
    if curr == end: return 1
    return f(curr // 3, end) + f(curr - 2, end) + f(curr - 5, end)


print(f(41, 37) * f(37, 8))
