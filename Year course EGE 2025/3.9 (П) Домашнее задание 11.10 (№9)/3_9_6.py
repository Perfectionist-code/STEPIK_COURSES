def is_condition_1(*args) -> bool:
    sum_odd = 0
    sum_even = 0
    for num in args:
        if num % 2:
            sum_odd += num
        else:
            sum_even += num
    return sum_odd > sum_even


def is_condition_2(*args) -> bool:
    return len(set(args)) == len(args) - 1


with open('3_9_6.txt', 'r') as file:
    cnt = 0
    for str_line in file:
        lst = list(map(int, str_line.split()))
        if is_condition_1(*lst) + is_condition_2(*lst) == 1:
            cnt += 1
            print(*lst)
print('Ответ:', cnt)