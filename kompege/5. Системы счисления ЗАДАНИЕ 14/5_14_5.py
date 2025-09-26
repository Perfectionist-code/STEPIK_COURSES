def to_5(num):
    res = []
    while num:
        num, r = divmod(num, 5)
        res.append(str(r))
    return ''.join(res[::-1])


for x in range(1,3000):
    if to_5(125 ** 200 - 5 ** x + 74).count('4') == 100:
        print('Ответ:', x)
        break
