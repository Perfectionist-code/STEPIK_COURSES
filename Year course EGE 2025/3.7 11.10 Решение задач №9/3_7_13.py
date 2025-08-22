from collections import Counter


def is_condition_1(*args) -> bool:
    set_nums = set(args)
    if set_nums.__len__() == 5:
        _count = Counter(args)
        cnt_two = 0
        for num in set_nums:
            if _count[num] == 3:
                return False
            elif _count[num] == 2:
                cnt_two += 1
            elif _count[num] == 1:
                continue
        if cnt_two == 2:
            return True
    return False


def is_condition_2(*args) -> bool:
    return args.count(max(args)) == 1


with open('3_7_13.txt', 'r') as file:
    for i, str_line in enumerate(file, 1):
        lst = sorted(map(int, str_line.split()))
        if all((is_condition_1(*lst), is_condition_2(*lst))):
            print(*lst)
            res = sum(lst)
            break
print('Ответ:', res)
