from itertools import product

letters = '0123456789'
cnt = 0
for pr in product(letters, repeat=3):
    if pr[0] != '0' and pr[0]<=pr[1]<=pr[2]:
        cnt += 1
        print(*pr, sep='')
print(cnt)
