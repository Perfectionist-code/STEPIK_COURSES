from string import digits, ascii_lowercase

d = {i: x for i, x in enumerate(digits + ascii_lowercase)}


def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(d[r])
    return ''.join(res[::-1])


num = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
num = num_to_cs(num, 25)
print(num.count('0'))
