def f(curr, end, cnt_C):
    if curr > end or cnt_C > 2: return 0
    if curr == end: return 1
    return f(curr + 1, end, cnt_C) + f(curr + 2, end, cnt_C) + f(curr * 2, end, cnt_C + 1)


print(f(2, 12, 0))
