from itertools import product

cnt = 0
for pr in product('01234567', repeat=7):
    w = ''.join(pr)
    if not w.startswith('0') and sum(x in '0246' for x in w) == 2 and all(
            '7' + x not in w and x + '7' not in w for x in '1357'):
        cnt += 1
        print(w)
print('-----' * 5)
print(cnt)
