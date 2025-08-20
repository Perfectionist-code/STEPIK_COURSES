from itertools import product

letters = ''.join(sorted('ПАРУС'))
res = 0
for i, per in enumerate(product(letters, repeat=5), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if word.count('У') <= 1 and 'АА' not in word:
        res = i
print('Ответ: ', res)