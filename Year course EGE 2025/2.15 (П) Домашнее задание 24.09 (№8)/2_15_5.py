from itertools import product

letters = ''.join(sorted('АБГОЩ', reverse=True))
cnt = 0
for i, per in enumerate(product(letters, repeat=6), 1):
    word = ''.join(per)
    if word == 'ОБЩАГА':
        print('Ответ: ', i)
        break