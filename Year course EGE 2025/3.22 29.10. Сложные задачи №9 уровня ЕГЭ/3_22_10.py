from statistics import mean


def cond_1(l: list) -> bool:
    return all((len(set(l)) == len(l) - 2, l[0] == l[1] == l[2]))


def cond_2(l: list) -> bool:
    return mean(l[3:]) < l[0]


with open('3_22_10.csv', 'r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split(',')))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if cond_1(lst) and cond_2(lst):
            print(*lst)
            cnt += 1
print('Ответ:', cnt)
