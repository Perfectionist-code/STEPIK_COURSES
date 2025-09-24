def f(curr, end, p):
    if curr > end: return 0
    if curr == end: return 1
    if curr < end and p == '*2': return f(curr + 1, end, '+1') + f(curr + 2, end, '+2')
    if curr < end and p != '*2': return f(curr + 1, end, '+1') + f(curr + 2, end, '+2') + f(curr * 2, end, '*2')



print(f(1, 15,""))
