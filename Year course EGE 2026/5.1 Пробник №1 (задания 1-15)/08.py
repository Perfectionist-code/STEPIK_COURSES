from itertools import permutations

word = 'АРТЁМ'
cnt = 0
for per in permutations(word):
    if (per[0] in 'АЁ') + (per[-1] in 'АЁ') != 2:
        cnt += 1
        print(''.join(per))
print('----' * 5)
print(cnt)
