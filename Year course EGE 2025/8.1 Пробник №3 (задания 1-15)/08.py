from itertools import product

word = 'ПРОБНИК'
word = ''.join(sorted(word))

cnt = 0
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if w.count('О') == 3 and len(set(w)) == 4:
        cnt = i
        print(i, w)
print('----' * 5)
print(cnt)
