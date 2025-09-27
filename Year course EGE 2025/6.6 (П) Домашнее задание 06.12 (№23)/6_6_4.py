def f(curr, end):
    if curr > end or curr == 43: return 0
    if curr == end: return 1
    return f(curr + 2, end) + f(2 * curr - 1, end) + f(2 * curr + 1, end)

print(f(7, 63))
