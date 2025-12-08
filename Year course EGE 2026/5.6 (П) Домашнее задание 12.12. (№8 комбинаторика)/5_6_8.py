from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:13].upper(), repeat=6):
    w = ''.join(pr)
    w1 = w
    for char in w:
        if int(char, 13) % 2:
            w1 = w1.replace(char, '*')
        else:
            w1 = w1.replace(char, '#')
    if not w.startswith('0') and w.count('5') <= 1 and '**' not in w1:
        cnt += 1
        print(w)
print('-----' * 5)
print(cnt)
