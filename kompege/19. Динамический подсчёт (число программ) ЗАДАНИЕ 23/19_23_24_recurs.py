def f(curr, end, k):
    if curr > end or k > 1: return 0
    if curr == end: return k == 1
    return f(curr + 1, end, k + (curr + 1) % 2) + f(curr + 2, end, k + (curr + 2) % 2) + f(curr * 2, end, k)

print(f(2, 40,0))