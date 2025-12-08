from itertools import permutations

word = 'АКАДЕМИК'

res = set()
for pr in permutations(word):
    w = ''.join(pr)
    w1 = w
    for char in w:
        if char in 'КДМК':
            w1 = w1.replace(char, '*')
        else:
            w1 = w1.replace(char, '#')
    if '**' not in w1 and '##' not in w1:
        res.add(w)
        print(w)
print('-----' * 5)
print(len(res))
