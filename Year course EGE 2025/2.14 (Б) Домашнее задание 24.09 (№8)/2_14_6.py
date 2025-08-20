from itertools import product

letters = ''.join(sorted('АОУ'))
for i, per in enumerate(product(letters, repeat=5), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if i == 240:
        print('Ответ: ', word)
        break