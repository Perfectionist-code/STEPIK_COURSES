from itertools import permutations

cnt = 0
for per in permutations('АПОРТ', 5):
    word = ''.join(per)
    if 'АО' not in word and 'ОА' not in word:
        cnt += 1
        print(word)
print('----' * 5)
print('Ответ:', cnt)
