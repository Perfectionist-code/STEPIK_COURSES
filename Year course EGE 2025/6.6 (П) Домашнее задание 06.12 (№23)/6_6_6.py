def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(2 * curr, end) + f(2 * curr + 1, end)


print(f(5, 46))
