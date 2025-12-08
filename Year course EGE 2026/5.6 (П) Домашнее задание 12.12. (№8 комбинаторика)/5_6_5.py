from itertools import product
from string import printable

cnt = 0
for pr in product(printable[:20].upper(), repeat=5):
    w = ''.join(pr)
    w1 = w
    for char in w:
        if int(char, 20) % 2:
            w1 = w1.replace(char, '*')
        else:
            w1 = w1.replace(char, '#')
    if not w.startswith('0') and (w1 == '*#*#*' or w1 == '#*#*#') and ((int(w[0], 20) + int(w[-1], 20)) == 26):
        cnt += 1
        print(w)
print('-----' * 5)
print(cnt)
