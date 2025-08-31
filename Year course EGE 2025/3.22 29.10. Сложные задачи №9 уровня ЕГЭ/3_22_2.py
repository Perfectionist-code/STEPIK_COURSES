from collections import Counter


def condition_1(*args) -> bool:
    _count = Counter(args)
    cnt_two = 0
    if len(set(args)) == len(args) - 2:
        for num in _count:
            if _count[num] >= 3:
                return False
            elif _count[num] == 2:
                cnt_two += 1
            elif _count == 1:
                continue
    return cnt_two == 2


def condition_2(*args) -> bool:
    return args.count(max(args)) == 1


with open('3_22_2.txt', 'r') as file:
    for s in file:
        lst = sorted(map(int, s.split()))
        if condition_1(*lst) and condition_2(*lst):
            print(*lst)
            print('Ответ:', sum(lst))
            break
