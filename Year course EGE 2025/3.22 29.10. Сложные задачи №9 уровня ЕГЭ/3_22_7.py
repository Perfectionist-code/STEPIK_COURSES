from statistics import mean


def condition_1(l: list) -> bool:
    return len(set(lst)) == len(lst) - 1


def condition_2(l: list) -> bool:
    return mean(lst[2:]) >= sum(lst[0:2])


with open('3_22_7.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if condition_1(lst) and condition_2(lst):
            print(*lst)
            cnt += 1
print('Ответ:', cnt)
