from itertools import product

letters = ''.join(sorted('КЛРТ'))
for i, per in enumerate(product(letters, repeat=4), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if i == 67:
        print('Ответ: ', word)
        break