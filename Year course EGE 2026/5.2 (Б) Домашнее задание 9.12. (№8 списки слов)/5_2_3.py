from itertools import product, repeat

word = ''.join(sorted('АНМФ'))

for i, pr in enumerate(product(word, repeat=4), 1):
    w = ''.join(pr)
    if not i % 2 and not w.startswith('А') and w.count('Н') >= 2 and 'Ф' not in w:
        print(i)
        break
