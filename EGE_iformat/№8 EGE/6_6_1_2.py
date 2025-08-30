from itertools import product

cnt = 0
for prod in product('БЕДА', repeat=6):
    if all([prod[0] in 'АЕ', prod[-1] in 'БД', prod.count('А') + prod.count('Е') == prod.count('Б') + prod.count('Д')]):
        print(*prod, sep='')
        cnt += 1
print(cnt)