from itertools import product, repeat

letters = 'ВИШНЯ'
cnt = 0
for pr in product(letters, repeat=6):
    word = ''.join(pr)
    if all((word.count('В') <= 1, not word.startswith('Ш'), not word.endswith('И'), not word.endswith('Я'))):
        print(word)
        cnt += 1
print(cnt)
