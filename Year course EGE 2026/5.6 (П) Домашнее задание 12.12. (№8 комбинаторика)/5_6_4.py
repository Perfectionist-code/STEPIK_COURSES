from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:14].upper(), repeat=5):
    w = ''.join(pr)
    if not w.startswith('0') and all(x + y not in w and y + x not in w for x in 'ABCD' for y in '13579'):
        cnt += 1
        print(w)
print('-----' * 5)
print(cnt)
