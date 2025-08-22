from collections import Counter


def is_condition_1(*args) -> bool:
    _count = Counter(args)
    if (set_args := set(args)).__len__() == args.__len__() - 2:
        for num in set_args:
            if _count[num] == 1:
                continue
            elif _count[num] == 2:
                return False
            elif _count[num] == 3:
                return True
    return False


def is_condition_2(*args) -> bool:
    return args == tuple(sorted(args))


with open('3_9_1.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = tuple(map(int, str_line.split()))
        if is_condition_1(*lst) + is_condition_2(*lst) <= 1:
            cnt += 1
            print(*lst)
print('Ответ:', cnt)
