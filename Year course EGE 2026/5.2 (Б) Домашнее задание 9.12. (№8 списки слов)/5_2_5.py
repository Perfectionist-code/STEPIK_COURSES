from itertools import product, repeat

word = ''.join(sorted('МАНГУСТ'))

cnt = 0
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if not w.startswith('У') and w.count('М') == 2 and w.count('Г') <= 1:
        cnt = i
print(cnt)
