def to_4(num):
    res = []
    while num:
        num, r = divmod(num, 4)
        res.append(str(r))
    return ''.join(res[::-1])


n = 3 * 16 ** 8 - 4 ** 5 + 3
print(to_4(n).count('3'))
