from itertools import product

letters = set('ABCWXYZ')
trigger_letters = set('WXYZ')
cnt = 0
for pr in product(letters, repeat=6):
    if pr[0] in trigger_letters and pr[-1] in trigger_letters and not (set(pr[1:-1]) & trigger_letters):
        cnt += 1
        print(''.join(pr))

print(cnt)
