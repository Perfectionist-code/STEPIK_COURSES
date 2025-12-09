from itertools import product, repeat

word = ''.join(sorted('ФОКУС'))

cnt = 0
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if 'Ф' not in w and w.count('У') == 2:
        cnt = i
        print(w)
print(cnt)
