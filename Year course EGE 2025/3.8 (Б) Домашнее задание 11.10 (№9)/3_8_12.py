def is_condition_1(*args) -> bool:
    s1 = (args[0] + args[-1]) ** 2
    s2 = sum([x ** 2 for x in args[1:-1]])
    return s1 > s2


def is_condition_2(*args) -> bool:
    return set(args).__len__() < len(args)


with open('9-177.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = sorted(map(int, str_line.split()))
        if all((is_condition_1(*lst), is_condition_2(*lst))):
            cnt += 1
            print(*lst)
print('Ответ:', cnt)
