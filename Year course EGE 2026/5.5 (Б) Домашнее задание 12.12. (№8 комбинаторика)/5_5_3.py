from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:7], repeat=4):
    num = ''.join(pr)

    if not num.startswith('0') and num.count('5') == 1 and all(x + '5' not in num and '5' + x not in num for x in '135'):
        cnt += 1
print(cnt)
