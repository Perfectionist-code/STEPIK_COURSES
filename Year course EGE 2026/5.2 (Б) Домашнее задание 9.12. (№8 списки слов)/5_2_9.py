from itertools import product, repeat

word = ''.join(sorted('ГОНДУБШ'))

cnt = 0
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if i % 2 and not w.startswith('Б') and w.count('Н') >= 2 and 'У' not in w:
        cnt = i
print(cnt)
