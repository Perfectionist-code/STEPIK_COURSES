from itertools import permutations

cnt = 0
for per in permutations('01234567', 4):
    per = ''.join(per).lstrip('0')
    if all([per.__len__() == 4, not ('26') in per, not ('62' in per)]):
        print(per)
        cnt += 1
print()
print(cnt)
