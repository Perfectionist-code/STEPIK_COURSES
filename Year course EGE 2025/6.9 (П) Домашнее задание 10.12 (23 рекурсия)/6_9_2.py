def f(curr, end, oper="Z"):
    if curr > end: return 0
    if curr == end: return 1
    if oper != 'A':
        return f(curr + 1, end, 'A') + f(curr +  3 , end, 'B') + f(curr * 2, end, 'C')
    return f(curr +  3 , end, 'B') + f(curr * 2, end, 'C')


print(f(3, 30))
