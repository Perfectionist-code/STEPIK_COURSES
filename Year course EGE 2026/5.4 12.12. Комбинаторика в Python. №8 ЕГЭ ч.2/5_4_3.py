from itertools import product

word = 'ABCX'
res = set()
for pr in product(word, repeat=5):
    if 'X' not in pr or (pr[-1] == 'X' and 'X' not in pr[:-1]):
        res.add(pr)
        # print(''.join(pr))
print(len(res))
