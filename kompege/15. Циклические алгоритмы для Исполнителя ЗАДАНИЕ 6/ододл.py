from itertools import permutations

res = set()

word = '123400000'
for per in permutations(word):
    # print(*per, sep='')
    res.add(per)
print(*res, sep='\n')