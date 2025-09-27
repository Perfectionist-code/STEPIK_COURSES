from itertools import permutations

letters = 'МИМИКРИЯ'
cnt = 0
res = set()
for pr in permutations(letters):
    res.add(''.join(pr))
print(len(res))
