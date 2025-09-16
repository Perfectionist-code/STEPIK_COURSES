from itertools import product

letters = ''.join(sorted('ДИСПАНЕРЗЦЯ'))
for i, per in enumerate(product(letters, repeat=15), 1):
    word = ''.join(per)
    if word == 'ДИСПАНСЕРИЗАЦИЯ':
        print(f'{i}. {word}')
        print('Ответ: ', i)
        break
544673535870442