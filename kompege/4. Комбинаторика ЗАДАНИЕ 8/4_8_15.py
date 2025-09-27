from itertools import product

letters = 'ДЕЙКСТРА'
cnt = 0
for pr in product(letters, repeat=6):
    if len(set(pr)) == 6 and pr.count('Й') == 1 and pr[-1] != 'Й' and pr[pr.index('Й') + 1] in 'ДКСТР':
        cnt += 1
        print(*pr, sep='')
print(cnt)
