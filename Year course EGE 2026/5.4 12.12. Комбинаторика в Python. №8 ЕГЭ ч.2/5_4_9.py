from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:8], repeat=5):
    num = ''.join(pr)
    if not num.startswith('0') and num.count('6') == 1 and all(
            x + '6' not in num and '6' + x not in num for x in printable[1:8:2]):
        cnt += 1
print(cnt)
