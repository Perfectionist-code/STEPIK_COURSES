def f(curr: int, end: int):
    if curr < end: return 0
    if curr == end: return 1
    return f(curr - 1, end) + f(curr >> 1, end)


print(f(int('100001', 2), int('100', 2)))
