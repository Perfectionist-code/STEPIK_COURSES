from itertools import product

word = ''.join(sorted('ВЕЧНОСТЬ'))

cnt = 0
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if not i % 2 and w.count('О') >= 2 and w[0] not in 'ВЧНСТ':
        cnt += 1
        print(i, w)
print('----' * 5)
print(cnt)
