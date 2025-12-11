from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:9], repeat=5):
    num = ''.join(pr)
    if not num.startswith('0') and num.count('5') == 1 and all(num[i] != num[i + 1] for i in range(4)):
        cnt += 1
        print(num)
print(cnt)
