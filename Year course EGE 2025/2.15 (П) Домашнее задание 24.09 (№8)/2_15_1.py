from itertools import product

letters = ''.join(sorted('ДИСПАНЕРЗЦЯ'))
for i, per in enumerate(product(letters, repeat=15), 1):
    word = ''.join(per)
    if not i % 1_000_000_000:
        print(f'{i}. {word}')
    if word == 'ДИСПАНСЕРИЗАЦИЯ':
        print(f'{i}. {word}')
        print('Ответ: ', i)
        break
