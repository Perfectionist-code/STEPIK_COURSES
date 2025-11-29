from itertools import product

word = ''.join(sorted('РЕПЛИКА'))

cnt = 0
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if not i % 2 and w[0] != 'К' and w.count('И') >= 2:
        print(i, w)
        cnt += 1
print('----' * 5)
print(cnt)
