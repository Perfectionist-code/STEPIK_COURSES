from itertools import product

word = ''.join(sorted('АКЛМНЯ'))

res = []
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if w.startswith('МН'):
        res.append(i)
print(max(res) - min(res) - 1)
