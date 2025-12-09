from itertools import product, repeat

word = ''.join(sorted('КОМПЬЮТЕР'))

cnt = 0
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if i % 2 and not w.startswith('Ь') and w.count('К') == 2:
        cnt = i
print(cnt)
