from statistics import mean


def is_condition_1(*args) -> bool:
    return set(args).__len__() == 6


def is_condition_2(*args) -> bool:
    return mean((args[0], args[-1])) < mean(args[1:-1])


with open('3_8_10.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = sorted(map(int, str_line.split()))
        if all((is_condition_1(*lst), is_condition_2(*lst))):
            cnt += 1
            print(*lst)
print('Ответ:', cnt)