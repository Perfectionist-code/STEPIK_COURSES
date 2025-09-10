from itertools import permutations

cnt = 0
for per in permutations('ИГРОК', 5):
    word = ''.join(per)
    if not word.startswith('К') and 'РОК' not in word:
        cnt += 1
print('Ответ:', cnt)
