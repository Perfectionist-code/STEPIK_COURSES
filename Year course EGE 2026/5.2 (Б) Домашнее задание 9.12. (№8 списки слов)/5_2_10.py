from itertools import product, repeat

word = ''.join(sorted('ЛЕГКО'))

cnt = 0
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if w.count('Г') >= 2 and 'ГГ' not in w:
        cnt = i
print(cnt)
