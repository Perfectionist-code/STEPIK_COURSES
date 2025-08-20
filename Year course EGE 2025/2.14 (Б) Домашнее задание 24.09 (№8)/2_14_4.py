from itertools import product

letters = ''.join(sorted('УЦЮТПСОШ'))
for i, per in enumerate(product(letters, repeat=6), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if word == 'ЮШОССО':
        print('Ответ: ', i)
        break