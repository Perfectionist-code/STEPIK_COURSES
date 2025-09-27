from itertools import product


def cond(w: str) -> bool:
    lst = list(map(int, w))
    for i in range(len(lst) - 1):
        if lst[i] % 2 == lst[i + 1] % 2:
            return False
    return True

cnt = 0
chars = '01234567'
for pr in product(chars, repeat=5):
    word = ''.join(pr).lstrip('0')
    if all((len(word) == 5, '1' not in word, len(set(word)) == len(word), cond(word))):
        print(word)
        cnt += 1
print(cnt)