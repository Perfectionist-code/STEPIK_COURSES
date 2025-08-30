from collections import Counter


def is_condition_1(*args) -> bool:
    a, b, c, d, e, f, g = args
    set_nums = set(args)
    if set_nums.__len__() == 5:
        _count = Counter(args)
        for num in set_nums:
            if _count[num] == 3:
                return True
            elif _count[num] == 2:
                return False
            elif _count[num] == 1:
                continue
    return False


def is_condition_2(*args) -> bool:
    cnt_even = 0
    cnt_odd = 0
    for num in args:
        if num % 2:
            cnt_odd += 1
        else:
            cnt_even += 1
    return cnt_even > cnt_odd


with open('3_7_12.txt', 'r') as file:
    for i, str_line in enumerate(file, 1):
        lst = sorted(map(int, str_line.split()))
        if all((is_condition_1(*lst), is_condition_2(*lst))):
            print(*lst)
            res = i
print('Ответ:', res)
