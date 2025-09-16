from statistics import mean


def cond_1(l: list) -> bool:
    return all((l[0] == l[1], l[2] == l[3], l[1] != l[2], l[4] != l[5]))


def cond_2(l: list) -> bool:
    l.sort()
    return mean((l[0], l[-1])) < mean(l[1:-1])


with open('3_22_9.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if cond_1(lst) and cond_2(lst):
            print(*lst)
            cnt += 1
print('Ответ:', cnt)
