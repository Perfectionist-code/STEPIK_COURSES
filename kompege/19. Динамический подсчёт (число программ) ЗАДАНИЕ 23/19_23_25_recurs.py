def f(curr, end, k):
    if curr > end or k > 6: return 0
    if curr == end: return k == 6
    return f(curr + 1, end, k + int(not (curr + 1) % 2)) + f(curr + 3, end, k + int(not (curr + 3) % 2)) + f(curr + 5, end, k + int(not (curr + 5) % 2))


print(f(3, 25, 0))
