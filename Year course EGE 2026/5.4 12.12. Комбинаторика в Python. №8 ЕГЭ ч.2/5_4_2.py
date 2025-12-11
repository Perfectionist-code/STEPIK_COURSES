from itertools import product

word = 'ЕГЭ'
res = set()
for pr in product(word, repeat=5):
    if pr[0] in 'ЕЭ':
        res.add(pr)
print(len(res))
