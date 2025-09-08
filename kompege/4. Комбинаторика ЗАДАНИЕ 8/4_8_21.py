from itertools import product

letters = ''.join(sorted('МАРИЯ'))

for i, pr in enumerate(product(letters, repeat=4), 1):
    if i == 211:
        print('Ответ:', ''.join(pr))
        break
