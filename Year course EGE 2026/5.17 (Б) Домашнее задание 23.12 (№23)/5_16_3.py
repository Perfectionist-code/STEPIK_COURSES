def f(curr: int, end: int, cnt: int):
    if curr == 30 or curr == 60: cnt += 1
    if curr > end or cnt > 1: return 0
    if curr == end: return cnt == 1
    return f(curr + 1, end, cnt) + f(curr * 2, end, cnt) + f(curr * 3, end, cnt)


print(f(10, 70, 0))
