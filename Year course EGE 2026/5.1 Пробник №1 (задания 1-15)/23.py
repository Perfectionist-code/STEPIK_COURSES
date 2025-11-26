def f(curr, end):
    if curr > end or curr == 35: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 2, end) + f(curr + 4, end)

print(f(24,33)*f(33, 42))
