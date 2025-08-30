from itertools import product

letters = ''.join(sorted('АКЛМНЯ'))
cnt = 0
for i, per in enumerate(product(letters, repeat=5), 1):
    word = ''.join(per)
    if cnt == 0 and word.startswith('МН'):
        start_index = i
        cnt += 1
    if cnt != 0 and word.startswith('МН'):
        print(f'{i}. {word}')
        end_index = i
print('Ответ: ', end_index - start_index - 1)
