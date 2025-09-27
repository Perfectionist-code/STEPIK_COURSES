from itertools import product


def check_word(w) -> bool:
    for i in range(len(w) - 1):
        if ord(w[i]) > ord(w[i + 1]):
            return False
    return True


letters = sorted('ABCD')
cnt = 0
for pr in product(letters, repeat=4):
    if check_word(pr):
        cnt += 1
        print(*pr, sep='')
print(cnt)
