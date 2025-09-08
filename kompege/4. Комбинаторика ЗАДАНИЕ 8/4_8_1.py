from itertools import product

letters = 'КРЕСЛО'
s_l = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ'
g_l = 'АЕЁИОУЫЭЮЯ'

cnt = 0
for pr in product(letters, repeat=4):
    if (pr[0] in s_l) and (pr[-1] in g_l):
        cnt += 1
        print(f'{cnt}. {''.join(pr)}')
print(cnt)
