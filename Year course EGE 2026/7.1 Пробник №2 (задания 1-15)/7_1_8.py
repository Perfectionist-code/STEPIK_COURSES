from itertools import product

word = ''.join(sorted('СТРЕЛА'))

cnt = 0
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if not i % 2 and w[0] not in 'АСТ' and w.count('Л') == 2 and 'ЛЛ' not in w:
        print(i, w)
        cnt = i
print('----' * 5)
print(cnt)
