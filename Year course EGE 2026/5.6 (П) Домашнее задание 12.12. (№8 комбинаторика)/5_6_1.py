from itertools import product

word = 'КАЛИЙ'

cnt = 0
for pr in product(word, repeat=6):
    w = ''.join(pr)
    if w.count('Й') <= 1 and not w.startswith('Й') and not w.endswith('Й') and 'ИЙ' not in w and 'ЙИ' not in w:
        cnt += 1
        print(w)
print('-----' * 5)
print(cnt)
