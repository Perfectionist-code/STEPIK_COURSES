from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:9], repeat=5):
    num = ''.join(pr)

    if num[0] in '1357' and sum(int(x, 9) % 2 == 0 for x in num) <= 1:
        cnt += 1
print(cnt)
