def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])


n = 5 ** 55 + 555 * 5 ** 555 - 5
n = num_to_cs(n, 5)
print('Ответ:', n.count('0'))
