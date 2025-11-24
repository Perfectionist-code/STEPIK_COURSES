def num_to_cs(num: int, cs: int) -> str:
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(str(r))
    return ''.join(res[::-1])


cnt = 0
for n in range(7500, 47655):
    n = num_to_cs(n, 6)
    if len(n) == 6 and n.count('0') == 1 and all(('0' + x not in n) and (x + '0' not in n) for x in '13579'):
        cnt += 1
        print(n)
print('----' * 5)
print(cnt)
