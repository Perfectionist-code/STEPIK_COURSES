from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:7], repeat=5):
    num = ''.join(pr)
    if not num.startswith('0') and num.count('6') == 1 and all(x + x not in num for x in set(num)):
        cnt += 1
        print(num)
print(cnt)
