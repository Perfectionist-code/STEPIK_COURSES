from itertools import product

cnt = 0
for pr in product('0123456', repeat=7):
    w = ''.join(pr)
    if not w.startswith('0') and sum(w.count(x) for x in '0246') == 2:
        cnt += 1
        print(w)
print('-----' * 5)
print(cnt)
