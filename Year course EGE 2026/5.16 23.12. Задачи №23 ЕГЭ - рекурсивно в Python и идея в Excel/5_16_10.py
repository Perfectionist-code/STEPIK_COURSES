def f(curr: int, end: int, cnt):
    if curr == 15 or curr == 21:
        cnt += 1
    if curr > end or cnt > 1: return 0
    if curr == end: return cnt == 1
    return f(curr + 1, end, cnt) + f(curr + 2, end, cnt) + f(curr * 3, end, cnt)


print(f(6, 25, 0))
