from itertools import product

cnt = 0
for pr in product('01234567', repeat=5):
    num = ''.join(pr)
    if num[0] in '246' and num[-1] not in '26' and num.count('7') <= 2:
        cnt += 1
print(cnt)
