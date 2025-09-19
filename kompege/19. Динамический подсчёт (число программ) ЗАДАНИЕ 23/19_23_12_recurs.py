def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 2, end) + f(2 * curr + 1, end) + f(curr * 10, end)

print(f(1,15))
