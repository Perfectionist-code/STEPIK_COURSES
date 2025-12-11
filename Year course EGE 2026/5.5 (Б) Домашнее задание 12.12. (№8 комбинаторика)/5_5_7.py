from itertools import permutations

word = 'ЗДАНИЕ'

cnt = 0
for pr in permutations(word, 6):
    word = ''.join(pr)
    word1 = word
    for char in word:
        if char in 'ЕИА':
            word1 = word1.replace(char, '*')
    if '**' not in word1:
        cnt += 1
print(cnt)
