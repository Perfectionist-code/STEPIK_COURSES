from itertools import product, repeat

letters = ''.join(sorted('МАРИЯ'))
res = 0

for i, pr in enumerate(product(letters, repeat= 4), 1):
    word = ''.join(pr)
    if word.startswith('АРИЯ'):
        res = i
        break
print(res)