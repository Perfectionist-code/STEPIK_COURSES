from itertools import product, repeat

word = ''.join(sorted('БАТЫР'))

for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if 'Ы' not in w and 'АА' not in w:
        print(i)
        break
