def increase_digit(num: int) -> int:
    num = str(num)
    res = []
    for char in num:
        if (char := int(char)) < 9:
            res.append(str(char + 1))
        else:
            res.append(str(char))
    return int(''.join(res))


def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(increase_digit(curr), end)


print(f(25, 51))
