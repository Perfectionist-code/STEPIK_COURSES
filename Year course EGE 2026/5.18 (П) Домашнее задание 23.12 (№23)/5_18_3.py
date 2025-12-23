def f(curr: int, end: int, cnt: int):
    if curr > end or cnt > 2: return 0
    if curr == end: return 1
    return f(curr - 2, end, cnt + 1) + f(curr * 2, end, cnt) + f(curr * 3, end, cnt)


print(f(6, 48, 0))
