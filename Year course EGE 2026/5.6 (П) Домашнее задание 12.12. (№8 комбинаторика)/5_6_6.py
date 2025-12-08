from itertools import product

word = 'ГЕРАКЛИТ'

cnt = 0
for pr in product(word, repeat=6):
    w = ''.join(pr)
    w1 = w
    for char in w:
        if char in 'ГРКЛТ':
            w1 = w1.replace(char, '*')
        else:
            w1 = w1.replace(char, '#')
    if len(set(w)) == 6 and w1.count('*') > w1.count('#') and '##' not in w1:
        cnt += 1
        print(w)
print('-----' * 5)
print(cnt)
