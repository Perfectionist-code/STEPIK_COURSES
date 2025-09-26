def f(curr, end, k):
    if curr > end or k > 3: return 0
    if curr == end: return k <= 3
    return f(curr + 2, end, k) + f(curr * 3, end, k + 1) + f(curr * 5, end, k + 1)

print(f(2, 200, 0))
