from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:12], repeat=5):
    num = ''.join(pr)
    if not num.startswith('0') and num.count('7') == 1 and sum(int(x, 12) > 8 for x in num) <= 3:
        cnt += 1
print(cnt)
