from itertools import permutations


def cond_1(l: list) -> bool:
    return l[0] == l[1] == l[2] and l[2] != l[3] and l[3] == l[4] and l[4] != l[5] and l[5] == l[6]


def cond_2(l: list) -> bool:
    l = sorted(l)[:4]
    for per in permutations(l):
        s1 = sum(per[:2])
        s2 = sum(per[2:])
        if s1 % 2 and s2 % 2:
            return True
    return False


with open('04.txt') as file:
    sum_nums = 0
    for s in file:
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if cond_1(lst) and cond_2(lst):
            print(*lst)
            sum_nums += sum(lst)
print('----' * 5)
print(sum_nums)