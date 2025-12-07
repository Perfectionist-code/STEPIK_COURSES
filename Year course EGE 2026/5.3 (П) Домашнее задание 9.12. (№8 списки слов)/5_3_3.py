from itertools import product

word = ''.join(sorted('МОДУЛЬ'))

res = []
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if not i % 2 and w.startswith('М'):
        res.append(i)
print(max(res) - min(res) - 1)
