from itertools import product

word = 'ЛОДКА'
cnt = 0
for per in product(word, repeat=4):
    if per.count('О') >= 2:
        cnt += 1
        print(f'{cnt}.', ''.join(per))
print('-----' * 10)
print('Ответ:', cnt)
