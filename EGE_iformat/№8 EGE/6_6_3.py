from itertools import product

cnt = 0
for prod in product('ШКОЛА', repeat=6):
    prod = ''.join(prod)
    if all([not ('ОА' in prod), not ('АО' in prod), not ('ОО' in prod), not ('АА' in prod)]):
        print(prod)
        cnt += 1
print(cnt)
