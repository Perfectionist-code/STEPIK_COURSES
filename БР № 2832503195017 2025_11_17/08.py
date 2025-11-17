from itertools import product

word = ''.join(sorted('МИНУС'))

for i, w in enumerate(product(word, repeat=4), 1):
    w = ''.join(w)
    # print(f'{i}: w')
    t = w
    for char in 'МНС':
        t = t.replace(char, '*')
    for char in 'ИУ':
        t = t.replace(char, '#')
    if t.count('*') >= t.count('#'):
        print(f'{i}: {w}')
        cnt = i
print(cnt)
