from itertools import product, repeat

word = ''.join(sorted('ЛАЙМ'))

cnt = 0
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if  w.count('М') <= 1 and 'ЛЛ' not in w:
        cnt = i
        print(w)
print(cnt)
