from itertools import permutations
from string import printable

cnt = 0
for pr in permutations(printable[:16], 3):
    num = ''.join(pr)
    num1 = num
    for char in set(num):
        if int(char, 16) % 2:
            num1 = num1.replace(char, '*')
        else:
            num1 = num1.replace(char, '#')
    if not num.startswith('0') and '**' not in num1 and '##' not in num1:
        cnt += 1
print(cnt)
