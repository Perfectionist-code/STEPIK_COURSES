def f(curr, end, step):
    if curr > end or (curr == end and step != 7): return 0
    if curr == end and step == 7: return 1
    return f(curr + 1, end, step + 1) + f(curr + 4, end, step + 1) + f(curr * 2, end, step + 1)


print(f(3, 27, 0))
