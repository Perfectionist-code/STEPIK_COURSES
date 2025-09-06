from itertools import product

letters = 'ПУЛЯ'
cnt = 0
for pr in product(letters, repeat=6):
    if pr.count('У') == 2:
        cnt += 1

print(cnt)
