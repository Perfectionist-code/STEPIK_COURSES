from itertools import product

letters = ''.join(sorted('АОУ', reverse=True))
cnt = 0
for i, per in enumerate(product(letters, repeat=5), 1):
    word = ''.join(per)
    if i == 240:
        print('Ответ: ', word)
