cnt = 0
for k in (0, 1):
    for l in (0, 1):
        for m in (0, 1):
            for n in (0, 1):
                if not ((k or l) <= (l and m and n)):
                    print(k, l, m, n, sep='')
                    cnt += 1
print('Ответ:', cnt)