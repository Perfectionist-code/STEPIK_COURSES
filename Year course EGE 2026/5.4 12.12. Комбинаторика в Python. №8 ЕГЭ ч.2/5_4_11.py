from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:5], repeat=6):
    num = ''.join(pr)
    if not num.startswith('0') and num.count('2') >= 1 and num[-1] not in '13':
        cnt += 1
print(cnt)
