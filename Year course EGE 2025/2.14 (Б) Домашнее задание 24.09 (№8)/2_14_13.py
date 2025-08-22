from itertools import product

letters = ''.join(sorted('МАНГУСТ'))
res = 0
for i, per in enumerate(product(letters, repeat=6), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if (not word.startswith('У')) and (word.count('М') == 2) and (word.count('Г') <= 1):
        res = i
print('Ответ: ', res)
