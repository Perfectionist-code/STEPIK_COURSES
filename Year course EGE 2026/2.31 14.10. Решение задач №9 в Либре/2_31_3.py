from itertools import permutations


def condition_1(l: list) -> bool:
    return lst[0] < sum(lst[1:])


def condition_2(l: list) -> bool:
    return any((per[0] + per[1] == per[2] + per[3] for per in permutations(lst)))


with open('03_9-160.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()), reverse=True)
        if condition_1(lst) and condition_2(lst):
            cnt += 1
            print(*lst)
print('----' * 5)
print(cnt)
