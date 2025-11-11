def f(curr, end, cnt_A):
    if curr > end or cnt_A > 2: return 0
    if curr == end: return 1
    return f(curr - 2, end, cnt_A + 1) + f(curr * 2, end, cnt_A) + f(curr * 3, end, cnt_A)


print(f(6, 48, 0))
