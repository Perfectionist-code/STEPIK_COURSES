def f(curr, end, k):
    if k > 1: return 0
    if curr > end: return 0
    if curr == end: return k == 1
    return f(curr + 1, end, k) + f(curr + 2, end, k) + f(curr * 2, end, k + 1)


print(f(2, 12, 0))
