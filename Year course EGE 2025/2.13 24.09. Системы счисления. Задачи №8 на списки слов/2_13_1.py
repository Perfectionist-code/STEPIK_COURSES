from itertools import product

i = 1
for per in product('ВНРТ', repeat=4):
    print(f'{i}. {''.join(per)}')
    i += 1
    if i == 252:
        break