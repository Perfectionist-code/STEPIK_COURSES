from itertools import permutations


def is_true(lst: list) -> bool:
    for per in permutations(lst, 4):
        print(per)
        if per[0] + per[1] == per[2] + per[3]:
            return True
    return False


with open('o_9_3.txt', 'r') as file:
    cnt = 0
    for l in file:
        l = sorted(map(int, l.split()))
        if l[3] < sum(l[:3]) and is_true(l):
            cnt += 1
        print('---' * 10)
    print(cnt)
