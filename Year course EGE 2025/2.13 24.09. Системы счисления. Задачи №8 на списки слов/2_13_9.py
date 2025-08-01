from itertools import product

i = 1
word = ''.join(sorted('ЦАПЛЯ'))
for per in product(word, repeat=5):
    print(f'{i}. {(wrd := ''.join(per))}')
    i += 1
    if (wrd.count('А') <= 1) and (wrd.count('Ц') == 2) and ('Л' not in wrd):
        break
