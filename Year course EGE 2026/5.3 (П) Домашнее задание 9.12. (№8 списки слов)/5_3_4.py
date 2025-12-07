from itertools import product

word = ''.join(sorted('КОФЕ'))

res = []
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if w.count('О') == 1 and all('О' + x not in w and x + 'О' not in w for x in 'КФ'):
        res.append(i)
        print(i, w)
print(max(res) + min(res))
