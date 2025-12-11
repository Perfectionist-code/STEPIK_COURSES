from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:8], repeat=5):
    num = ''.join(pr)
    num1 = num
    for char in '1357':
        num1 = num1.replace(char, '*')
    if not num.startswith('0') and num.count('3') <= 1 and '**' not in num1:
        cnt += 1
        print(num)
print(cnt)
