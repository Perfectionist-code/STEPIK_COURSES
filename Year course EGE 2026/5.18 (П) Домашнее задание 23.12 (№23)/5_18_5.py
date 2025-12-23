def f(curr: int, end: int, cnt: int):
    if curr > end or cnt > 2: return 0
    if curr == end: return 1
    return f(curr + 1, end, cnt) + f(curr + 2, end, cnt) + f(curr * 2, end, cnt + 1)


print(f(2, 12, 0))
