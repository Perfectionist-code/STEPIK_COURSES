from itertools import permutations


def check_letters(word, pack):
    print('----' * 5)
    for per_g in permutations(pack, 2):
        word1 = ''.join(per_g)
        print(word1)
        if word1 in word:
            return False
    return True


cnt = 0
g_l = 'АИОУ'
s_l = 'БКЛН'
for per in permutations('АИОУБКЛН'):
    word = ''.join(per)
    if check_letters(word, g_l) and check_letters(word, s_l):
        cnt += 1
        # print(word)
print('-----' * 5)
print(cnt)