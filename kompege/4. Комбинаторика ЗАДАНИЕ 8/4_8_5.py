from itertools import product

word = 'САЛО'
cnt = 0
for per in product(word, repeat=6):
    if 'О' in per and per.count('О') <= 3:
        cnt += 1
        print(f'{cnt}.', ''.join(per))
print('----' * 5)
print('Ответ:', cnt)
