from itertools import permutations


word = 'ВИКТОР'
cnt = 0
for pr in permutations(word, 4):
    w = ''.join(pr)
    if all(''.join(p) not in w for p in permutations('ИО')) and all(''.join(p) not in w for p in permutations('ВКТР', 2)):
        cnt += 1
print(cnt)
