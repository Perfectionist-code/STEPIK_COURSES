from string import digits, ascii_lowercase

d = {i: x for i, x in enumerate(digits + ascii_lowercase)}


def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(d[r])
    return ''.join(res[::-1])


number = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
number = num_to_cs(number, 12)
print(number.count('b'))
