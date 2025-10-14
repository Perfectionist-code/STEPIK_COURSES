def condition_1(l: list) -> bool:
    return (len(set(l)) == len(l) - 2) and (lst[2] == lst[3])


def condition_2(l: list) -> bool:
    return l.count(max(l)) == 1


with open('05.txt') as file:
    cnt = 0
    for s in file:
        lst = list(map(int, s.split()))
        lst = sorted(lst, key=lambda x: (lst.count(x), x), reverse=True)
        if condition_1(lst) and condition_2(lst):
            print(sum(lst))
            break
