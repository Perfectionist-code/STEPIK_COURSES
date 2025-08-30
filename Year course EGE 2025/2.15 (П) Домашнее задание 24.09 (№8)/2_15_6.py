from itertools import product

letters = ''.join(sorted('КОФЕ'))
cnt = 0
for i, per in enumerate(product(letters, repeat=5), 1):
    word = ''.join(per)
    if word.count('О') == 1 and all(('КО' not in word, 'ОК' not in word, 'ОФ' not in word, 'ФО' not in word)):
        print(f'{i}. {word}')
        if cnt == 0:
            start_index = i
            cnt += 1
        end_index = i
print('Ответ: ', start_index + end_index)