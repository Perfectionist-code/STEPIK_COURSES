def f(curr, end, neg):
    if curr > end or curr == neg: return 0
    if curr == end: return 1
    return f(curr + 1, end, neg) + f(curr + 2, end, neg) + f(
        curr * 3, end, neg)


print(f(6, 15, 21) * f(15, 25, 21) + f(6, 21, 15) * f(21, 25, 15))
