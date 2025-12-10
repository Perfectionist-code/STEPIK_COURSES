from itertools import product, repeat

word = ''.join(sorted('СЛОН'))

for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if i == 1020:
        print(w)
        break
