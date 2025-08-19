from collections import Counter
from itertools import permutations


def is_condition_1(*args) -> bool:
    if len((set_args := set(args))) == len(args) - 4:
        _count = Counter(args)
        cnt_3 = 0
        cnt_2 = 0
        for num in set_args:
            if _count[num] == 2:
                cnt_2 += 1
            elif _count[num] == 3:
                cnt_3 += 1
        return cnt_2 == 2 and cnt_3 == 1
    return False


def is_condition_2(*args) -> bool:
    for per in permutations(args[:4], 4):
        a, b, c, d = per
        if (a + b) % 2 != 0 and (c + d) % 2 != 0:
            return True
    return False


with open('3_9_7.txt', 'r') as file:
    res = 0
    for str_line in file:
        lst = sorted(map(int, str_line.split()))
        if all((is_condition_1(*lst), is_condition_2(*lst))):
            print(*lst)
            res += sum(lst)
print('Ответ:', res)
