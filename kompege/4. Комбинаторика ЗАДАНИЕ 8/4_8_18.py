from itertools import product, repeat

letters = ''.join(sorted('ЛЕМУР'))
print(letters)
cnt = 0
for pr in product(letters, repeat= 4):
    cnt += 1
    if pr[0] == 'Л':
        print(cnt)
        break