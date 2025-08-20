from itertools import product

lst = []
res = 0
letters = ''.join(sorted('ИНФАТОП'))
for i, per in enumerate(product(letters, repeat=4), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if word.startswith('Т') and word.endswith('И'):
        res = i
print('Ответ: ', res)
