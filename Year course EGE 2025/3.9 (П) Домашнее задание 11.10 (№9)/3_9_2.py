def is_condition_1(*args) -> bool:
    return args == tuple(sorted(args))


def is_condition_2(*args) -> bool:
    return set(args).__len__() < args.__len__()


with open('3_9_2.txt', 'r') as file:
    res = 0
    for i, str_line in enumerate(file, 1):
        lst = tuple(map(int, str_line.split()))
        if any((is_condition_1(*lst), is_condition_2(*lst))):
            res += i
            print(*lst)
print('Ответ:', res)
