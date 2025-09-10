def to_3(num):
    res = []
    while num:
        num, r = divmod(num, 3)
        res.append(str(r))
    return ''.join(res[::-1])

n = 2 * 27 ** 7 + 3 ** 10 - 9
print('Ответ:', to_3(n).count('0'))