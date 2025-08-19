def is_condition_1(*args) -> bool:
    return set(args).__len__() == args.__len__() - 1


def is_condition_2(*args) -> bool:
    return args.count(args[-1]) == args.count(args[0])


with open('3_9_4.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = sorted(map(int, str_line.split()))
        if all((is_condition_1(*lst), is_condition_2(*lst))):
            cnt += 1
            print(*lst)
print('Ответ:', cnt)
