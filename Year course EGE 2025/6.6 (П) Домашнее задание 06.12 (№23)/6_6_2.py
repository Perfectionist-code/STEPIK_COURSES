from math import factorial


def f(curr, end):
    if curr > end:  return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr + 4, end) + f(curr + factorial(curr), end)

print(f(1, 10) * f(10, 20))
