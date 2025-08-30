from itertools import product

letters = ''.join(sorted('АЗНС'))
for i, per in enumerate(product(letters, repeat=5), 1):
    word = ''.join(per)
    print(f'{i}. {word}')
    if word == 'САЗАН':
        start_num = i
    if word == 'ЗАНАС':
        end_num = i
res = abs(end_num - start_num) + 1
print('Ответ: ', res)