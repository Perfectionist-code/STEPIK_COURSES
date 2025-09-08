from statistics import mean


def condition_1(l: list) -> bool:
    return len(set(l)) == len(l) - 1


def condition_2(l: list) -> bool:
    return mean(l[2:]) <= 2 * l[0]


with open('3_22_4.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if condition_1(lst) and condition_2(lst):
            cnt += 1
            print(f'{cnt}. ', *lst)
print('------' * 10)
print('Ответ:', cnt)
