from itertools import product, repeat

word = ''.join(sorted('ГИРЛЯНДА'))

cnt = 0
for pr in product(word, repeat=6):
    cnt += 1
    w = ''.join(pr)
    # print(w)
    if cnt % 2 == 0 and w[0] != 'Я' and w.count('Д') == 3:
        print(cnt, w)
