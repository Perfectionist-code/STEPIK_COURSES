from itertools import product

letters = ''.join(sorted('МАРТ'))
for i, per in enumerate(product(letters, repeat=4), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if word == 'МАРТ':
        start_num = i
    if word == 'РАМТ':
        end_num = i
res = abs(end_num - start_num) + 1
print('Ответ: ', res)
