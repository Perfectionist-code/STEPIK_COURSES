from itertools import product

i = 1
for per in product('НРТУ', repeat=4):
    print(f'{i}. {''.join(per)}')
    i += 1
    if i == 216:
        break

