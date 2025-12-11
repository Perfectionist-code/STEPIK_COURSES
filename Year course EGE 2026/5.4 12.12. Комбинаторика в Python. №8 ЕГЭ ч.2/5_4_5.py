from itertools import permutations

word = 'АПОРТ'
cnt = 0
for pr in permutations(word, 5):
    w = ''.join(pr)
    if all(''.join(p) not in w for p in permutations('АО')):
        cnt += 1
print(cnt)
