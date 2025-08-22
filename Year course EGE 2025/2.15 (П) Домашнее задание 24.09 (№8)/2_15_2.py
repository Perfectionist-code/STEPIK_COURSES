from itertools import product

letters = ''.join(sorted('ПРОБНИК'))
res = 0
for i, per in enumerate(product(letters, repeat=6), 1):
    word = ''.join(per)
    # print(f'{i}. {word}')
    if word.count('О') == 3 and len(set(word)) == 4:
        print(f'{i}. {word}')
        res = i
print('Ответ: ', res)
