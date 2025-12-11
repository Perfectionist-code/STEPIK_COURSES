from itertools import permutations
from string import printable

cnt = 0
for pr in permutations(printable[:10], 8):
    num = ''.join(pr)
    if not num.startswith('0') and num[-1] in '05' and all(bool((int(num[i]) + int(num[i + 1])) % 2) for i in range(7)):
        cnt += 1
        print(num)
print(cnt)
