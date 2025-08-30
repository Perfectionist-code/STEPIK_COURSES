def is_condition_1(*args) -> bool:
    return set(args).__len__() == args.__len__() - 1


def is_condition_2(*args) -> bool:
    return (args[-2] + args[-1]) / (args[0] + args[1]) > 2


def is_condition_3(*args) -> bool:
    return bool(args[-1] % args[0])


with open('3_9_3.csv', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = sorted(map(int, str_line.split(';')))
        if all((is_condition_1(*lst), is_condition_2(*lst), is_condition_3(*lst))):
            cnt += 1
            print(*lst)
print('Ответ:', cnt)
