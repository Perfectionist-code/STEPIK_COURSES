def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    if curr % 2 == 0:
        return f(curr + 1, end) + f(curr + 2, end) + f(curr * 2, end)
    else:
        return f(curr * 2, end)

print(f(1, 32))