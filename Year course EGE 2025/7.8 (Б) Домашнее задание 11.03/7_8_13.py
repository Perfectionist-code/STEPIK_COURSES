def num_to_cs(num, cs):
    res = []
    while num:
        num, r = divmod(num, cs)
        res.append(r)
    return res[::-1]


cnt = 0
for i in range(1, 1000000):
    try:
        n = num_to_cs(i, 3)
        if len(n) == 6 and n.count(2) == 1 and n[n.index(2) + 1] % 2 == 0:
            cnt += 1
            print(*n, sep='')
    except:
        continue
print('Ответ:', cnt)
