def f(curr, end):
    if curr > end or '6' in str(curr): return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 2, end) + f(curr * 2, end)


print(f(1, 38))
