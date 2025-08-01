from itertools import product

i = 1
word = ''.join(sorted('ПАРУС'))
print(word)
for per in product(word, repeat=3):
    print(f'{i}. {(wrd:=''.join(per))}')
    i += 1
    if wrd[0] == 'С' :
        break