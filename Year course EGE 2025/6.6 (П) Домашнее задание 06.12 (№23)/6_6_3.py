def f(curr, end):
    if curr > end or curr == 21: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 4, end) + f(curr + (curr + curr % 2 + 2 * int(not curr % 2)), end)

print(f(2, 11) * f(11, 26))