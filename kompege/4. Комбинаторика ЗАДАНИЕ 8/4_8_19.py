from itertools import product, repeat

letters = ''.join(sorted('АЛГОРИТМ'))
res = 0

for i, pr in enumerate(product(letters, repeat= 4), 1):
    word = ''.join(pr)
    if word.endswith('ИМ'):
        res = i
print(res)