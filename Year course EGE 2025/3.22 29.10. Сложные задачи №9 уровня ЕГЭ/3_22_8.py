from collections import Counter


def cond_1(l: list) -> bool:
    return l[0] != l[1]


def cond_2(l: list) -> bool:
    return len(set(l)) < len(l)


def cond_3(l: list) -> bool:
    _count = Counter(l)
    res = 0
    for num, counter in _count.items():
        if counter > 1:
            res += num * counter
    return l[0] + l[-1] < res


with open('3_22_8.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = sorted(map(int, s.split()))
        if cond_1(lst) and cond_2(lst) and cond_3(lst):
            print(*lst)
            cnt += 1
print('Ответ:', cnt)
