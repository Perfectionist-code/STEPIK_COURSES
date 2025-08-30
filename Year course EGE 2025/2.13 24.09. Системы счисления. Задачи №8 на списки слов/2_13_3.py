from itertools import product

i = 1
word = 'ЛНОС'
for per in product(word, repeat=5):
    print(f'{i}. {''.join(per)}')
    i += 1
    if i == 1021:
        break

