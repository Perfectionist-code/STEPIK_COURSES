from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:13], repeat=3):
    num = ''.join(pr)
    if not num.startswith('0') and '8' not in num and len(num) == len(set(num)) and all(
            (int(num[i], 13) % 2 == 0) != (int(num[i + 1], 13) % 2 == 0) for i in range(len(num) - 1)):
        cnt += 1
print(cnt)
