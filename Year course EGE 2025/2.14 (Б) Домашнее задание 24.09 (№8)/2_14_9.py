from itertools import product

letters = ''.join(sorted('РЕБУС'))
for i, per in enumerate(product(letters, repeat=5), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if word.count('Б') <= 1 and 'ЕЕ' not in word:
        print('Ответ: ', i)
        break
