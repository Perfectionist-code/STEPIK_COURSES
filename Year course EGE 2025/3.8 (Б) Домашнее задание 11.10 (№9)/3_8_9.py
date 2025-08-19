from collections import Counter
from statistics import mean


def is_condition_1(*args) -> bool:
    if (set_args := set(args)).__len__() == 4:
        _count = Counter(args)
        cnt_two = 0
        for num in set_args:
            if _count[num] == 1:
                continue
            elif _count[num] == 2:
                cnt_two += 1
            elif _count[num] == 3:
                return False
        return cnt_two == 2
    return False


def is_condition_2(*args) -> bool:
    return mean((args[0], args[-1])) > mean(args[1:-1])


with open('9-228.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = sorted(map(int, str_line.split()))
        if all((is_condition_1(*lst), is_condition_2(*lst))):
            cnt += 1
            print(*lst)
print('Ответ:', cnt)
