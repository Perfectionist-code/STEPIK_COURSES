def f(curr, end, oper="Z"):
    if curr > end: return 0
    if curr == end: return 1
    if oper != 'B':
        return f(curr + 2, end, 'A') + f(curr ** 2, end, 'B') + f(curr * 3, end, 'C')
    return f(curr + 2, end, 'A') + f(curr * 3, end, 'C')


print(f(2, 64))
