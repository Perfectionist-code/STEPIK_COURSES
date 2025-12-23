def num_tu_cs_3(num: int) -> str:
    res = []
    while num:
        num, r = divmod(num, 3)
        res.append(str(r))
    return ''.join(res[::-1])


def f(curr: int, end: int):
    curr_3cs = num_tu_cs_3(curr)
    if curr < end: return 0
    if curr == end: return 1
    if curr_3cs[-1] == '0': return f(curr - 2, end)
    return f(curr - 2, end) + f(int(curr_3cs[:-1] + '0', 3), end)


print(f(int('212', 3), int('10', 3)))
