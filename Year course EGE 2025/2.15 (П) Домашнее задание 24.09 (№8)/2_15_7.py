from itertools import product

letters = ''.join(sorted('ФАВОРИТ'))
cnt = 0
for i, per in enumerate(product(letters, repeat=7), 1):
    word = ''.join(per)
    if all(('ТРИО' in word, i % 2, not word.startswith('ТРИО'), not word.endswith('ТРИО'))):
        print(f'{i}. {word}')
        cnt += 1
print('Ответ: ', cnt)