from itertools import product

cnt = 0
for prod in product('АРБУЗИК', repeat=5):
    cnt_vowel_letters = 0
    for char in set(prod) & set('АУИ'):
        cnt_vowel_letters += prod.count(char)
    if cnt_vowel_letters <= 3:
        print(*prod, sep='')
        cnt += 1
print(cnt)
