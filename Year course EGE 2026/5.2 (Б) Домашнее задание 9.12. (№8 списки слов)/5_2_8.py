from itertools import product, repeat

word = ''.join(sorted('ЦАПЛЯ'))

cnt = 0
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if  w.count('А') <= 1 and w.count('Ц') == 2 and 'Л' not in w:
        print(i)
        break
