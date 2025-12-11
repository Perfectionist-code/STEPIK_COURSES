from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:15], repeat=5):
    num = ''.join(pr)
    if not num.startswith('0') and num.count('8') == 1 and sum(int(x, 15) > 9 for x in num) >= 2:
        cnt += 1
print(cnt)
