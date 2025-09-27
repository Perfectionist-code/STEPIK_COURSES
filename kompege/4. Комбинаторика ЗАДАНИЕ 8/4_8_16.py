from itertools import permutations

letters = 'ВАЙФУ'
cnt = 0
for pr in permutations(letters, 4):
    word = ''.join(pr)
    if word[0] != 'Й' and 'ВФ' not in word and 'ФВ' not in word:
        cnt += 1
        print(*pr, sep='')
print(cnt)
