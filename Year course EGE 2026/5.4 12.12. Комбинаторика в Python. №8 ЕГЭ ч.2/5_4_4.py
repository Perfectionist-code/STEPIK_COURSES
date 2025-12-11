from itertools import permutations

word = 'КРОЙ'
cnt = 0
for pr in permutations(word, 4):
    w = ''.join(pr)
    if w[0] != 'Й' and 'ОЙ' not in w:
        cnt += 1
print(cnt)
