from itertools import product

word = 'ПИР'
res = set()
for pr in product(word, repeat=5):
    if pr.count('П') == 1:
        res.add(pr)
print(len(res))
