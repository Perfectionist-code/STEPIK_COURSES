def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    if curr < end and not curr % 2: return f(curr + 1, end) + f(int(curr * 1.5), end)
    if curr < end and curr % 2: return f(curr + 1, end)


print(f(1, 20))
