from math import prod


def cond1(l: list) -> bool:
    return l[-1] ** 3 >= 2 * prod(l[:-1])


def cond2(l: list) -> bool:
    return all((x > 10 for x in l))


with open('09_9_4637.txt') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if cond1(lst) and cond2(lst):
            cnt += 1
            print(*lst)
print('----' * 5)
print(cnt)
