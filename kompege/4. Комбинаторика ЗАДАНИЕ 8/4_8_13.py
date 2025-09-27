from itertools import product

letters = 'ГЕПАРД'
cnt = 0
for pr in product(letters, repeat=5):
    if pr[0] != 'А' and pr[-1] != 'Е' and pr.count('Г') == 1:
        cnt += 1
        print(*pr, sep='')
print(cnt)
