from itertools import product

word = ''.join(sorted('ФЕВРАЛЬ'))

for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if 'Е' not in w and 'А' not in w:
        print(i, w)
        break

