from itertools import product

i = 1
word = ''.join(sorted('РЕБУС'))
for per in product(word, repeat=5):
    print(f'{i}. {(wrd := ''.join(per))}')
    i += 1
    if wrd.startswith('Е') and 'У' in wrd and wrd.count('Е') + wrd.count('У') > 2:
        break
