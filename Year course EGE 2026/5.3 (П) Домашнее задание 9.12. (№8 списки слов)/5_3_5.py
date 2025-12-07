from itertools import product

word = ''.join(sorted('ФАВОРИТ'))

cnt = 0
for i, pr in enumerate(product(word, repeat=7), 1):
    w = ''.join(pr)
    if i % 2 and 'ТРИО' in w and not w.startswith('ТРИО') and not w.endswith('ТРИО'):
        cnt += 1
        print(cnt, w)
print('----' * 5)
print(cnt)
