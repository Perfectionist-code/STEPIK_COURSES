from itertools import product

i = 1
word = ''.join(sorted('АОУ'))
for per in product(word, repeat=5):
    print(f'{i}. {(wrd := ''.join(per))}')
    i += 1
    if wrd == 'ОАОАО':
        break
print(i - 1)
