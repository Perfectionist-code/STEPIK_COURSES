from collections import Counter


def condition_1(*args) -> bool:
    if set(args).__len__() == args.__len__() - 2:
        _counter = Counter(args)
        for num in _counter:
            if _counter[num] == 1:
                continue
            elif _counter[num] == 3:
                return True
    return False


def condition_2(*args) -> bool:
    _counter = Counter(args)
    r_p = 0
    r_u = 0
    for num in _counter:
        if _counter[num] == 3:
            r_p = (3 * num) ** 2
        else:
            r_u += num
    return r_u ** 2 < r_p


with open('3_22_3.txt', 'r') as file:
    cnt = 0
    for s in file:
        lst = [*map(int, s.split())]
        if condition_1(*lst) and condition_2(*lst):
            cnt += 1
            print(f'{cnt}. ', *lst)
print('Ответ:', cnt)
