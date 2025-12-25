def f(curr: int, end: int):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 2, end)


print(f(4, 8) * f(8, 10) * f(10, 15))
