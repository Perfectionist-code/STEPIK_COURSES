def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    if str(curr)[-2] < str(curr)[-1]:
        return f(curr + 1, end) + f(int(str(curr)[:-2] + str(curr)[-2:][::-1]), end)
    return f(curr + 1, end)


print(f(101, 154))
