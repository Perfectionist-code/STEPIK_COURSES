from itertools import product

i = 1
word = ''.join(sorted('БАТЫР'))
cnt = 0
for per in product(word, repeat=5):
    print(f'{i}. {(wrd := ''.join(per))}')
    i += 1
    if 'Ы' not in wrd and 'АА' not in wrd:
        break

