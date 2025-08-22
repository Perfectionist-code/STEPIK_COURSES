from itertools import product

i = 1
letters = ''.join(sorted('АЛГОРИТМ'))
for per in product(letters, repeat=4):
    word = ''.join(per)
    print(f'{i}. {word}')
    if word.startswith('ГО'):
        print('Ответ: ', i)
        break
    i += 1
