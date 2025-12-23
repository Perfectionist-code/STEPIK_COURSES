def f(curr: int, end: int, cmd='0'):
    if curr > end: return 0
    if curr == end: return 1
    if cmd == 'B':
        return f(curr + 2, end, 'A') + f(curr * 3, end, 'C')
    return f(curr + 2, end, 'A') + f(curr ** 2, end, 'B') + f(curr * 3, end, 'C')


print(f(2, 64))
