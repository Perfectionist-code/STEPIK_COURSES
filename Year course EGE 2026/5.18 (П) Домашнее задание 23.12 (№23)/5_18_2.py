def f(curr: int, end: int, cmd='0'):
    if curr > end: return 0
    if curr == end: return 1
    if cmd == '1':
        return f(curr + 3, end, '2') + f(curr * 2, end, '3')
    return f(curr + 1, end, '1') + f(curr + 3, end, '2') + f(curr * 2, end, '3')


print(f(3, 30))
