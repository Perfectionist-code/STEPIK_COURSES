def is_condition_1(*args) -> bool:
    return set(args).__len__() < 6


def is_condition_2(*args) -> bool:
    cnt_odd = 0
    for num in args:
        if num % 2:
            cnt_odd += 1
    return cnt_odd == 3


with open('9-190.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = sorted(map(int, str_line.split()))
        if is_condition_1(*lst) + is_condition_2(*lst) == 1:
            cnt += 1
            print(*lst)
print('Ответ:', cnt)
