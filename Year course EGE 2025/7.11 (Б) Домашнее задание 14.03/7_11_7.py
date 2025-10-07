from collections import Counter
from statistics import mean


def cond_1(l: list) -> bool:
    _count = Counter(l)
    return (len(set(l)) == len(l) - 2) and 3 in _count.values()


def cond_2(l: list) -> bool:
    return mean(l[3:]) < l[0]


with open('7_11_7.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lst.count, reverse=True)
        if cond_1(lst) and cond_2(lst):
            print(*lst)
            cnt += 1
print('Ответ:', cnt)
