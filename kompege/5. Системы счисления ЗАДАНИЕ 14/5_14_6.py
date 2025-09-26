d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}


def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r) if r < 10 else d[r])
    return ''.join(res[::-1])

num = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
print(len(set(num_conv:=num_to_cs(num, 15))))
print(num_conv)
